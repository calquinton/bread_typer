import csv

class FileProcessor:
    '''
    Reads csv files and returns specific lines and values
    '''

    def __init__(self):
        pass

    def get_file_line(self, file_name, line_number):
        '''
        Reads csv files with two values per line only
        Returns values on a given line as a list
        '''
        
        current_line = 0

        # open the file
        with open(file_name, 'r') as file:

            # create a csv reader object
            reader = csv.reader(file)

            # skip the first line
            next(file)

            # read the file one line at a time
            for line in file:

                # iterate current_line by 1
                current_line = current_line + 1
