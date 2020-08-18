# Question Page import

# import csv lib
import csv

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from key_questions.models import KeyQuestions
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


        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            questions = csv.DictReader(import_file)

            # loop through questions and for every question create a page
            for question in questions:

                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page
                category_event = CategoryEventCollection.objects.get(collection_event=question["event_collection"].upper())
                print('CATEGORY EVENT: ', category_event)
                print('QUESTION: ', question["question"])

                # create question page
                # assign fields to each item
                # category_event is the FK above


                # IMPORT
                import_question = KeyQuestions.objects.create(
                    event_collection=category_event,
                    question=question["question"],
                    # explanation=question["explanation"],
                    # video_link=question["video_link"],

                )

                # TEST
                # import_question = KeyQuestions(
                #     event_collection=category_event,
                #     question=question["question"],
                #     # explanation=question["explanation"],
                #     # video_link=question["video_link"],
                #
                # )


                print('IMPORTQ: ', import_question)



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
# $ python manage.py import_questionsModel --file=".data/aswl_e1_keyquestionsD.csv"






# NOW DO YOU IMPORT AN ORDERABLE M2M relationship import
# HOW DO YOU HANDLE A STUCT BLOCK STREAM IMPORT


















