# Carafe Rinse Simulation and Optimization

This project is a simulation of rinsing out a coffee carafe. The simulation repeats the following process:

1. adds a random amount of water to the carafe
2. pours it out
3. repeats until the carafe is clean, i.e., the concentration of coffee is low enough to be considered clean. 

The simulation records timing for each run and determines which steps lead to the fastest (and slowest) process of rinsing the carafe until it is clean.

## Getting Started

Copy the files to a folder on your hard drive and run pour.py.

### Prerequisites

python 3.6

### Installing

1. Copy the files to a folder on your hard drive
2. Edit pour.py and set program parameters to drive the simulation
3. Edit carafe.py and set the carafe parameters to match your carafe and sink

Run 'python pour.py'
```
Simulation 100,000 (20.00%) of 500,000 done in 0:00:05.087291
Fastest run took 4 cycles in 25.182078348680 seconds: CleaningRun(run_num=95130, cycle_list=[CleaningCycle(initial_fill=168.31206062687377, extra_drip=False), CleaningCycle(initial_fill=296.0652701149384, extra_drip=False), CleaningCycle(initial_fill=109.31703033663531, extra_drip=False), CleaningCycle(initial_fill=194.7012352594819, extra_drip=False)], carafe=<Carafe.Carafe object at 0x000000001B00CC88>)
Slowest run took 3 cycles in 104.135365472003 seconds: CleaningRun(run_num=50166, cycle_list=[CleaningCycle(initial_fill=1866.0032125623218, extra_drip=True), CleaningCycle(initial_fill=1971.7651999383725, extra_drip=True), CleaningCycle(initial_fill=1991.0699347986535, extra_drip=True)], carafe=<Carafe.Carafe object at 0x000000000F889668>)
400,000 remaining, estimated remaining time 0:00:20.400000, estimated completion 2018-06-03 18:04:30.975242
Simulation 200,000 (40.00%) of 500,000 done in 0:00:10.247587
Fastest run took 4 cycles in 23.740211648809 seconds: CleaningRun(run_num=148125, cycle_list=[CleaningCycle(initial_fill=143.84040100645245, extra_drip=False), CleaningCycle(initial_fill=177.7764612802799, extra_drip=False), CleaningCycle(initial_fill=86.96371115227674, extra_drip=False), CleaningCycle(initial_fill=252.05231226073454, extra_drip=False)], carafe=<Carafe.Carafe object at 0x000000000E8656D8>)
Slowest run took 4 cycles in 105.467651999656 seconds: CleaningRun(run_num=195192, cycle_list=[CleaningCycle(initial_fill=1855.8215313497803, extra_drip=True), CleaningCycle(initial_fill=1580.446491006191, extra_drip=True), CleaningCycle(initial_fill=3.1786394146595676, extra_drip=True), CleaningCycle(initial_fill=1837.9867163460542, extra_drip=True)], carafe=<Carafe.Carafe object at 0x000000001AEF4908>)
300,000 remaining, estimated remaining time 0:00:15.300000, estimated completion 2018-06-03 18:04:31.035538
Simulation 300,000 (60.00%) of 500,000 done in 0:00:15.388881
Fastest run took 4 cycles in 23.740211648809 seconds: CleaningRun(run_num=148125, cycle_list=[CleaningCycle(initial_fill=143.84040100645245, extra_drip=False), CleaningCycle(initial_fill=177.7764612802799, extra_drip=False), CleaningCycle(initial_fill=86.96371115227674, extra_drip=False), CleaningCycle(initial_fill=252.05231226073454, extra_drip=False)], carafe=<Carafe.Carafe object at 0x000000000E8656D8>)
Slowest run took 4 cycles in 105.467651999656 seconds: CleaningRun(run_num=195192, cycle_list=[CleaningCycle(initial_fill=1855.8215313497803, extra_drip=True), CleaningCycle(initial_fill=1580.446491006191, extra_drip=True), CleaningCycle(initial_fill=3.1786394146595676, extra_drip=True), CleaningCycle(initial_fill=1837.9867163460542, extra_drip=True)], carafe=<Carafe.Carafe object at 0x000000001AEF4908>)
200,000 remaining, estimated remaining time 0:00:10.200000, estimated completion 2018-06-03 18:04:31.076832
Simulation 400,000 (80.00%) of 500,000 done in 0:00:20.662182
Fastest run took 4 cycles in 23.740211648809 seconds: CleaningRun(run_num=148125, cycle_list=[CleaningCycle(initial_fill=143.84040100645245, extra_drip=False), CleaningCycle(initial_fill=177.7764612802799, extra_drip=False), CleaningCycle(initial_fill=86.96371115227674, extra_drip=False), CleaningCycle(initial_fill=252.05231226073454, extra_drip=False)], carafe=<Carafe.Carafe object at 0x000000000E8656D8>)
Slowest run took 4 cycles in 105.467651999656 seconds: CleaningRun(run_num=195192, cycle_list=[CleaningCycle(initial_fill=1855.8215313497803, extra_drip=True), CleaningCycle(initial_fill=1580.446491006191, extra_drip=True), CleaningCycle(initial_fill=3.1786394146595676, extra_drip=True), CleaningCycle(initial_fill=1837.9867163460542, extra_drip=True)], carafe=<Carafe.Carafe object at 0x000000001AEF4908>)
100,000 remaining, estimated remaining time 0:00:05.200000, estimated completion 2018-06-03 18:04:31.350133
Simulation 500,000 (100.00%) of 500,000 done in 0:00:25.841478
Fastest run took 4 cycles in 23.740211648809 seconds: CleaningRun(run_num=148125, cycle_list=[CleaningCycle(initial_fill=143.84040100645245, extra_drip=False), CleaningCycle(initial_fill=177.7764612802799, extra_drip=False), CleaningCycle(initial_fill=86.96371115227674, extra_drip=False), CleaningCycle(initial_fill=252.05231226073454, extra_drip=False)], carafe=<Carafe.Carafe object at 0x000000000E8656D8>)
Slowest run took 4 cycles in 105.765977343487 seconds: CleaningRun(run_num=481493, cycle_list=[CleaningCycle(initial_fill=5.723306984657395, extra_drip=True), CleaningCycle(initial_fill=1961.8100160094898, extra_drip=False), CleaningCycle(initial_fill=1950.2847114389, extra_drip=True), CleaningCycle(initial_fill=1754.4717951235405, extra_drip=True)], carafe=<Carafe.Carafe object at 0x00000000175306D8>)
0 remaining, estimated remaining time 0:00:00, estimated completion 2018-06-03 18:04:31.329429
1 Fastest run took 4 cycles in 23.740211648809 seconds: [CleaningCycle(initial_fill=143.84040100645245, extra_drip=False), CleaningCycle(initial_fill=177.7764612802799, extra_drip=False), CleaningCycle(initial_fill=86.96371115227674, extra_drip=False), CleaningCycle(initial_fill=252.05231226073454, extra_drip=False)]
2 Fastest run took 4 cycles in 24.751791968556 seconds: [CleaningCycle(initial_fill=228.17368256547232, extra_drip=False), CleaningCycle(initial_fill=292.55180931245394, extra_drip=False), CleaningCycle(initial_fill=59.761839171850184, extra_drip=False), CleaningCycle(initial_fill=155.7493793960163, extra_drip=False)]
3 Fastest run took 4 cycles in 24.885074889521 seconds: [CleaningCycle(initial_fill=50.86913022461115, extra_drip=False), CleaningCycle(initial_fill=244.59262871784216, extra_drip=False), CleaningCycle(initial_fill=288.3215524388989, extra_drip=False), CleaningCycle(initial_fill=162.41474212495265, extra_drip=False)]
4 Fastest run took 4 cycles in 25.131931914632 seconds: [CleaningCycle(initial_fill=107.65536749462301, extra_drip=False), CleaningCycle(initial_fill=243.26560990320468, extra_drip=False), CleaningCycle(initial_fill=317.73006257519444, extra_drip=False), CleaningCycle(initial_fill=95.99669557973468, extra_drip=False)]
5 Fastest run took 4 cycles in 25.157656329006 seconds: [CleaningCycle(initial_fill=131.5607496949378, extra_drip=False), CleaningCycle(initial_fill=190.83140443377067, extra_drip=False), CleaningCycle(initial_fill=195.19795508113714, extra_drip=False), CleaningCycle(initial_fill=248.98022613859894, extra_drip=False)]
6 Fastest run took 4 cycles in 25.182078348680 seconds: [CleaningCycle(initial_fill=168.31206062687377, extra_drip=False), CleaningCycle(initial_fill=296.0652701149384, extra_drip=False), CleaningCycle(initial_fill=109.31703033663531, extra_drip=False), CleaningCycle(initial_fill=194.7012352594819, extra_drip=False)]
7 Fastest run took 4 cycles in 25.553944271542 seconds: [CleaningCycle(initial_fill=205.0240913436008, extra_drip=False), CleaningCycle(initial_fill=165.01100339012154, extra_drip=False), CleaningCycle(initial_fill=188.70462193366944, extra_drip=False), CleaningCycle(initial_fill=237.44851809204337, extra_drip=False)]
8 Fastest run took 4 cycles in 25.888326650094 seconds: [CleaningCycle(initial_fill=226.58068039200097, extra_drip=False), CleaningCycle(initial_fill=114.71400979124336, extra_drip=False), CleaningCycle(initial_fill=220.98370998656836, extra_drip=False), CleaningCycle(initial_fill=258.90101547040103, extra_drip=False)]
9 Fastest run took 4 cycles in 26.073341806793 seconds: [CleaningCycle(initial_fill=116.21808651465027, extra_drip=False), CleaningCycle(initial_fill=384.13629220418443, extra_drip=False), CleaningCycle(initial_fill=170.97229076099785, extra_drip=False), CleaningCycle(initial_fill=163.68047017735887, extra_drip=False)]
10 Fastest run took 4 cycles in 26.121207318746 seconds: [CleaningCycle(initial_fill=64.35135808169635, extra_drip=False), CleaningCycle(initial_fill=130.252524475164, extra_drip=False), CleaningCycle(initial_fill=381.3370430784639, extra_drip=False), CleaningCycle(initial_fill=262.64360249650645, extra_drip=False)]

1 Slowest run took 4 cycles in 105.765977343487 seconds: [CleaningCycle(initial_fill=5.723306984657395, extra_drip=True), CleaningCycle(initial_fill=1961.8100160094898, extra_drip=False), CleaningCycle(initial_fill=1950.2847114389, extra_drip=True), CleaningCycle(initial_fill=1754.4717951235405, extra_drip=True)]
2 Slowest run took 4 cycles in 105.467651999656 seconds: [CleaningCycle(initial_fill=1855.8215313497803, extra_drip=True), CleaningCycle(initial_fill=1580.446491006191, extra_drip=True), CleaningCycle(initial_fill=3.1786394146595676, extra_drip=True), CleaningCycle(initial_fill=1837.9867163460542, extra_drip=True)]
3 Slowest run took 3 cycles in 105.238346882487 seconds: [CleaningCycle(initial_fill=1995.4450009259174, extra_drip=True), CleaningCycle(initial_fill=1958.8001615493158, extra_drip=True), CleaningCycle(initial_fill=1957.0281745412158, extra_drip=True)]
4 Slowest run took 3 cycles in 105.025048689881 seconds: [CleaningCycle(initial_fill=1912.9874908137326, extra_drip=True), CleaningCycle(initial_fill=1993.2032814318886, extra_drip=True), CleaningCycle(initial_fill=1989.1410138552462, extra_drip=True)]
5 Slowest run took 4 cycles in 105.002358657874 seconds: [CleaningCycle(initial_fill=1.8220560566448718, extra_drip=True), CleaningCycle(initial_fill=1767.0503058715376, extra_drip=False), CleaningCycle(initial_fill=1967.9074892362453, extra_drip=True), CleaningCycle(initial_fill=1878.4383923273722, extra_drip=True)]
6 Slowest run took 3 cycles in 104.674111214002 seconds: [CleaningCycle(initial_fill=1986.292188530761, extra_drip=True), CleaningCycle(initial_fill=1901.7866522694387, extra_drip=True), CleaningCycle(initial_fill=1981.024464076533, extra_drip=True)]
7 Slowest run took 3 cycles in 104.670774112206 seconds: [CleaningCycle(initial_fill=1990.3202085769465, extra_drip=True), CleaningCycle(initial_fill=1931.1338657615797, extra_drip=True), CleaningCycle(initial_fill=1947.3998211197297, extra_drip=True)]
8 Slowest run took 3 cycles in 104.627377897085 seconds: [CleaningCycle(initial_fill=1884.5211095836794, extra_drip=True), CleaningCycle(initial_fill=1998.099416215628, extra_drip=True), CleaningCycle(initial_fill=1982.9900089700716, extra_drip=True)]
9 Slowest run took 3 cycles in 104.599788348097 seconds: [CleaningCycle(initial_fill=1971.8244248558397, extra_drip=True), CleaningCycle(initial_fill=1987.9865470198433, extra_drip=True), CleaningCycle(initial_fill=1903.7375660499843, extra_drip=True)]
10 Slowest run took 4 cycles in 104.338116546110 seconds: [CleaningCycle(initial_fill=4.980059978521911, extra_drip=False), CleaningCycle(initial_fill=1900.104872355041, extra_drip=True), CleaningCycle(initial_fill=1912.9351640338502, extra_drip=True), CleaningCycle(initial_fill=1747.5538003272686, extra_drip=True)]

Playing back fastest run
Cycle 1
Filling 143.84 ml for 1.20 seconds
Shaking for 2.00 seconds
Tipping for 0.50 seconds
Pouring 143.84 ml for 0.75 seconds
Dripping fast for 1.20 seconds
Cycle 2
Filling 177.78 ml for 1.48 seconds
Shaking for 2.00 seconds
Tipping for 0.50 seconds
Pouring 177.78 ml for 0.92 seconds
Dripping fast for 1.20 seconds
Cycle 3
Filling 86.96 ml for 0.72 seconds
Shaking for 2.00 seconds
Tipping for 0.50 seconds
Pouring 86.96 ml for 0.46 seconds
Dripping fast for 1.20 seconds
Cycle 4
Filling 252.05 ml for 2.10 seconds
Shaking for 2.00 seconds
Tipping for 0.50 seconds
Pouring 252.05 ml for 1.30 seconds
Dripping fast for 1.20 seconds
Total simulated time: 23.74 seconds
```


## Running the tests

Currently unit tests are supported for the Carafe class.

run 'python Carafe_tests.py'

## Deployment

Copy Carafe.py and pour.py to the same directory.

## Built With

* [PyCharm Community Edition Version 2.7.34 ](https://www.jetbrains.com/pycharm/)

## Authors

* **Vic Levy** - *Initial work* - [vlevy](https://github.com/vlevy)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspiration: I frequently make coffee in a Cuisinart machine, and I wanted to create a simulation to determine how to most 
efficiently rinse out the carafe.

