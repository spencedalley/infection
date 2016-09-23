from nose.tools import * 

from infection.infection import InfectionSimulation 
from infection.user import User, generate_users

def init_users(): 
    USERS = {
        # Teachers
        '0': User('0', 'teacher', False, 'A', [str(i) for i in range(6, 11)]+['11']),
        '1': User('1', 'teacher', False, 'A', [str(i) for i in range(11, 16)]+['2', '16']),
        '2': User('2', 'teacher', False, 'A', [str(i) for i in range(16, 21)]+['15']),
        '3': User('3', 'teacher', False, 'A', [str(i) for i in range(21, 25)]+['26']),
        '4': User('4', 'teacher', False, 'A', [str(i) for i in range(26, 31)]),
        '5': User('5', 'teacher', False, 'A', ['31']), # no students

        # Students with teachers
        '6': User('6', 'student', False, 'A', ['0']),
        '7': User('7', 'student', False, 'A', ['0']),
        '8': User('8', 'student', False, 'A', ['0']),
        '9': User('9', 'student', False, 'A', ['0']),
        '10': User('10', 'student', False, 'A', ['0']),
        '11': User('11', 'student', False, 'A', ['1', '0']),
        '12': User('12', 'student', False, 'A', ['1']),
        '13': User('13', 'student', False, 'A', ['1']),
        '14': User('14', 'student', False, 'A', ['1']),
        '15': User('15', 'student', False, 'A', ['1', '2']),
        '16': User('16', 'student', False, 'A', ['2']),
        '17': User('17', 'student', False, 'A', ['2']),
        '18': User('18', 'student', False, 'A', ['2']),
        '19': User('19', 'student', False, 'A', ['2']),
        '20': User('20', 'student', False, 'A', ['2']),
        '21': User('21', 'student', False, 'A', ['3']),
        '22': User('22', 'student', False, 'A', ['3']),
        '23': User('23', 'student', False, 'A', ['3']),
        '24': User('24', 'student', False, 'A', ['3']),
        '25': User('25', 'student', False, 'A', ['3']),
        '26': User('26', 'student', False, 'A', ['4', '3']),
        '27': User('27', 'student', False, 'A', ['4']),
        '28': User('28', 'student', False, 'A', ['4']),
        '29': User('29', 'student', False, 'A', ['4']),
        '30': User('30', 'student', False, 'A', ['4']),
        '31': User('31', 'student', False, 'A', ['5']),

        # Self Learners
        '32': User('32', 'student', False, 'A', []),
        '33': User('33', 'student', False, 'A', []),
    }

    TEACHER_IDS = ['0', '1', '2', '3', '4', '5']
    SELF_LEARNER_IDS = [str(i) for i in range(32, 34)]

    return (USERS, TEACHER_IDS, SELF_LEARNER_IDS)

def setup():
	USERS, TEACHER_IDS, SELF_LEARNER_IDS = init_users()

def teardown():
    pass
	# del USERS, TEACHER_IDS, SELF_LEARNER_IDS
    
@with_setup(setup, teardown)
def test_generate_users():
    users, teacherIds, selfLearnerIds = generate_users(20)

    assert_true(len(teacherIds) == 2)
    assert_true(len(users) == 20, "\nActual: {}, Expected: {}".format(len(users), 20))
    assert_true(len(users)-len(teacherIds)-len(selfLearnerIds) == 15)
    assert_true(len(selfLearnerIds) == 3, "\nActual: {}, Expected: {}".format(len(selfLearnerIds), 3))

@with_setup(setup, teardown)
def test_infect(): 
    for i in range(6): 
        USERS, TEACHER_IDS, SELF_LEARNER_IDS = init_users()
        infectionSimulation = InfectionSimulation(USERS, TEACHER_IDS, SELF_LEARNER_IDS) 
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
        USERS, TEACHER_IDS, SELF_LEARNER_IDS = init_users()
        infectionSimulation = InfectionSimulation(USERS, TEACHER_IDS, SELF_LEARNER_IDS) 
        infectionSimulation.total_infection(infectionSimulation.teacherIds[i])

        if i == 0 or i == 1 or i == 2: 
            expected = 18 
        elif i == 3 or i == 4: 
            expected = 11 
        elif i == 5: 
            expected = 2

        assert_true(len(infectionSimulation.globalInfectionSet) == expected, 'Expected: {}, Actual: {}'.format(expected, len(infectionSimulation.globalInfectionSet)))

def test_limited_infection(): 
    nSet = [-1, 1, 10, 17, 29, 31, 33, 40]
    expected = [[],
                [['32']], 
                [['32'], ['33'], ['5']], 
                [['32'], ['33'], ['5'], ['3', '4']], 
                [['3', '4'], ['0', '1', '2']], 
                [['5'], ['3', '4'], ['0', '1', '2']], 
                [['32'], ['33'], ['5'], ['3', '4'], ['0', '1', '2']], 
                [['32'], ['33'], ['5'], ['3', '4'], ['0', '1', '2']]]

    for i in range(len(nSet)): 
        USERS, TEACHER_IDS, SELF_LEARNER_IDS = init_users()
        infectionSimulation = InfectionSimulation(USERS, TEACHER_IDS, SELF_LEARNER_IDS) 
        result = infectionSimulation.limited_infection(nSet[i], False)
        assert_true(result == expected[i], '\nActual: {}\nExpected: {}'.format(result, expected[i]))

    # strict testing (i.e. limit to exactly `n` infections)
    nSet = [-1, 1, 10, 17, 29, 31, 33, 40]
    expected = [[],
                [['32']], 
                [], 
                [], 
                [['3', '4'], ['0', '1', '2']], 
                [['5'], ['3', '4'], ['0', '1', '2']], 
                [['32'], ['33'], ['5'], ['3', '4'], ['0', '1', '2']], 
                []]

    for i in range(len(nSet)): 
        USERS, TEACHER_IDS, SELF_LEARNER_IDS = init_users()
        infectionSimulation = InfectionSimulation(USERS, TEACHER_IDS, SELF_LEARNER_IDS) 
        result = infectionSimulation.limited_infection(nSet[i], True)
        assert_true(result == expected[i], '\nActual: {}\nExpected: {}'.format(result, expected[i]))

def test_subset_sum(): 
    USERS, TEACHER_IDS, SELF_LEARNER_IDS = init_users()
    infectionSimulation = InfectionSimulation(USERS, TEACHER_IDS, SELF_LEARNER_IDS) 

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









