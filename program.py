"""Program code"""

# System Imports
import os

# First-Party imports
from zipcode import Zipcode, Base
from user_interface import UserInterface
from utils import CSVProcessor


# Third Party Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def create_database():
    """Create the database"""
    Base.metadata.create_all(engine)


def populate_database(zip_codes):
    """populate database from list of employees"""
    for zip_code in zip_codes:
        session.add(zip_code)
        session.commit()


def main(*args):
    """Method to run program"""

    zip_codes = []

    # Make a new instance of the UserInterface class
    ui = UserInterface()

    # if we do not have the database, we can create it.
    if not os.path.exists("./db.sqlite3"):
        # Create the database
        create_database()

    if session.query(Zipcode).first() is None:

        # Path to CSV file
        path_to_csv_file = "2023zipcodes.csv"

        # Make new instance of CSVProcessor class
        csv_processor = CSVProcessor()

        # Reading the CSV file could raise exceptions. Be sure to catch them.
        try:
            # Call the import_csv method sending in our path to the csv and the Employee list.
            csv_processor.import_csv(path_to_csv_file, zip_codes)
        except FileNotFoundError:
            ui.print_file_not_found_error()
        except EOFError:
            ui.print_empty_file_error()

        # Populate the database with data from CSV
        populate_database(zip_codes)

    # Get some input from the user
    selection = ui.display_menu_and_get_response()

    # While the choice they selected is not 2, continue to do work.
    while selection != ui.MAX_MENU_CHOICES:
        # See if the input they sent is equal to 1.

        if selection == 1:
            #"""print zip codes by string relation"""

        if selection == 2:
            #print one line by zip

            single_employee_by_criteria = (
                session.query(zip_codes)
                .filter(
                    Zipcode.zip_code == "49002",
                )
                .first()
            )
            ui.print_entry(single_employee_by_criteria)

        if selection == 3:
            #"""print all"""

        if selection == 4:
            #"""print by state"""

        if selection == 5:
            #"""calculate distance between zips"""

        if selection == 6:
            #"""find all other zip codes in radius"""

        if selection == 7:
            #"""map total distance in series of zips"""

        # if selection == 1:

        #     ##########################################################
        #     # Query and print out all entries                        #
        #     ##########################################################
        #     ui.print("Query and print out all entries")

        #     # get the employees from the database
        #     employees = session.query(Employee).all()

        #     # Create string for concatenation
        #     output_string = ""

        #     # Convert each employee to a string and add it to the outputstring
        #     for employee in employees:
        #         # Concatenate to the output_string
        #         output_string += f"{employee}{os.linesep}"

        #     # Use the UI class to print out the string
        #     ui.print_list(output_string)
        #     ##########################################################
        #     # Query single entry and primary key                     #
        #     ##########################################################
        #     ui.print("Query single entry by primary key")
        #     employee_by_pk = session.query(Employee).get(1)
        #     ui.print_entry(employee_by_pk)
        #     ##########################################################
        #     # Query single entry by criteria                         #
        #     ##########################################################
        #     ui.print("Query single entry by criteria")
        #     single_employee_by_criteria = (
        #         session.query(ZipCode)
        #         .filter(
        #             Zipcode.zip_code == "49002",
        #         )
        #         .first()
        #     )
        #     ui.print_entry(single_employee_by_criteria)
        #     ##########################################################
        #     # Query multiple entries by criteria                     #
        #     ##########################################################
        #     ui.print("Query multiple entries by criteria")
        #     employee_by_criteria = (
        #         session.query(Employee).filter(Employee.weekly_salary > 400)
        #     ).all()
        #     output_string = ""
        #     for employee in employee_by_criteria:
        #         output_string += f"{employee}{os.linesep}"
        #     ui.print_list(output_string)

        #     # Add new entry to thedatabase
        #     ui.print("add new entry")
        #     new_employee = Employee("David", "Barnes", 999.99)
        #     session.add(new_employee)
        #     session.commit()
        #     employees = session.query(Employee).all()
        #     output_string = ""
        #     for employee in employees:
        #         output_string += f"{employee}{os.linesep}"
        #     ui.print_list(output_string)

        #     # Update an entry in the database
        #     ui.print("update an entry")
        #     employee_to_update = (
        #         session.query(Employee)
        #         .filter(
        #             Employee.first_name == "David",
        #         )
        #         .first()
        #     )
        #     ui.print_entry(employee_to_update)
        #     employee_to_update.last_name = "BBBBArnesss"
        #     session.commit()

        #     employees = session.query(Employee).all()
        #     output_string = ""
        #     for employee in employees:
        #         output_string += f"{employee}{os.linesep}"
        #     ui.print_list(output_string)

        #     # Delete an entry from the database
        #     ui.print("delete an entry from database")
        #     employee_to_delete = (
        #         session.query(Employee).filter(Employee.first_name == "David").first()
        #     )
        #     ui.print_entry(employee_to_delete)
        #     session.delete(employee_to_delete)
        #     session.commit()

        #     employee_to_delete = (
        #         session.query(Employee).filter(Employee.first_name == "David").first()
        #     )
        #     ui.print_entry(employee_to_delete)

        #     if employee_to_delete is None:
        #         ui.print("Record successfully deleted")

        #     employees = session.query(Employee).all()
        #     output_string = ""
        #     for employee in employees:
        #         output_string += f"{employee}{os.linesep}"
        #     ui.print_list(output_string)

        # # Check for different choice here if there was one to check.

        # # Lastly, re-prompt user for input on what to do.
        # selection = ui.display_menu_and_get_response()
