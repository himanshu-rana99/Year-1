'''
Created on Nov 15, 2017

@author: hrana2 - Himanshu Rana 
" I pledge my honor that I have abided by the Stevens Honor System" 

@author: jvalenzu - Jessica Valenzuela 
" I pledge my honor that I have abided by the Stevens Honor System"
'''

PREF_FILE = "musicrecplus.txt"

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'.
        Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict
         
def getPreferences(userName, userMap):
    ''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs


def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = drop(prefs, userMap[bestUser])
    return recommendations

def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = numMatches(prefs, userMap[user])
        if score > bestScore and currUser != user:
            bestScore = score
            bestUser = user
    return bestUser

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    
    return list3

def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()  
    
artistFreq = {}
artistFreq_Temp = {}
def getPopular(userMap):
    '''Gets the frequency of the artists in the whole database and returns
which is the most frequent artist'''
    global artistFreq
    global artistFreq_Temp
    
    for user in list(userMap.values()):
        for artist in user:
            if artist in artistFreq:
                artistFreq[artist] += 1
            else:
                artistFreq[artist] = 1

    artistFreq_Temp = artistFreq
    artistFreq = {}
    return mostFreq(artistFreq_Temp)

def mostFreq(artistFreq):
    '''Turns the dictionary of artists or users and frequency of each to determine
which is the most frequent or most number of preferences, returns the most frequent artist.'''
    tempLKey = list(artistFreq.keys())
    tempLVal = list(artistFreq.values())
    return tempLKey[tempLVal.index(max(tempLVal))]


def standardizeAll(storedPrefs):
    ''' Returns a new list of lists of stored user preferences,
    with each artist string in Title Case,
    with leading and trailing whitespace removed.
    '''
    standardStoredPrefs = []
    for storedUser in storedPrefs:
        standardStoredUser = []
        for artist in storedUser:
            standardStoredUser.append(artist.strip().title())
        standardStoredPrefs.append(standardStoredUser)
    return standardStoredPrefs


def main():
    ''' The main recommendation function '''
    ############### Variable ######################################
    global artistFreq
    
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!")

    userName = input("Please enter your name: ")
    print ("Welcome,", userName)

    userMap = dictToL(userMap)
    popular = getPopular(userMap)
    option = None
    ##############################################################
    while option != 'q':
        option = input('\nEnter a letter to choose an option:\n\
e - enter\n\
r - Get recommendations\n\
p - Show most popular artists\n\
h - How popular is the most popular\n\
m - Which user has the most likes\n\
q - Save and quit ')
        if option == 'e':
            prefs = getPreferences(userName, userMap)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            userMap = dictToL(userMap)
        elif option == 'r':
            prefs = userMap[userName]
            recs = getRecommendations(userName, prefs, userMap)
            # Print the user's recommendations
            if len(recs) == 0:
                print("I'm sorry but I have no recommendations")
                print("for you right now.")
            else:
                print(userName, "based on the users I currently")
                print("know about, I believe you might like:")
                for artist in recs:
                    print(artist)

                print("I hope you enjoy them! I will save your")
                print("preferred artists and have new")
                print(" recommendations for you in the future")

        elif option == 'p':
            popular = getPopular(userMap)
            print('\nThe most popular artist/band is', popular)
        elif option == 'h':
            howPopular = artistFreq_Temp[popular]
            print('\n',str(howPopular).strip(),'users like the most popular artist,', popular)
        elif option == 'm':
            userMostLikes = numOfPref(userMap)
            userMostPref = userMap[userMostLikes]
            print('\nThe user with the most likes is',userMostLikes,', here are\
 his preferences:',userMostPref)

def numOfPref(userMap):
    '''Assigns each use to the number of preferences each user has except the
users who are private  ($ at end of name) and returns the most user with the
the most number of preferences.'''
    numOfPref = {}
    index = 0
    for user in userMap:
        if '$' in user:
            index += 1
            continue
        numOfPref[user] = len(list(userMap.values())[index])
        index += 1
    return mostFreq(numOfPref)
             
def dictToL(userMap):
    '''This turns the dictionary values into a list to be examined and standardized
all values (Preferences)'''
    L = []
    for user in list(userMap.values()):
        L.append(user)
    return listToDict(standardizeAll(L),userMap)

def listToDict(userList,userMap):
    '''This turns the list values back into the dictionary values to be examined.'''
    index = 0
    for key in userMap:
        userMap[key] = userList[index]
        index += 1
    return userMap
    
   

if __name__ == "__main__": main()