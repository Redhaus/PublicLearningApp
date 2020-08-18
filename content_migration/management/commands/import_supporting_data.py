# Question Page import

# import csv lib
import csv

# import management command
from django.core.management.base import BaseCommand, CommandError

# import needed models
from categories.models import ContinualGoalStandardType, ExtensionCommandType, ReadingCategory
# from events.models import CategoryEventCollection
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
            support_data = csv.DictReader(import_file)

            # loop through questions and for every question create a page
            for data in support_data:

                # for every foreign key relationship you will need to import that model
                # get that specific object with the id reference and apply it to the page
                # category_event = CategoryEventCollection.objects.get(id=question["event_collection"])
                # print('CATEGORY EVENT: ', category_event)
                # print('QUESTION: ', question["question"])

                # create question page
                # assign fields to each item
                # category_event is the FK above

# //////////////////////////////////////////////////
#                 if data["icons"]:
#                     # IMPORT READING
#                     import_icon_category = IconCategory.objects.create(
#                           icon_category=data["icons"],
#                     )
#
#
#                     # TEST
#
#                     # import_icon_category = IconCategory(
#                     #     icon_category=data["icons"],
#                     # )
#
#                     print('ICONS: ', import_icon_category)



# //////////////////////////////////////////////////
                if data["reading_category"]:
                    # IMPORT READING
                    import_reading_category = ReadingCategory.objects.create(
                        category_name=data["reading_category"],
                    )

                    # TEST
                    # import_reading_category = ReadingCategory(
                    #     category_name=data["reading_category"],
                    # )

                    print(import_reading_category)


# //////////////////////////////////////////////////

                if data["extension_command_type"]:
                    # IMPORT CategoryEventCollection ///////////////////////////////
                    import_extension = ExtensionCommandType.objects.create(
                         command_name = data["extension_command_type"],

                    )

                    # TEST
                    # import_extension = ExtensionCommandType(
                    #     command_name=data["extension_command_type"],
                    #
                    # )

                    print(import_extension)



# //////////////////////////////////////////////////

                if data["continual_goal"]:
                    # IMPORT continual_goal ///////////////////////////////
                    import_continual_goal = ContinualGoalStandardType.objects.create(
                                            standard_type = data["continual_goal"],
                                        )

                    # TEST
                    # import_continual_goal = ContinualGoalStandardType(
                    #     standard_type=data["continual_goal"],
                    #
                    # )

                    print(import_continual_goal)

        # print all done
        self.stdout.write("All done!")

# --file="PATH TO CSV FILE"
# import_supporting_data is py file
# $ python manage.py import_supporting_data --file=".data/ideal_supporting_data.csv"

