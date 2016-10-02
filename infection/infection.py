from itertools import chain, combinations

from .user import *

class InfectionSimulation(): 

    def __init__(self, users, teacherIds, selfLearnerIds, siteVersion): 
        """Initialize the InfectionSimulation

        Parameters
        ----------
        users : dict(str: User), a mapping of userIds to User objects
        teacherIds : list(str), a list of all the teacher IDs in users dict 
        selfLearnerIds : list(str), a list of all the self learner IDs in users dict
        siteVersion : str, site version that is being tested
        """
        self.users = dict(users)
        self.teacherIds = list(teacherIds) 
        self.selfLearnerIds = list(selfLearnerIds)
        self.siteVersion = siteVersion
        self.globalInfectionSet = set()
        self.teacherIdsExplored = list()
        
    def infect(self, userId): 
        """Infect userId and userId's connections

        Parameters
        ----------
        userId : str, the id of the user

        Returns
        -------
        infectedSet: set(str), a set of userId's that have been infected
        """
        if not self.users.get(userId) or self.users[userId].infected == True: 
            return set()

        infectedSet = set()
        
        self.users[userId].infected = True 
        self.users[userId].siteVersion = self.siteVersion 
        if self.users[userId].role == 'teacher': 
            self.teacherIdsExplored.append(userId)

        infectedSet.add(userId)

        for id in self.users[userId].connections: 
            # depth-first search
            infectedSet = infectedSet.union(self.infect(id))

        return infectedSet

    def total_infection(self, userId): 
        """Infect userId and get set of all users that will be infected as a result. 
        This method returns the number of users that will have been infected if userId 
        is infected. To view all of the user ID's that have been infected, access the 
        globalInfectionSet attribute. 

        Parameters
        ----------
        userId : str, the id of the user

        Returns
        -------
        result: int, number of users that have been infected
        """
        self.globalInfectionSet = self.infect(userId)
        return len(self.globalInfectionSet)

    def limited_infection(self, target, strict): 
        """Infect userId and get set of all users that will be infected as a result. 
        This method returns the number of users that will have been infected if userId 
        is infected. To view all of the user ID's that have been infected, access the 
        globalInfectionSet attribute. 

        Parameters
        ----------
        target : int, target number of users to be infected
        strict : bool, indicate whether exactly `target` number of users are to 
                 be infected or not. 

        Returns
        -------
        result: list(list(str, ...,), ...,), 
                returns a list of lists of userIds that can be infected to get `target` 
                amount of users to be infected
        """
        frontier = []

        for id in self.teacherIds: 
            result = self.infect(id)
            if result: 
                frontier.append([len(result), self.teacherIdsExplored])
                self.teacherIdsExplored = list() # reset 

        for id in self.selfLearnerIds: 
            frontier.append([1, [id]])

        frontier.sort()
        infectionCounts = self.subset_sum([count for (count, ids) in frontier], target, strict)
        
        return self.extract_users_to_infect(infectionCounts, frontier)

    def extract_users_to_infect(self, infectionCounts, frontier): 
        """Infect userId and get set of all users that will be infected as a result. 
        This method returns the number of users that will have been infected if userId 
        is infected. To view all of the user ID's that have been infected, access the 
        globalInfectionSet attribute. 

        Parameters
        ----------
        infectionCounts : list(int), count of infections that add up/close to `target`
        frontier : list(list(int, list(str)), ...), a collection of [number of infections, [userIds]] 

        Returns
        -------
        result: list(list(str, ...,), ...,), 
                returns a list of lists of userIds that can be infected to get `target` 
                amount of users to be infected
        """

        if infectionCounts == []: 
            return [] 

        result = []

        for item in frontier: 
            if len(infectionCounts) > 0 and item[0] == infectionCounts[0]: 
                result.append(item[1])
                infectionCounts.pop(0)

        return result

    def subset_sum(self, nArr, target, strict): 
        """Find subset of `nArr` that sums closest (without exceeding) to `target` if `strict` 
        is False else sums exactly to `target` if `strict` is True. 

        Parameters
        ----------
        nArr : list(int), a list of numbers
        target : int, target sum
        strict : bool, indicate whether to find subset exactly equal to `target` or not

        Returns
        -------
        result: list(int), list of integers that sum closest or exactly to `target` else returns
                blank list (i.e. list())
        """
        if min(nArr) > target or target <= 0: 
            return []

        closestSum = 0 
        result = []
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


