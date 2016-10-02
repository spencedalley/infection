## Infection Project
This project simulates an infections spread throughout an interconnected network. There are two methods of the simulation that are publicly availiable: `total_infection` and `limited_infection`. `total_infection` maps an infections complete infection course throughout a network. `limited_infection` attempts to infect a target number of individuals. 

### Setup: 
Running the infection simulation requires the following version of python: 

*   python 3.4 or above

Dependency requirements for this project can be found in the requirements.txt file. Install the requirements with the following command after cd to the module's root: 
```
$ sudo pip install -r requirements.txt 
```

The project setup is now complete. 

### Running Tests: 
All the tests for this module are located in the `tests/infection_test.py` file. 

To run the tests, open up a terminal, cd to the root of the project, and type `nosetests` to run the tests. You should get an output like the text below: 

```
$ nosetests

.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```

All tests should pass. 

## Implementation Notes: 
[Add notes]


