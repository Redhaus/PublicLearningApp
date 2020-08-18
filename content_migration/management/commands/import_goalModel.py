
# Model Import


# import csv lib
import csv
import ast

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from continual_goals.models import ContinualGoals
from categories.models import ContinualGoalStandardType

# create command class
class Command(BaseCommand):
    help = "Import Continual Goals data"

    # parse csv file?
    def add_arguments(self, parser):
        parser.add_argument("--file", action="store", type=str)


    def handle(self, *args, **options):

        # get instance of the key question index page / folder
        # get parent folder these pages will be placed in
        # parent_page = Page.objects.get(title='Lexis').specific


        with open(options["file"]) as import_file:
            # create questions dictionary from csv file
            goals = csv.DictReader(import_file)


            # loop through questions and for every question create a page
            for goal in goals:

                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page
                standard_type = ContinualGoalStandardType.objects.get(standard_type=goal["type"])

                print('STANDARDTYPE: ', standard_type)
                print('GOALS: ', goal["goals"])



                # IMPORT var reference for goalModel
                import_goal = ContinualGoals.objects.create(

                    standard_type=standard_type,
                    goal=goal["goals"]

                )


                # TEST
                # import_goal = ContinualGoals(
                #
                #     standard_type=standard_type,
                #     goal=goal["goals"]
                #
                # )

                print(import_goal)


        # print all done
        self.stdout.write("All done!")


# --file="PATH TO CSV FILE"
# $ python manage.py import_goalModel --file=".data/aswl_e1_continual_goals.csv"



