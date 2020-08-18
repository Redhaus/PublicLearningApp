
# Model Import


# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models

from lexis.models import Lexis, IconList
from events.models import CategoryEventCollection


# create command class
class Command(BaseCommand):
    help = "Import LexisModel data"

    # parse csv file?
    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str)


    def handle(self, *args, **options):

        # get instance of the key question index page / folder
        # get parent folder these pages will be placed in
        # parent_page = Page.objects.get(title='Lexis').specific


        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            lexis = csv.DictReader(import_file)



            # Create Icon Orderable Function
            def createOrderable(orderList, entry):

                # working write tag
                # In[1]: testtag = Tag(name="blue", slug="blue")
                # In[2]: testtag.save()

                # loop through all List items
                for i in orderList:

                    # create and save a new icon row in IconList table passing
                    # icon and lexis parent page id
                    icon = IconList(icons=i, page_id=entry.id)
                    icon.save()





            # usage createBlock(item, 'exploration', 'Exploration')
            def createBlock(item, column, blockName):

                # get list of items from csv item
                string_List = item[column]

                finalList = []
                # convert string list to python list
                if string_List:
                    blockList = ast.literal_eval(string_List)
                    print(blockName, blockList)

                    # create an empty array list to pass to new lexi obj
                    # finalList = []

                    # create a tuple for every item in explorations list and add to exlist
                    for i in blockList:
                        # blockName is the Struct Type, and I is the value
                        finalList.append((blockName, i))


                # return struct final list
                return finalList


            # loop through questions and for every question create a page
            for item in lexis:

                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page
                # category_event = CategoryEventCollection.objects.get(id=item["event_collection_id"])
                category_event = CategoryEventCollection.objects.filter(collection_event=item["event_collection"].upper()).first()

                # collection_event
                print('TERM TERM TERM: ', item['term'])
                print('CATEGORY EVENT: ', category_event)


                exList = createBlock(item, 'exploration', 'Exploration')
                derList = createBlock(item, 'derivations', 'Derivations')
                rootList = createBlock(item, 'roots', 'Lexis_Root')
                highList = createBlock(item, 'highlight', 'Highlight')
                appList = createBlock(item, 'application', 'Application')



                print('TERM TERM: ', item['term'])
                print('EXLIST: ', exList)
                print('DERLIST: ', derList)
                print('ROOTLIST: ', rootList)
                print('HIGHLIST: ', highList)
                print('APPLIST: ', appList)



            # IMPORT
            # create var reference for lexisModel

                import_lexis = Lexis.objects.create(

                    term=item["term"],
                    part_of_speech=item["part_of_speech"],
                    etymology=item["etymology"],
                    quotation=item["quote"],
                    quotation_author=item["author"],
                    quote_source=item["source_major"],
                    event_collection=category_event,

                    # struct imports
                    exploration=exList,
                    lexis_root=rootList,
                    derivations=derList,
                    highlight=highList,
                    application=appList

                )


                # TEST
                # import_lexis = Lexis(
                #
                #     term=item["term"],
                #     part_of_speech=item["part_of_speech"],
                #     etymology=item["etymology"],
                #     quotation=item["quote"],
                #     quotation_author=item["author"],
                #     quote_source=item["source_major"],
                #     event_collection=category_event,
                #
                #     # struct imports
                #     exploration=exList,
                #     lexis_root=rootList,
                #     derivations=derList,
                #     highlight=highList,
                #     application=appList
                #
                # )


                # Import orderable

                # get array from csv for icons
                icon_string = item["icons"]
                # convert string to list
                orderList = ast.literal_eval(icon_string)

                print(import_lexis)
                print(orderList)


                # IMPORT
                # pass function OrderList and newEntry to function
                createOrderable(orderList, import_lexis)




        # print all done
        self.stdout.write("All done!")


# --file="PATH TO CSV FILE"
# Import file 01 - 05 in lexis folder
# $ python manage.py import_lexisModel --file=".data/aswl_e1_fullLexisB.csv"



