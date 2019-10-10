from labb6.song import Song
import timeit
from random import shuffle

#########################################################
#                        SETUP                          #
#########################################################

song_list = []

with open("unique_tracks.txt", "r", encoding="utf-8") as tracklist:
    for row in tracklist:
        songinfo = row.split("<SEP>")
        track_ID = songinfo[0]
        song_ID = songinfo[1]
        artist = songinfo[2]
        song_title = songinfo[3]
        song = Song(track_ID, song_ID, artist, song_title)
        song_list.append(song)


song_dict = {song.artist : song for song in song_list}

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

def bubblesort(array):
    # length of array, minus one since we will be comparing current val with next val
    array_len = len(array) - 1

    for i in range(array_len):

        for j in range(array_len - i):
            # if next value is larger, we swap them!
            # which is laughably easy in python
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


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
    """
    size = len(song_list)

    print("Antal element:", size)

    sista = song_list[size - 1]
    test_artist = sista.artist

    n = 1
    linjtid = timeit.timeit(stmt = lambda: linear_search(song_list, test_artist), number =n)
    print("linjärsökningen tog", round(linjtid, 4), "sekunder.")

    song_list.sort()
    bin_time = timeit.timeit(stmt = lambda: binary_search(song_list, test_artist), number =n)
    print("Binärsökningen på sorterad lista tog", round(bin_time, 4), "sekunder.")

    hash_time = timeit.timeit(stmt = lambda: hash_search(song_dict, test_artist), number =n)
    print("Hashsökning tog", round(hash_time, 4), "sekunder.")
    """
    smaller_list = song_list[0:1000]

    shuffle(smaller_list)
    sort_n = 80
    bubble_time = timeit.timeit(stmt=lambda: bubblesort(smaller_list), number = sort_n)
    print("Bubblesort tog", round(bubble_time, 4), "sekunder")

    qs_time = timeit.timeit(stmt=lambda: smaller_list.sort(), number=sort_n)
    print("Quicksort tog", round(qs_time, 4), "sekunder")






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
