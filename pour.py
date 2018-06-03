from Carafe import Carafe
import random
from time import time
from datetime import datetime
from collections import namedtuple

CleaningCycle = namedtuple('CleaningCycle', 'initial_fill  extra_drip')
CleaningRun = namedtuple('CleaningRun',   'run_num  carafe  cycle_list')

# Program parameters
CARAFE_CAPACITY = 2000  # Milliliters
NUMBER_OF_RUNS = 400000000
RUNS_PER_DATA_CLEANUP = 1000000
INITIAL_COFFEE_VOLUME = 5.0
MAXIMUM_ALLOWED_CONCENTRATION = 1.0e-6
RUNS_ON_EACH_END_TO_KEEP = 100
REALTIME_PLAYBACK = True
RANDOM_SEED = time()

def perform_carafe_cleaning(initial_volume, final_concentration):
    """Perform one carafe cleaning, starting with an amount of pure coffee and finishing when the final
    concentration is sufficiently low.
    :param initial_volume: Initial volume of pure coffee
    :param final_concentration: Required maximum final concentration to be considered clean
    :return: A tuple of the carafe object and the list of cleaning cycles for the entire cleaning run
    """
    cycle_list = list()
    carafe = Carafe(initial_volume)
    while carafe.concentration > final_concentration:
        initial_fill = random.random() * CARAFE_CAPACITY
        extra_drip = random.random() < 0.5
        carafe.fill(initial_fill)
        carafe.pour_out(extra_drip)
        cycle = CleaningCycle(initial_fill, extra_drip)
        cycle_list.append(cycle)

    return carafe, cycle_list


def clean_up_runs(runs):
    """Clean up the list of runs to maintain a manageable memory footprint. Keeps only the fastest and slowest
    cleaning runs.
    :param runs: List of cleaning runs to manage
    :return: The cleaned-up list of runs
    """
    # Keep only the shortest and longest runs
    sorted_runs = sorted(runs, key=lambda r:  r.carafe.seconds_elapsed)
    if len(sorted_runs) <= 2 * RUNS_ON_EACH_END_TO_KEEP:
        # List of runs is already short enough
        return sorted_runs

    cleaned_runs = sorted_runs[:RUNS_ON_EACH_END_TO_KEEP] + sorted_runs[-RUNS_ON_EACH_END_TO_KEEP:]

    return cleaned_runs


def perform_runs():
    """Perform a simulation running the required number of cleaning runs
    :return: The list of carafe-cleaning runs
    """
    runs = list()
    start_time = datetime.now()
    for run_num in range(NUMBER_OF_RUNS):
        carafe, cycle_list = perform_carafe_cleaning(INITIAL_COFFEE_VOLUME, MAXIMUM_ALLOWED_CONCENTRATION)
        runs.append(CleaningRun(run_num, carafe, cycle_list))
        if not ((run_num + 1) % RUNS_PER_DATA_CLEANUP):
            # Time to clean up the list of runs, in order to maintain a manageble memory footprint
            runs = clean_up_runs(runs)

            # Print a summary
            num_runs_completed = run_num + 1
            elapsed_run_time = datetime.now() - start_time
            print(f'Simulation {num_runs_completed} ({100.0 * (num_runs_completed) / NUMBER_OF_RUNS}%) of '
                  f'{NUMBER_OF_RUNS} done in {elapsed_run_time}')
            run = runs[0]
            print(f'Fastest run took {len(run.cycle_list)} cycles in {run.carafe.seconds_elapsed} seconds: {run}')
            run = runs[-1]
            print(f'Slowest run took {len(run.cycle_list)} cycles in {run.carafe.seconds_elapsed} seconds: {run}')
            runs_remaining = NUMBER_OF_RUNS - num_runs_completed
            time_per_run = elapsed_run_time / num_runs_completed
            time_remaining = runs_remaining * time_per_run
            eta = datetime.now() + time_remaining
            print(f'{runs_remaining} remaining, estimated remaining time {time_remaining}, estimated completion {eta}')

    runs = clean_up_runs(runs)
    return runs


def display_runs(runs):
    """Display a summary of the fastest and slowest runs, provided a list of runs
    :param runs: The list of runs for which to display a summary
    :return: None
    """
    runs.sort(key=lambda r: r.carafe.seconds_elapsed)
    for run_num in range(100):
        run = runs[run_num]
        print(f'{run_num + 1} Fastest run took {len(run.cycle_list)} '
              f'cycles in {run.carafe.seconds_elapsed} seconds: {run.cycle_list}')
    fastest_run = runs[0]

    print('')
    runs.sort(key=lambda r: r.carafe.seconds_elapsed, reverse=True)
    for run_num in range(100):
        run = runs[run_num]
        print(f'{run_num + 1} Slowest run took {len(run.cycle_list)} '
              f'cycles in {run.carafe.seconds_elapsed} seconds: {run.cycle_list}')

    print('\nPlaying back fastest run')
    fastest_run.carafe.play_back_events(REALTIME_PLAYBACK)

if __name__ == "__main__":
    """Main program
    """
    random.seed(RANDOM_SEED)
    the_runs = perform_runs()
    display_runs(the_runs)
