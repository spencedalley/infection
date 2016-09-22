from nose.tools import * 

from infection import infection, user

# users, teacherIds, selfLearnerIds = None

def setup():
	pass

def teardown():
	pass

@with_setup(setup, teardown)
def test_generate_users():
    users, teacherIds, selfLearnerIds = user.generate_users(20)

    assert_true(len(teacherIds) == 2)
    assert_true(len(users) == 20, "\nActual: {}, Expected: {}".format(len(users), 20))
    assert_true(len(users)-len(teacherIds)-len(selfLearnerIds) == 15)
    assert_true(len(selfLearnerIds) == 3, "\nActual: {}, Expected: {}".format(len(selfLearnerIds), 3))

@with_setup(setup, teardown)
def test_infection(): 
    for i in [30, 50, 100]: 
        infectionSimulation = infection.InfectionSimulation(i)
        infectionSet = infectionSimulation.total_infection(infectionSimulation.teacherIds[0])

        for id in infectionSet: 
            assert_true(infectionSimulation.users[id].siteVersion == 'B')
            assert_true(infectionSimulation.users[id].infected == True)

        for id in infectionSimulation.selfLearnerIds: 
            assert_true(infectionSimulation.users[id].siteVersion == 'A')
            assert_true(infectionSimulation.users[id].infected == False)

        assert_true(len(infectionSet) == 20, 'Should be 20 infected individuals')

    for i in [50, 100, 1000]: 
        infectionSimulation = infection.InfectionSimulation(i)
        infectionSet = infectionSimulation.total_infection(infectionSimulation.teacherIds[-1])

        for id in infectionSet: 
            assert_true(infectionSimulation.users[id].siteVersion == 'B')
            assert_true(infectionSimulation.users[id].infected == True)

        for id in infectionSimulation.selfLearnerIds: 
            assert_true(infectionSimulation.users[id].siteVersion == 'A')
            assert_true(infectionSimulation.users[id].infected == False)

        assert_true(len(infectionSet) == 7, 'Should be 7 infected individuals')

        infectionSet = infectionSimulation.total_infection(infectionSimulation.teacherIds[-2])

        for id in infectionSet: 
            assert_true(infectionSimulation.users[id].siteVersion == 'B')
            assert_true(infectionSimulation.users[id].infected == True)

        for id in infectionSimulation.selfLearnerIds: 
            assert_true(infectionSimulation.users[id].siteVersion == 'A')
            assert_true(infectionSimulation.users[id].infected == False)

        assert_true(len(infectionSet) == 10, 'Should be 10 infected individuals')










