# Question Page import

# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from extensions.models import Extensions, ExtensionLexisLink
from categories.models import ExtensionCommandType
from lexis.models import Lexis
from events.models import CategoryEventCollection

# create command class
class Command(BaseCommand):
    help = "Import key question data"

    # parse csv file?
    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str)



    def handle(self, *args, **options):
        # get instance of the key question index page / folder
        # get parent folder these pages will be placed in
        # parent_page = Page.objects.get(title='Key Questions').specific

        # Create Icon Orderable Function for Lexis
        def createOrderable(orderList, id):

            # loop through all List items
            if orderList:
                for i in orderList:
                    # create and save a new icon row in IconList table passing
                    # fetch the lexisterm to get the id
                    term = Lexis.objects.get(term=i)
                    print('TERM: ', term)
                    print('TERMID: ', term.id)

                    if term:
                        lex = ExtensionLexisLink(term_link_id=term.id, page_id=id)
                        print('LEX: ', lex)
                    # lex.save()

            return





        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            extensions = csv.DictReader(import_file)

            # loop through questions and for every question create a page
            for ex in extensions:
                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page

                if ex["event_collection"]:
                    category_event = CategoryEventCollection.objects.get(
                        collection_event=ex["event_collection"].upper())

                    # category_event = CategoryEventCollection.objects.get(id=ex["event_collection"])
                    print('CATEGORY EVENT: ', category_event)
                else:
                    category_event = None
                # print('QUESTION: ', book["question"])

                # get assignment command link
                print('COMMAND: ', ex["assignment_command_type"])
                assignment_link = ExtensionCommandType.objects.get(command_name=ex["assignment_command_type"])
                print('ASS_LINK: ', category_event)




                # IMPORT
                import_ext = Extensions.objects.create(
                    assignment_command_types=assignment_link,
                    event_collection=category_event,
                    action=ex["action"],
                    explanation=ex["explanation"],

                )

                # TEST
                # import_ext = Extensions(
                #     assignment_command_types=assignment_link,
                #     event_collection=category_event,
                #     action=ex["action"],
                #     explanation=ex["explanation"],
                #
                # )

                print('IMPORT_EXT: ', import_ext)
                print('IMPORT_EXT_ID: ', import_ext.id)


                # Import orderable
                # get array from csv for lex links

                lex_string = ex["lexis_links"]

                if lex_string:

                    # convert string to list
                    orderList = ast.literal_eval(lex_string)
                    print(orderList)

                    # pass function OrderList and newEntry.id to function
                    createOrderable(orderList, import_ext.id)





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
# $ python manage.py import_extensionsModel --file=".data/aswl_e1_extensionsB.csv"


# NOW DO YOU IMPORT AN ORDERABLE M2M relationship import
# HOW DO YOU HANDLE A STUCT BLOCK STREAM IMPORT