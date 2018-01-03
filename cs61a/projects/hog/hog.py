"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    total = 0
    rolls = []
    count_1 = 0
    while num_rolls > 0:
        rolls += [dice()]
        num_rolls -= 1
    for i in rolls:
        if i == 1:
            count_1 += 1
        else:
            total += i
    if count_1 == 0:
        return total
    else:
        return count_1
    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    digits = []
    for i in str(opponent_score):
        digits += [int(i)]
    freescore = max(digits)
    return freescore + 1
    # END PROBLEM 2


# Write your prime functions here!
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def next_prime(number):
    number += 1
    while not is_prime(number):
        number += 1
    return number

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    
    if num_rolls == 0:
        freebacon = free_bacon(opponent_score)
        if is_prime(freebacon):
            return next_prime(freebacon)
        else:
            return freebacon
    score = roll_dice(num_rolls, dice)
    if is_prime(score):
        return min(next_prime(score), 25 - num_rolls)
    else:
        return min(score, 25 - num_rolls)

    # END PROBLEM 2


def reroll(dice):
    """Return dice that return even outcomes and reroll odd outcomes of DICE."""
    def rerolled():
        # BEGIN PROBLEM 3
        result = dice()
        if result % 2 != 0:
            result = dice()
        return result # Replace this statement
        # END PROBLEM 3
    return rerolled


def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    """
    # BEGIN PROBLEM 4
    dice = six_sided
    if dice_swapped:
        dice = four_sided
    if (score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    # END PROBLEM 4
    return dice


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    # BEGIN PROBLEM 5
    
    
    
    while score1 < goal and score0 < goal:
        if player == 0:
            numrolls0 = strategy0(score0, score1)
            if numrolls0 == -1:
                score0 += 1
                dice_swapped = not dice_swapped
            else:
                dice0 = select_dice(score0, score1, dice_swapped)
                score0 = score0 + take_turn(numrolls0, score1, dice0)
        else:
            numrolls1 = strategy1(score1, score0)
            if numrolls1 == -1:
                score1 += 1
                dice_swapped = not dice_swapped
            else:
                dice1 = select_dice(score1, score0, dice_swapped)
                score1 = score1 + take_turn(numrolls1, score0, dice1)
        if score1 * 2 == score0 or score0 * 2 == score1:
            score0, score1 = score1, score0
        player = other(player)
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    score1 = 0
    while score1 <= goal:
        for score0 in range(0,goal):
            assert strategy(score0, score1) <= 10, "Invalid number of rolls."
        score1 += 1
    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    def averaged(*args):
        total = 0
        for i in range(0, num_samples):
            total += fn(*args)
        return total / num_samples
    return averaged
    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    average_results = []
    for n in range(1,11):
        average = make_averaged(roll_dice, num_samples)
        average_results += [average(n, dice)]
    return average_results.index(max(average_results)) + 1
    # END PROBLEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    freebaconscore = free_bacon(opponent_score)
    if is_prime(freebaconscore):
        freebaconscore = next_prime(freebaconscore)
    if freebaconscore >= margin:
        return 0
    else:
        return num_rolls
    # END PROBLEM 9
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    free_bacon_score = free_bacon(opponent_score)
    bacon_strategy_result = bacon_strategy(score, opponent_score, margin, num_rolls)

    if is_prime(free_bacon_score):
        free_bacon_score = next_prime(free_bacon_score)
    
    if (free_bacon_score + score) * 2 == opponent_score or bacon_strategy_result == 0:
        return 0
    else:
        return num_rolls  # Replace this statement
    # END PROBLEM 10
check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    The strategy will assess first the free_bacon_score, or the score obtained
    should the player roll 0. The next two functions assess whether hog wild is    
    in effect. Following this, right from the beginning of the game the player
    will activate pork chop, such that the game takes longer, and that there is 
    more time to maneuver and change strategies, as well as a decreased likelihood
    of the opponent quickly winning by chance. Finally, there are two sets of 
    conditions under which the player would be more inclined to take risks; the 
    first one, if the player has fewer than 55 points, or is more than 10 points 
    behind the opponent, greater risks will be taken (shown by higher roll count 
    and margin); the second, if greater than 55 or more than 10 points ahead of 
    the opponent, fewer risks will be taken. In both of these brackets, if hog wild
    is in effect, greater risks will also be taken, as hog wild will decrease the chances
    of pig out taking effect. Finally, for each time assessing the final strategy, 
    the code will return whether or not free bacon should be taken, given the margins
    and number of rolls.

    is_hog_wild_player -- whether or not hog wild is active
    """
    # BEGIN PROBLEM 11
    


    def is_hog_wild_player(score, opponent_score):
        return (score + opponent_score) % 7 == 0

    if score == 0:
        num_rolls = -1
        return num_rolls

    if score <= 55 or score + 10 < opponent_score:
        if is_hog_wild_player(score, opponent_score):
            margin = 9
            num_rolls = 6
        else:
            margin = 6
            num_rolls = 5
    elif score > 55 or score > opponent_score + 10:
        if is_hog_wild_player(score, opponent_score):
            margin = 6
            num_rolls = 5
        else:
            margin = 6
            num_rolls = 4
    

    return swap_strategy(score, opponent_score, margin, num_rolls)
        
    #return num_rolls
    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()