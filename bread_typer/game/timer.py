# imports
import time

class Timer:
    '''
    A code template for timing how long a process
    takes. Creates a start time, and end time, and
    finds the difference to find the running time.
    '''
    

    def __init__(self):
        pass


    def check_current_time(self):
        '''
        Returns the current time for processing.
        '''

        # return the current time
        return time.time()

    
    def calculate_time_difference(self, start_time, end_time):
        '''
        Takes in two values and calculates the
        difference between them. Intended to find
        the difference between the start time and
        end time of a process to determine how long
        that process took.
        '''

        # return the difference between start_time and end_time
        return end_time - start_time

    
    def convert_seconds_to_minutes(self, seconds):
        '''
        Converts a float in seconds to a float
        in minutes and returns.
        '''

        # return minutes converted from seconds
        return seconds / 60
