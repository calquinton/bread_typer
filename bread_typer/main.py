# import game classes and libraries
from game import constants
from game.displayer import Displayer
from game.quotes import Quotes
from game.scorer import Scorer
from game.timer import Timer
from game.typer import Typer
import random

def main():
    '''
    Controls the entire program by calling
    class functions.
    '''
    
    # get quotes_list from Quotes
    quotes_list = Quotes.create_quotes_list()

    # get random list from quotes_list
    quote_list = quotes_list[random.randint(1, len(quotes_list))]

    quote = quote_list[1]
    quote_source = quote_list[2]

    # display quote
    Displayer.print_string(quote)

    # start timer
    start_time = Timer.check_current_time()

    # accept player input
    player_input = Typer.get_input()

    # end timer
    end_time = Timer.check_current_time()

    # calculate time spent typing
    typing_time_seconds = Timer.calculate_time_difference(start_time, end_time)

    # convert typing time to minutes
    typing_time_minutes = Timer.convert_seconds_to_minutes(typing_time_seconds)

    # create Scorer object
    score = Scorer()

    # calculate words per minute, stored in score object
    score._wpm = Scorer.calculate_wpm(player_input, typing_time_minutes)

    # calculate accuracy, stored in score object
    score._accuracy = Scorer.calculate_accuracy(quote, player_input)

    # display quote source
    Displayer.print_string(constants.CREDIT_STRING)
    Displayer.print_string(quote_source)

    # display score
    # wpm
    Displayer.print_string(constants.SCORE_WPM_STRING)
    Displayer.print_string(score._wpm)

    # accuracy
    Displayer.print_string(constants.SCORE_ACCURACY_STRING)
    Displayer.print_string(score._accuracy)

    # end of program

# call main
main()
    