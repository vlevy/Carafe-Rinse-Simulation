
from datetime import datetime, timedelta
import unittest
from Carafe import Carafe, FILL_ML_PER_SECOND, DREGS_ML_EXTRA, DREGS_ML_FAST, SECONDS_TO_SHAKE, \
    SECONDS_TO_DRIP_EXTRA, SECONDS_TO_DRIP_FAST, SECONDS_TO_TIP, POUR_ML_PER_SECOND


class Carafe_test(unittest.TestCase):

    def test_init(self):
        """Test the Carafe constructor
        :return: None
        """
        carafe = Carafe(100.0)
        self.assertAlmostEqual(carafe.contents_ml, 100.0, places=9)
        self.assertAlmostEqual(carafe.concentration, 1.0, places=9)
        self.assertAlmostEqual(carafe.seconds_elapsed, 0.0, places=9)
        self.assertFalse(carafe.events)

    def test_add_time(self):
        """Test the Carafe add_time method
        :return: None
        """
        carafe = Carafe(100.0)
        event = carafe.add_time(1.0, 'Adding 1 second')
        self.assertEqual(len(carafe.events), 1)
        self.assertAlmostEqual(carafe.seconds_elapsed, 1.0, places=9)
        self.assertAlmostEqual(event.seconds, 1.0, places=9)
        self.assertEqual(event.comment, 'Adding 1 second for 1.0 seconds')

        event = carafe.add_time(2.0, 'Adding 2 seconds')
        self.assertEqual(len(carafe.events), 2)
        self.assertAlmostEqual(carafe.seconds_elapsed, 3.0, places=9)
        self.assertAlmostEqual(event.seconds, 2.0, places=9)
        self.assertEqual(event.comment, 'Adding 2 seconds for 2.0 seconds')

    def test_fill(self):
        """Test the Carafe fill method
        :return: None
        """
        carafe = Carafe(100.0)
        carafe.fill(300.0)
        self.assertAlmostEqual(carafe.concentration, 0.25, places=9)
        self.assertAlmostEqual(carafe.contents_ml, 400.0, places=9)
        self.assertAlmostEqual(carafe.seconds_elapsed, 300 / FILL_ML_PER_SECOND, places=9)

    def test_pour_out(self):
        """Test the Carafe pour_out method
        :return: None
        """
        carafe = Carafe(100.0)
        carafe.pour_out(False)
        self.assertAlmostEqual(carafe.contents_ml, DREGS_ML_FAST, places=9)
        self.assertAlmostEqual(carafe.seconds_elapsed,
                SECONDS_TO_SHAKE + SECONDS_TO_TIP + 100.0 / POUR_ML_PER_SECOND + SECONDS_TO_DRIP_FAST,
                places=9)


        carafe = Carafe(100.0)
        carafe.pour_out(True)
        self.assertAlmostEqual(carafe.contents_ml, DREGS_ML_EXTRA, places=9)
        self.assertAlmostEqual(carafe.seconds_elapsed,
                SECONDS_TO_SHAKE + SECONDS_TO_TIP + 100.0 / POUR_ML_PER_SECOND + SECONDS_TO_DRIP_FAST + SECONDS_TO_DRIP_EXTRA,
                places=9)

    def test_play_back_events(self):
        """Test the Carafe play_back_events method
        :return: None
        """
        carafe = Carafe(100.0)
        carafe.add_time(0.1, 'Event 1')
        carafe.add_time(0.2, 'Event 2')
        carafe.add_time(0.3, 'Event 3')

        # Realtime check
        start_time = datetime.now()
        carafe.play_back_events(True)
        end_time = datetime.now()
        playback_time = end_time - start_time
        self.assertAlmostEqual((playback_time - timedelta(seconds=0.6)).total_seconds(), 0.0, places=2)

        # Non-realtime check
        start_time = datetime.now()
        carafe.play_back_events(False)
        end_time = datetime.now()
        playback_time = end_time - start_time
        self.assertAlmostEqual((playback_time - timedelta(seconds=0.0)).total_seconds(), 0.0, places=2)

