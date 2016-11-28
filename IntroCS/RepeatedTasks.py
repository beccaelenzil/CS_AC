def numMatches(userPrefs, storedUserPrefs):
    ''' return the number of elements that match between
        the lists userPrefs and storedUserPrefs '''
    count = 0
    for item in userPrefs:
        if item in storedUsersPrefs:
            count += 1
    return count


def listDoubler(aList):
	doubledList = []
	for elem in aList:
	# append the value 2*elem to doubledList
	    doubledList.append(2*elem)
	return doubledList

print (listDoubler([20, 21, 22]))


artists = []

for i in [0, 1, 2]:
    next_artist = raw_input('Enter an artist that you like:')
    artists.append(next_artist)

print ('Thank you!  Well work on your recommendations now.')


artists = []

for i in ['i', 'love', 'spam']:
    next_artist = raw_input('Enter an artist that you like:')
    artists.append(next_artist)

print ('Thank you!  Well work on your recommendations now.')
