# Question Page import

# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from assignments_types.models import AudienceTypes

# create command class
class Command(BaseCommand):
    help = "Import key question data"

    # parse csv file?
    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str)


    def handle(self, *args, **options):


        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            audience_types = csv.DictReader(import_file)

            # loop through questions and for every question create a page
            for item in audience_types:

                # # IMPORT
                import_audience = AudienceTypes.objects.create(
                    audience=item["audience_type"],
                )

                # TEST
                # import_audience = AudienceTypes(
                #     audience=item["audience_type"],
                #     # question=question["question"],
                # )

                print(import_audience)


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
# $ python manage.py import_audience_types --file=".data/Audience_Types.csv"



