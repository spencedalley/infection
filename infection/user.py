class User(): 

    def __init__(self, id, role, infected, siteVersion, connections): 
        """Representation of a user 

        Parameters
        ----------
        _id : str, unique id of the user
        role : str, the user's role, it's either `teacher` or `student`
        infected : bool, is the user seeing the new version of the website? 
        siteVersion : str, what version of the site user sees
        connections: list(str), list of user's userIDs that this user is connected to 
        """
        self._id = id
        self.role = role
        self.infected = infected 
        self.siteVersion = siteVersion 
        self.connections = connections 