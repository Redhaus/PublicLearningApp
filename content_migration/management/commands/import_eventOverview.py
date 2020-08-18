# Question Page import

# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
# from readings.models import PrimaryFocus
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

        # usage createBlock(item, 'exploration', 'Exploration')
        # def createBlock(item, column, blockName):
        #
        #     # get list of items from csv item
        #     string_List = item[column]
        #
        #     # create an empty array list to pass to new lexi obj
        #     finalList = []
        #     # convert string list to python list
        #     if string_List:
        #         blockList = ast.literal_eval(string_List)
        #         print(blockName, blockList)
        #
        #         # create a tuple for every item in explorations list and add to exlist
        #         for i in blockList:
        #             # blockName is the Struct Type, and I is the value
        #             finalList.append((blockName, i))
        #
        #     # return struct final list
        #     return finalList




        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            events = csv.DictReader(import_file)

            # loop through questions and for every question create a page
            for event in events:
                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page

                # category_event = CategoryEventCollection.objects.get(collection_event=book["event_collection"].upper())
                # print('CATEGORY EVENT: ', category_event)
                # print('QUESTION: ', book["question"])

                # reading_category = ReadingCategory.objects.get(category_name=book["category"])
                # print('READING CATEGORY: ', category_event)

                # KEYS = createBlock(book, 'keywords', 'Keywords')


                # print('LEVEL: ', book["level"],)

                # create question page
                # assign fields to each item
                # category_event is the FK above

                # IMPORT
                import_events = CategoryEventCollection.objects.create(
                    collection_name=event["collection"],
                    collection_event=event["event_category"],
                    event_title=event["event_title"],
                    event_descriptor=event["event_descriptor"],
                    quotation=event["quotation"],
                    quotation_author=event["quotation_author"],
                    quote_source=event["quote_source"],

                )


                # TEST
                # import_events = CategoryEventCollection(
                #     collection_name=event["collection"],
                #     collection_event=event["event_category"],
                #     event_title=event["event_title"],
                #     event_descriptor=event["event_descriptor"],
                #     quotation=event["quotation"],
                #     quotation_author=event["quotation_author"],
                #     quote_source=event["quote_source"],
                #
                #
                # )

                # print('LEVEL', book["level"])
                print('IMPORT', import_events)

                # add child page to the parent page
                # parent_page.add_child(instance=import_question)

                # save page
                # parent_page.save()

        # print all done
        self.stdout.write("All done!")


 #
 # MultiFieldPanel(
 #            [
 #                FieldPanel("collection_name", classname="col6"),
 #                FieldPanel("collection_event", classname="col6"),
 #                FieldPanel("event_title", classname="col12 line"),
 #                FieldPanel("event_descriptor"),
 #            ],
 #            heading="Event Info",
 #        ),
 #
 #        # group together all the panels for banner in a multi field panel
 #        MultiFieldPanel(
 #            [
 #                FieldPanel("quotation"),
 #                FieldPanel("quotation_author"),
 #                FieldPanel("quote_source"),
 #                ImageChooserPanel("author_image"),
 #            ],
 #            heading="Quote Options",
 #        ),




#
# invoke the file in the command line

# folder structure
# create app content_mmigration
# create folder structure management / commands / commandfile.py
# put data in .data folder in root
# import_questions = import_questions.py file

# --file="PATH TO CSV FILE"
# $ python manage.py import_eventOverview --file=".data/aswl_e1_event_overviewB.csv"


# NOW DO YOU IMPORT AN ORDERABLE M2M relationship import
# HOW DO YOU HANDLE A STUCT BLOCK STREAM IMPORT