class User(): 

    def __init__(self, id, role, infected, siteVersion, connections): 
        """Representation of a user 

        Parameters
        ----------
        _id : str, unique id of the user
        role : str, the user's role, it's either `teacher` or `student`
        infected : bool, does user see new version of website? 
        siteVersion : str, what version of the site user sees (e.g. either `A` or `B`)
        connections: list(str), list of user's userIDs that this user is connected to 
        """
        self._id = id
        self.role = role
        self.infected = infected 
        self.siteVersion = siteVersion 
        self.connections = connections 


def generate_users(n): 
    # generate `n` users
    userIds = [str(i) for i in range(n)]
    users = {}
    teachersIds = []
    selfLearnersIds = []
    currentTeacherId = ''

    # add n-3 users with every 10th user being a teacher
    for i in range(len(userIds)-3): 
        if i % 10 == 0: 
            currentTeacherId = userIds[i]
            teachersIds.append(currentTeacherId)
            user = User(userIds[i], 'teacher', False, siteVersion='A', connections=[])
        else: 
            user = User(userIds[i], 'student', False, siteVersion='A', connections=[currentTeacherId]) # give teacher connection
            users[currentTeacherId].connections.append(userIds[i]) # append student Id to teacher
        
        users[userIds[i]] = user

    # Add three self-learners
    for i in range(len(userIds)-3, len(userIds)): 
        selfLearnersIds.append(userIds[i])
        users[userIds[i]] = User(userIds[i], 'student', False, siteVersion='A', connections=[])

    users['1'].connections.append(teachersIds[1]) # give one student two teachers

    return (users, teachersIds, selfLearnersIds)



