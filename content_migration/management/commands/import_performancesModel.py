# Question Page import

# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from performances.models import Performances, PerformanceFeatsLink
from events.models import CategoryEventCollection


# create command class
class Command(BaseCommand):
    help = "Import Performance data"

    # parse csv file?
    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str)



    def handle(self, *args, **options):
        # get instance of the key question index page / folder
        # get parent folder these pages will be placed in
        # parent_page = Page.objects.get(title='Key Questions').specific

        # Create Feat Orderable Function
        def createOrderable(orderList, entry):

            # loop through all List items


            for i in orderList:


                newFeat = PerformanceFeatsLink(performance_feats=i, page_id=entry.id)
                print("FEAt: ", newFeat)
                newFeat.save()




        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            performances = csv.DictReader(import_file)

            # print('PERFORMANCES: ', performances)
            # loop through questions and for every question create a page
            for perf in performances:
                # print('PERF: ', perf)
                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page
                category_event = CategoryEventCollection.objects.get(collection_event=perf["event_collection"].upper())
                print('CATEGORY EVENT: ', category_event)


                # # IMPORT
                import_pref = Performances.objects.create(
                    event_collection = category_event,
                    performance_title = perf["perf_title"],
                    performance_overview = perf["perf_overview"],
                    performance_description = perf["perf_description"],
                    # performance_assignment = perf["pref_assignment"],
                    # star_value = pref["star_value"],
                    # performance_lexis_link

                )


                # Import orderable

                # get array from csv for icons
                feat_string = perf["perf_feats"]

                # check if string is available to eval
                # needed due to empty feats
                if feat_string:
                    # convert string to list
                    orderList = ast.literal_eval(feat_string)
                    print(orderList)

                # IMPORT
                # pass function OrderList and newEntry to function
                #     check to make sure order list isn't empty'
                    if len(orderList) > 0:
                        createOrderable(orderList, import_pref)

                    print('import_pref: ', import_pref)

        # print all done
        self.stdout.write("All done!")

#
# invoke the file in the command line

# folder structure
# create app content_mmigration
# create folder structure management / commands / commandfile.py
# put data in .data folder in root
# import_questions = import_questions.py file

# --file="PATH TO CSV FILE"
# $ python manage.py import_performancesModel --file=".data/aswl_e1_performances3.csv"


# NOW DO YOU IMPORT AN ORDERABLE M2M relationship import
# HOW DO YOU HANDLE A STUCT BLOCK STREAM IMPORT