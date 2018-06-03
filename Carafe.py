from time import sleep
from collections import namedtuple

CleaningEvent = namedtuple('CleaningEvent',   'seconds  comment')

# Constants
SECONDS_TO_TIP = 0.5           # Before pouring can occur, need to tip carafe over
SECONDS_TO_SHAKE = 2.0         # Number of seconds of shaking to mix contents after adding water
SECONDS_TO_DRIP_FAST = 1.2     # Transition time from full pour to fast drip
SECONDS_TO_DRIP_EXTRA = 5      # At pour time, extra time to wait from when dripping starts to when drops occur
                               # at 1-second intervals
POUR_ML_PER_SECOND = 198.15    # Depends on the model of carafe
FILL_ML_PER_SECOND = 120.0     # Depends on the sink
DREGS_ML_FAST = 5.0            # Leftover volume in carafe after pouring stops and dripping starts
DREGS_ML_EXTRA = 2.0           # Leftover volume in carafe after waiting for drops at 1-second intervals


class Carafe(object):
    """Class to encapulate a coffee carafe as used to fill and pour out during rinsing.
    """
    def __init__(self, contents_ml):
        """Constructor for the Carafe object
        :param contents_ml: Initial volume of pure coffee
        """
        self.concentration = 1.0  # Starting with pure coffee and no water
        self.contents_ml = contents_ml
        self.seconds_elapsed = 0.0
        self.events = list()

    def add_time(self, seconds, comment):
        """Add elapsed time to a carafe object, with a comment
        :param seconds: Number of added seconds to add to elapsed time. Can be None to add only a comment.
        :param comment: Comment to attach to the elapsed time
        :return: A CleaningEvent object with the results of the added elapsed time
        """
        if seconds is not None:
            event = CleaningEvent(seconds, f'{comment} for {seconds:.2f} seconds')
            self.seconds_elapsed += seconds
        else:
            event = CleaningEvent(seconds, comment)

        self.events.append(event)

        return event

    def play_back_events(self, realtime):
        """Print a play-by-play of the events in a carafe. Optionally waits for the elapsed time for each event.
        :param realtime: Whether to wait for the duration of each event
        :return: None
        """
        for event in self.events:
            print(event.comment)
            if realtime and event.seconds:
                sleep(event.seconds)
        print(f'Total simulated time: {self.seconds_elapsed:.2f} seconds')

    def pour_out(self, extra_drip):
        """Simulate pouring out the carafe.
        :param extra_drip: Whether to wait the extra time to drip our a few more ml of contents
        :return: None
        """
        self.add_time(SECONDS_TO_SHAKE, 'Shaking')
        self.add_time(SECONDS_TO_TIP, 'Tipping')
        seconds_to_pour = self.contents_ml / POUR_ML_PER_SECOND
        contents_poured = self.contents_ml - (DREGS_ML_EXTRA if extra_drip else DREGS_ML_FAST)
        self.add_time(seconds_to_pour, f'Pouring {contents_poured:.2f} ml')
        self.add_time(SECONDS_TO_DRIP_FAST, 'Dripping fast')
        if extra_drip:
            # If we want to wait a few more seconds, we can lower the remaining volume by a few ml by waiting until
            # the carafe is dripping only once per second
            self.add_time(SECONDS_TO_DRIP_EXTRA, 'Dripping extra')
            self.contents_ml = DREGS_ML_EXTRA
        else:
            self.contents_ml = DREGS_ML_FAST

    def fill(self, fill_amt_ml):
        """Simulate adding water to the carafe
        :param fill_amt_ml: Volume of water to add
        :return: None
        """
        self.concentration = (self.concentration * self.contents_ml) / (self.contents_ml + fill_amt_ml)
        self.contents_ml += fill_amt_ml
        self.add_time(fill_amt_ml / FILL_ML_PER_SECOND, f'Filling {fill_amt_ml:.2f} ml')
