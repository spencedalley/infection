from nose.tools import * 

from infection.infection import InfectionSimulation 
from infection.user import User
from infection.utils import init_users, generate_users

SITE_VERSION = 'B'

def setup():
	print('Setup')

def teardown():
    print('Teardown')
    
@with_setup(setup, teardown)
def test_generate_users():
    users, teacherIds, selfLearnerIds = generate_users(20)

    assert_true(len(teacherIds) == 2)
    assert_true(len(users) == 20, "\nActual: {}, Expected: {}".format(len(users), 20))
    assert_true(len(users)-len(teacherIds)-len(selfLearnerIds) == 15)
    assert_true(len(selfLearnerIds) == 3, "\nActual: {}, Expected: {}".format(len(selfLearnerIds), 3))

def test_infect(): 
    for i in range(6): 
        users, teacherIds, selfLearnerIds = init_users()
        infectionSimulation = InfectionSimulation(users, teacherIds, selfLearnerIds, SITE_VERSION) 
        infectionSet = infectionSimulation.infect(infectionSimulation.teacherIds[i])

        if i == 0 or i == 1 or i == 2: 
            expected = 18 
        elif i == 3 or i == 4: 
            expected = 11 
        elif i == 5: 
            expected = 2

        assert_true(len(infectionSet) == expected, 'Expected: {}, Actual: {}'.format(expected, len(infectionSet)))

def test_total_infection(): 
    for i in range(6): 
        users, teacherIds, selfLearnerIds = init_users()
        infectionSimulation = InfectionSimulation(users, teacherIds, selfLearnerIds, SITE_VERSION) 
        result = infectionSimulation.total_infection(infectionSimulation.teacherIds[i])

        if i == 0 or i == 1 or i == 2: 
            expected = 18 
        elif i == 3 or i == 4: 
            expected = 11 
        elif i == 5: 
            expected = 2

        assert_true(result == expected, 'Expected: {}, Actual: {}'.format(expected, len(infectionSimulation.globalInfectionSet)))

def test_limited_infection(): 
    # Non strict testing (i.e. infect as close to `target` number as possible)
    target = [-1, 1, 10, 17, 29, 31, 33, 40]
    expected = [[],
                [['32']], 
                [['32'], ['33'], ['5']], 
                [['32'], ['33'], ['5'], ['3', '4']], 
                [['3', '4'], ['0', '1', '2']], 
                [['5'], ['3', '4'], ['0', '1', '2']], 
                [['32'], ['33'], ['5'], ['3', '4'], ['0', '1', '2']], 
                [['32'], ['33'], ['5'], ['3', '4'], ['0', '1', '2']]]

    for i in range(len(target)): 
        users, teacherIds, selfLearnerIds = init_users()
        infectionSimulation = InfectionSimulation(users, teacherIds, selfLearnerIds, SITE_VERSION) 
        result = infectionSimulation.limited_infection(target[i], False)
        assert_true(result == expected[i], '\nActual: {}\nExpected: {}'.format(result, expected[i]))

    # strict testing (i.e. limit to exactly `n` infections)
    target = [-1, 1, 10, 17, 29, 31, 33, 40]
    expected = [[],
                [['32']], 
                [], 
                [], 
                [['3', '4'], ['0', '1', '2']], 
                [['5'], ['3', '4'], ['0', '1', '2']], 
                [['32'], ['33'], ['5'], ['3', '4'], ['0', '1', '2']], 
                []]

    for i in range(len(target)): 
        users, teacherIds, selfLearnerIds = init_users()
        infectionSimulation = InfectionSimulation(users, teacherIds, selfLearnerIds, SITE_VERSION) 
        result = infectionSimulation.limited_infection(target[i], True)
        assert_true(result == expected[i], '\nActual: {}\nExpected: {}'.format(result, expected[i]))

def test_subset_sum(): 
    users, teacherIds, selfLearnerIds = init_users()
    infectionSimulation = InfectionSimulation(users, teacherIds, selfLearnerIds, SITE_VERSION) 

    testArr = [3, 4, 1, 2]
    assert_true(infectionSimulation.subset_sum(testArr, 7, False) == [3, 4])
    assert_true(infectionSimulation.subset_sum(testArr, 8, False) == [1, 3, 4])
    assert_true(infectionSimulation.subset_sum(testArr, 10, False) == [1, 2, 3, 4])

    testArr = [3, 4]
    assert_true(infectionSimulation.subset_sum(testArr, 1, False) == [])
    assert_true(infectionSimulation.subset_sum(testArr, 7, True) == [3, 4])
    assert_true(infectionSimulation.subset_sum(testArr, 5, True) == [])

    testArr = [10, 3, 2]
    assert_true(infectionSimulation.subset_sum(testArr, 6, False) == [2, 3])

    testArr = [10, 3, 1, 4, 21]
    assert_true(infectionSimulation.subset_sum(testArr, 9, False) == [1, 3, 4])









