# Question Page import

# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from readings.models import PrimaryFocus
from categories.models import ReadingCategory
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

        # Create Tag Orderable Function
        # def createOrderable(orderList, entry):
        #
        #     # working write tag
        #     # In[1]: testtag = Tag(name="blue", slug="blue")
        #     # In[2]: testtag.save()
        #
        #     # connect tag to model
        #     # In[4]: newTag = FurtherExplorationTag(content_object_id=2, tag_id=testtag.id)
        #     # In[5]: newTag.save()
        #     # In[6]: newTag.id
        #
        #     # loop through all List items
        #     for i in orderList:
        #         # create and save a new icon row in IconList table passing
        #         # icon and lexis parent page id
        #         islug = slugify(i)
        #
        #         lookup = Tag.objects.filter(slug=islug).first()
        #         print('LOOKUP ', lookup)
        #
        #         if lookup:
        #             newTag = FurtherExplorationTag(content_object_id=entry.id, tag_id=lookup.id)
        #             newTag.save()
        #
        #         else:
        #
        #             tag = Tag(name=i, slug=islug)
        #             tag.save()
        #
        #             newTag = FurtherExplorationTag(content_object_id=entry.id, tag_id=tag.id)
        #             newTag.save()
        #
        #         #
        #         # IconList(icons=i, page_id=entry.id)
        #         # icon.save()



        # usage createBlock(item, 'exploration', 'Exploration')
        def createBlock(item, column, blockName):

            # get list of items from csv item
            string_List = item[column]

            # create an empty array list to pass to new lexi obj
            finalList = []
            # convert string list to python list
            if string_List:
                blockList = ast.literal_eval(string_List)
                print(blockName, blockList)

                # create a tuple for every item in explorations list and add to exlist
                for i in blockList:
                    # blockName is the Struct Type, and I is the value
                    finalList.append((blockName, i))

            # return struct final list
            return finalList




        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            books = csv.DictReader(import_file)

            # loop through questions and for every question create a page
            for book in books:
                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page

                category_event = CategoryEventCollection.objects.get(collection_event=book["event_collection"].upper())
                print('CATEGORY EVENT: ', category_event)
                # print('QUESTION: ', book["question"])

                reading_category = ReadingCategory.objects.get(category_name=book["category"])
                print('READING CATEGORY: ', category_event)

                KEYS = createBlock(book, 'keywords', 'Keywords')


                print('LEVEL: ', book["level"],)

                # create question page
                # assign fields to each item
                # category_event is the FK above

                # IMPORT
                import_book = PrimaryFocus.objects.create(
                    keywords=KEYS,
                    event_collection=category_event,
                    author_dob=book["birthdate"],
                    author_first_name=book["author_first_name"],
                    author_last_name=book["author_last_name"],
                    title_major=book["title_major"],
                    synopsis=book["synopsis"],
                    purchase_link=book["purchase_link"],
                    page_count=book["page_count"],
                    reading_category=reading_category,
                    source=book["source"],
                    level_ability=book["level"],


                )


                # TEST
                # import_book = PrimaryFocus(
                #     keywords=KEYS,
                #     event_collection=category_event,
                #     author_dob=book["birthdate"],
                #     author_first_name=book["author_first_name"],
                #     author_last_name=book["author_last_name"],
                #     title_major=book["title_major"],
                #     synopsis=book["synopsis"],
                #     purchase_link=book["purchase_link"],
                #     page_count=book["page_count"],
                #     reading_category=reading_category,
                #     source=book["source"],
                #     level_ability=book["level"]
                #
                # )

                # print('LEVEL', book["level"])

                # Import orderable

                # get array from csv for icons
                # tag_string = book["keywords"]
                # convert string to list
                # orderList = ast.literal_eval(tag_string)

                # print(import_book)
                # print(orderList)
                # print(tag_string)

                # IMPORT
                # pass function OrderList and newEntry to function
                # createOrderable(orderList, import_book)


                # print('IMPORT', import_book)

                # add child page to the parent page
                # parent_page.add_child(instance=import_question)

                # save page
                # parent_page.save()

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
# $ python manage.py import_primaryFocusModel --file=".data/aswl_e1_primaryFocusB.csv"


# NOW DO YOU IMPORT AN ORDERABLE M2M relationship import
# HOW DO YOU HANDLE A STUCT BLOCK STREAM IMPORT