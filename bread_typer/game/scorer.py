# imports
import re

class Scorer:
    '''
    Creates values for players words per minute (wpm) and accuracy.

    Attributes:
        _accuracy (float): Typing accuracy as a percentage.
        _wpm (int): Words per minute.
    '''

    def __init__(self):
        ''' The class constructor.'''
        self._accuracy = 0.0
        self._wpm = 0

    def calculate_num_differences(self, string_1, string_2):
        '''
        Calculates the number of differences between
        two strings as an int.
        '''

        # count  and return the number of differences between the strings, adding
        # the difference in length in case one is longer than the other
        return sum(1 for a, b in zip(string_1, string_2) if a != b) + abs(len(string_1) - len(string_2))


    def calculate_accuracy(self, original_string, new_string):
        '''
        Calculates the percentage of one string that is the same as
        the original string. This is used to find the users typing
        accuracy as a percentage.
        '''

        # calculate the number of differences between the two strings
        num_differences = self.calculate_num_differences(original_string, new_string)

        # return accuracy as percentage of differences
        return round((len(original_string) - num_differences) / len(original_string) * 100, 2)
    

    def calculate_wpm(self, typed_string, typing_time_seconds):
        '''
        Calculates gross words per minute from a string and the
        given time in seconds that it took to type.
        '''

        # find the number of words in the string
        num_words = len(re.findall(r'\w+', typed_string))

        # calculate and return wpm
        return round(num_words / typing_time_seconds * 60, 2)
