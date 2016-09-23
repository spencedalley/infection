from itertools import chain, combinations

from .user import *

class InfectionSimulation(): 

    def __init__(self, users, teacherIds, selfLearnerIds): 
        # self.users, self.teacherIds, self.selfLearnerIds = generate_users(n)
        self.users = users.copy()
        self.teacherIds = list(teacherIds) 
        self.selfLearnerIds = list(selfLearnerIds)
        self.globalInfectionSet = set()
        self.teacherIdsExplored = list()
        self.position = 0

    def infect(self, userId): 
        """Infect user and user's connections

        Parameters
        ----------
        userId : str, the id of the user
        n      : int, max number of users that can be infected. 
        strict : bool, if True then algorithm attempts to infect exactly `n` users. 

        Returns
        -------
        infectedSet: 
        """
        # This is the modified infected user set...
        infectedSet = set()

        if not self.users.get(userId) or self.users[userId].infected == True: 
            return infectedSet
        
        self.users[userId].infected = True # change infection 
        self.users[userId].siteVersion = 'B' # change site-version 
        if self.users[userId].role == 'teacher': 
            self.teacherIdsExplored.append(userId)

        infectedSet.add(userId)

        for id in self.users[userId].connections: 
            infectedSet = infectedSet | self.infect(id)

        return infectedSet

    def total_infection(self, userId): 
        self.globalInfectionSet = self.infect(userId)
        # print(len(self.globalInfectionSet))

    def limited_infection(self, target, strict): 
        infectionCounts = []
        frontier = {}
        position = 0

        for id in self.teacherIds: 
            self.globalInfectionSet = self.infect(id)
            frontier[position] = self.teacherIdsExplored
            if len(self.teacherIdsExplored) > 0: 
                infectionCounts.append(len(self.globalInfectionSet))
                position += 1
            self.teacherIdsExplored = list() # reset list

        for id in self.selfLearnerIds: 
            frontier[position] = [id] 
            infectionCounts.append(1)
            position += 1

        print(frontier)
        print(infectionCounts)

        subsetSumResult = self.subset_sum(infectionCounts, target, strict)
        # result = self.extractLocations(subsetSumResult, frontier, infectionCounts)

    def subset_sum(self, nArr, target, strict): 
        closestSum = 0 
        result = []

        if min(nArr) > target or target <= 0: 
            return []

        powerset = chain.from_iterable(combinations(nArr, r) for r in range(len(nArr)+1))

        for item in powerset: 
            tempSum = sum(item)
            if tempSum == target: 
                return sorted(list(item))
            elif tempSum < target and tempSum > closestSum: 
                closestSum = tempSum 
                result = list(item)

        if strict: 
            return []
        else: 
            return sorted(result)

    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))




        
    # def total_infection(self, userId): 
    #     """Infect user and user's connections

    #     Parameters
    #     ----------
    #     userId : str, the id of the user

    #     Returns
    #     -------
    #     infectedSet: set, a set of all infected userIds
    #     """
    #     infectedSet = set()

    #     if not self.users.get(userId) or self.users[userId].infected == True: 
    #         return infectedSet

    #     self.users[userId].infected = True # change infection 
    #     self.users[userId].siteVersion = 'B' # change site-version 
    #     infectedSet.add(userId)

    #     for id in self.users[userId].connections: 
    #         infectedSet = infectedSet | self.total_infection(id)

    #     return infectedSet

    # def limited_infection(self, userId, n, strict): 
    #     """Infect user and user's connections limit by less than equal to `n`. If `strict` is True limit by exactly `n`. 

    #     Parameters
    #     ----------
    #     userId : str, the id of the user
    #     n      : int, max number of users that can be infected. 
    #     strict : bool, if True then algorithm attempts to infect exactly `n` users. 

    #     Return
    #     ------
    #     result : bool, returns whether or not infecting userId will result in < n infections

    #     """
    #     # look at the teachers that we can infect based on a studentId/teacherId
    #     # 
    #     frontier = [] # just a list of connected people 



    # def limited_infection_validation(self): 
    #     pass




if __name__ == '__main__': 
    infectionSimulation = InfectionSimulation(20)
    infectionSet = infectionSimulation.total_infection(infectionSimulation.teacherIds[0])
    print(infectionSet)







