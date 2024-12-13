import ipdb
class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = []
    artists = []
    
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)

    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls,genre):
        cls.add_to_genre_count(genre)
        if not any([gen == genre for gen in cls.genres]):
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        cls.add_to_artist_count(artist)
        if not any([art == artist for art in cls.artists]):
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        current = cls.genre_count.get(genre,0)
        cls.genre_count[genre] = current + 1
    
    @classmethod
    def add_to_artist_count(cls,artist):
        current = cls.artist_count.get(artist,0)
        cls.artist_count[artist] = current + 1
    
#s = Song("s","g","s")
#ipdb.set_trace()