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
    # create objects for classes
    displayer = Displayer()
    quotes = Quotes()
    scorer = Scorer()
    timer = Timer()
    typer = Typer()
    
    # get quotes_list from quotes
    quotes_list = quotes.create_quotes_list()

    # get random list from quotes_list
    quote_list = quotes_list[random.randint(0, len(quotes_list) - 1)]

    quote = quote_list[0]
    quote_source = quote_list[1]

    # display quote
    displayer.print_string(quote)

    # start timer
    start_time = timer.check_current_time()

    # accept player input
    player_input = typer.get_input()

    # end timer
    end_time = timer.check_current_time()

    # calculate time spent typing
    typing_time = timer.calculate_time_difference(start_time, end_time)

    # convert typing time to minutes
    # typing_time_minutes = timer.convert_seconds_to_minutes(typing_time_seconds)

    # calculate words per minute, stored in score object
    scorer._wpm = scorer.calculate_wpm(player_input, typing_time)

    # calculate accuracy, stored in score object
    scorer._accuracy = scorer.calculate_accuracy(quote, player_input)

    # display quote source
    displayer.print_string(constants.CREDIT_STRING)
    displayer.print_string(quote_source)

    # display score
    # wpm
    displayer.print_string(constants.SCORE_WPM_STRING)
    displayer.print_string(scorer._wpm)

    # accuracy
    displayer.print_string(constants.SCORE_ACCURACY_STRING)
    displayer.print_string(scorer._accuracy)

# call main
main()
    