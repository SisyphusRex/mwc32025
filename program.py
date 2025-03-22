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

def terminate_option():
    print("Do you wish to continue using the program?: ")
    keep_running = input("Y/N")
    if keep_running == "N":
        return True

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
            ...
        if selection == 2:
            #print one line by zip
            zip_code_to_search = input("Enter the zip you wish to search: ")
            single_zip_code_by_criteria = (
                session.query(Zipcode)
                .filter(
                    Zipcode.zip_code == zip_code_to_search,
                )
                .first()
            )
            print(single_zip_code_by_criteria)
            if terminate_option():
                break

        if selection == 3:
            #print all
            all_zip_codes = session.query(Zipcode).all()
            for line in all_zip_codes:
                print(line)

            if terminate_option():
                break
        if selection == 4:
            #"""print by state"""
           state_to_search = input("Enter the state you wish to search: ")
           zip_codes_by_criteria = (
                session.query(Zipcode)
                .filter(
                    Zipcode.state == state_to_search,
                )
                .all()
            )
            
        if selection == 5:
            #"""calculate distance between zips"""
            ...
        if selection == 6:
            #"""find all other zip codes in radius"""
            ...
        if selection == 7:
            #"""map total distance in series of zips"""
            ...

        if selection == 8:
            break
