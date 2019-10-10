from labb6.song import Song
import timeit
from labb7.DictHash import HashTable

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

def linear_search(arr, key):
    for x in arr:
        if x.artist == key:
            return True
    return False


def binary_search(arr, key):
    lower = 0
    upper = len(arr)

    while lower < upper:
        middle = lower + (upper - lower) // 2
        val = arr[middle]

        if val.artist == key:
            return True
        elif key > val.artist:
            if lower == middle:
                break
            lower = middle
        elif key < val.artist:
            upper = middle


def hash_search(song_dict, artist):

    return artist in song_dict

def main():

    n = len(song_list)

    print("Antal element:", n)

    sista = song_list[n - 1]
    test_artist = sista.artist

    linjtid = timeit.timeit(stmt = lambda: linear_search(song_list, test_artist), number = 10000)
    print("linjärsökningen tog", round(linjtid, 4), "sekunder.")

    song_list.sort()
    bin_time = timeit.timeit(stmt = lambda: binary_search(song_list, test_artist), number = 10000)
    print("Binärsökningen på sorterad lista tog", round(bin_time, 4), "sekunder.")

    hash_time = timeit.timeit(stmt = lambda: hash_search(song_dict, test_artist), number = 10000)
    print("Hashsökning tog", round(hash_time, 4), "sekunder.")

main()