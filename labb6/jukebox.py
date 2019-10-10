import timeit
from random import shuffle
from labb6.song import Song

#########################################################
#                        SETUP                          #
#########################################################



def readfile(filename):
    song_list = []
    with open(filename, "r", encoding="utf-8") as tracklist:
        for row in tracklist:
            songinfo = row.split("<SEP>")
            track_ID = songinfo[0]
            song_ID = songinfo[1]
            artist = songinfo[2]
            song_title = songinfo[3]
            song = Song(track_ID, song_ID, artist, song_title)
            song_list.append(song)

    return song_list


#########################################################
#                       SÖKNING                         #
#########################################################

def linear_search(tracklist, artist):
    for i in range(len(tracklist)):
        if tracklist[i].artist == artist:
            return tracklist[i]
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

    song_list = readfile("unique_tracks.txt")

    n = 10000
    smaller_list = song_list[0:250000]

    size = len(smaller_list)
    print("Antal element:", size)

    sista = smaller_list[size - 2]
    test_artist = sista.artist

    print(str(sista))

    song_dict = {song.artist: song for song in smaller_list}

    linjtid = timeit.timeit(stmt = lambda: linear_search(smaller_list, test_artist), number =n)
    print("linjärsökningen tog", round(linjtid, 4), "sekunder.")

    sorted_songs = sorted(smaller_list)

    bin_time = timeit.timeit(stmt = lambda: binary_search(sorted_songs, test_artist), number =n)
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
# Linjär     |    1.3768             13.6894       48.5282      #
#            |                                                  #
# Binär      |    0.0115             0.0091       5.9332       #
#            |                                                  #
# Dict       |    0.0002             0.0001        0.2279       #
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