"""Utils module"""

# First-part Imports
from zipcode import Zipcode


class CSVProcessor:
    """CSV Processor Class to read and process an employee csv file."""

    # No Constructor as we do not need to accept any parameters or set any
    # class level variables. But, this does not mean that we can't do that
    # in the event that we do need something.

    def import_csv(self, path_to_csv_file, zip_list):
        """Accept a path to a csv file, then read the file in and process it
        into a list of employee instances"""

        # With open of file
        with open(path_to_csv_file, "r", encoding="utf-8") as file:
            # Priming line read
            line = file.readline().replace("\n", "")
            # While the line is not None
            while line:
                # Process the line.
                self._process_line(line, zip_list)
                # Read next line.
                line = file.readline().replace("\n", "")

    def _process_line(self, line, zip_list):
        """Process a line from a CSV file"""

        # Split line by comma
        parts = line.split(",")

        # Assign each part to a var
        zip_code = parts[0]
        city = parts[1]
        state = parts[2]
        latitude = parts[3]
        longitude = parts[4]

        # Add a new beverage to the collection with the properties of what was read in.
        zip_list.append(Zipcode(zip_code, city, state, latitude, longitude))
