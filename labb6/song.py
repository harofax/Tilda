class Song:

    def __init__(self, track_id, song_id, artist, song_title):
        self.track_id = track_id
        self.song_id = song_id
        self.artist = artist
        self.song_title = song_title

    def __lt__(self, other):
        return self.artist < other.artist

    def __str__(self):
        return "Track ID: " + self.track_id + ", Song ID: " + self.song_id + \
               ", Artist: " + self.artist + ", Song title: " + self.song_title



