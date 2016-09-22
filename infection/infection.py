from .user import *

class InfectionSimulation(): 

    def __init__(self, n): 
        self.users, self.teacherIds, self.selfLearnerIds = generate_users(n)
        

    def total_infection(self, userId): 
        """Infect user and user's connections

        Parameters
        ----------
        userId : str, the id of the user

        Returns
        -------
        infectedSet: set, a set of all infected userIds
        """
        infectedSet = set()

        if not self.users.get(userId) or self.users[userId].infected == True: 
            return infectedSet

        self.users[userId].infected = True # change infection 
        self.users[userId].siteVersion = 'B' # change site-version 
        infectedSet.add(userId)

        for id in self.users[userId].connections: 
            infectedSet = infectedSet | self.total_infection(id)

        return infectedSet

    def limited_infection(self, userId, n, strict): 
        """Infect user and user's connections limit by less than equal to `n`. If `strict` is True limit by exactly `n`. 

        Parameters
        ----------
        userId : str, the id of the user
        n      : int, max number of users that can be infected. 
        strict : bool, if True then algorithm attempts to infect exactly `n` users. 

        Return
        ------
        result : bool, returns whether or not infecting userId will result in < n infections

        """
        # look at the teachers that we can infect based on a studentId/teacherId
        # 
        frontier = [] # just a list of connected people 



    def limited_infection_validation(self): 
        pass




if __name__ == '__main__': 
    infectionSimulation = InfectionSimulation(20)
    infectionSet = infectionSimulation.total_infection(infectionSimulation.teacherIds[0])
    print(infectionSet)







