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
        return len(self.globalInfectionSet)

    def limited_infection(self, target, strict): 
        teacherFrontier = set()
        frontier = []
        position = 0

        for id in self.teacherIds: 
            if id not in teacherFrontier: 
                self.globalInfectionSet = self.infect(id)
                teacherFrontier = teacherFrontier.union(set(self.teacherIdsExplored))
                frontier.append([len(self.globalInfectionSet), self.teacherIdsExplored])
                self.teacherIdsExplored = list() # reset list
                position += 1

        for id in self.selfLearnerIds: 
            frontier.append([1, [id]])
            position += 1

        infectionCounts = self.subset_sum([count for (count, ids) in frontier], target, strict)
        frontier.sort()

        return self.extract_users_to_infect(infectionCounts, frontier)

    def extract_users_to_infect(self, infectionCounts, frontier): 
        if infectionCounts == []: 
            return [] 

        result = []

        for item in frontier: 
            if len(infectionCounts) > 0 and item[0] == infectionCounts[0]: 
                result.append(item[1])
                infectionCounts.pop(0)

        return result

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








