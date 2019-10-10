import timeit
from random import shuffle

#########################################################
#                        SETUP                          #
#########################################################

song_list = []

class Song:
    def __init__(self, trackID, songID, artist, song_title):
        self.trackID = trackID
        self.songID = songID
        self.artist = artist
        self.song_title = song_title

    def __str__(self):
        return "artist: " + self.artist + ", song_title: " + self.song_title

    def __lt__(self, other):
        return ((self.artist) < (other.artist))


with open("unique_tracks.txt", "r", encoding="utf-8") as tracklist:
    for row in tracklist:
        songinfo = row.split("<SEP>")
        track_ID = songinfo[0]
        song_ID = songinfo[1]
        artist = songinfo[2]
        song_title = songinfo[3]
        song = Song(track_ID, song_ID, artist, song_title)
        song_list.append(song)

#########################################################
#                       SÖKNING                         #
#########################################################

def linear_search(tracklist, artist):
    for song in tracklist:
        if song.artist == artist:
            return True
    return False


def binary_search(tracklist, artist):
    lower = 0
    upper = len(tracklist)

    while lower < upper:
        middle = lower + (upper - lower) // 2
        song = tracklist[middle]

        if song.artist == artist:
            return True
        elif artist > song.artist:
            if lower == middle:
                break
            lower = middle
        elif artist < song.artist:
            upper = middle


def hash_search(song_dict, artist):

    return artist in song_dict

########################################################
#                     SORTING ALGS                     #
########################################################

#def insertionSort(array):
#    for i in range(1, len(array)):
#        key = array[i]
#        j = i-1
#        while j >=0 and key < array[j] :
#                array[j+1] = array[j]
#                j -= 1
#        array[j+1] = key
#        return array



def quicksort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quicksort(less) + equal + quicksort(greater)

    # slutet av rekursionen, stoppfallet
    else:
        return array

########################################################
#                       MAIN                           #
########################################################


def main():

    n = 1000
    smaller_list = song_list[0:250000]

    size = len(smaller_list)
    print("Antal element:", size)

    sista = song_list[size - 1]
    test_artist = sista.artist

    song_dict = {song.artist: song for song in smaller_list}

    linjtid = timeit.timeit(stmt = lambda: linear_search(smaller_list, test_artist), number =n)
    print("linjärsökningen tog", round(linjtid, 4), "sekunder.")

    smaller_list.sort()

    bin_time = timeit.timeit(stmt = lambda: binary_search(smaller_list, test_artist), number =n)
    print("Binärsökningen på sorterad lista tog", round(bin_time, 4), "sekunder.")

    hash_time = timeit.timeit(stmt = lambda: hash_search(song_dict, test_artist), number =n)
    print("Hashsökning tog", round(hash_time, 4), "sekunder.")

    shuffle(smaller_list)
    sort_n = 1000

    pysort_time = timeit.timeit(stmt=lambda: smaller_list.sort, number = sort_n)
    print("Pythons sortfunktion tog", round(pysort_time, 4), "sekunder")

    #qs_time = timeit.timeit(stmt=lambda: smaller_list.sort(), number=sort_n)
    #print("Quicksort tog", round(qs_time, 4), "sekunder")

main()


#####################################
#             SÖKNINGAR             #
#####################################

#################################################################
#            | n= 250 000         n= 500 000     n= 1 000 000   #
# ___________|_________________________________________________ #
# Linjär     |     13.1193           24.1981       48.5282      #
#            |                                                  #
# Binär      |     2.487             2.29683       5.9332       #
#            |                                                  #
# Dict       |     0.0586            0.1102        0.2279       #
#            |                                            [sek] #
#################################################################



########################################################################
#                         S O R T E R I N G                            #
########################################################################

################################################################################
#              | n = 1000       n = 10 000     n = 100 000     n = 1 000 000   #
# _____________|______________________________________________________________ #
# Python sort  |  0.0005 s       0.0025 s       0.038 s          0.3189 s      #
#              |                                                               #
# Quick sort   |  0.4517 s       5.1563 s        51.59 s         463.0291 s    #
#              |                                                   [sek]       #
################################################################################