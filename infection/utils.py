from .user import User

def init_users(): 
    users = {
        # Teachers
        '0': User('0', 'teacher', False, 'A', [str(i) for i in range(6, 11)]+['11']),
        '1': User('1', 'teacher', False, 'A', [str(i) for i in range(11, 16)]+['2', '16']),
        '2': User('2', 'teacher', False, 'A', [str(i) for i in range(16, 21)]+['15']),
        '3': User('3', 'teacher', False, 'A', [str(i) for i in range(21, 25)]+['26']),
        '4': User('4', 'teacher', False, 'A', [str(i) for i in range(26, 31)]),
        '5': User('5', 'teacher', False, 'A', ['31']),

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

    teacherIds = ['0', '1', '2', '3', '4', '5']
    selfLearnerIds = [str(i) for i in range(32, 34)]

    return (users, teacherIds, selfLearnerIds)

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



