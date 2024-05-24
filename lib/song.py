class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(self):
        self.count += 1

    def add_to_genres(self):
        if self.genre not in self.__class__.genres:
            self.__class__.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.__class__.artists:
            self.__class__.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre in self.__class__.genre_count:
            self.__class__.genre_count[self.genre] += 1
        else:
            self.__class__.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in self.__class__.artist_count:
            self.__class__.artist_count[self.artist] += 1
        else:
            self.__class__.artist_count[self.artist] = 1

    @classmethod
    def get_count(self):
        return self.count

    @classmethod
    def get_artists(self):
        return self.artists

    @classmethod
    def get_genres(self):
        return self.genres

    @classmethod
    def get_genre_count(self):
        return self.genre_count

    @classmethod
    def get_artist_count(self):
        return self.artist_count



ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
god_plan = Song("God's Plan", "Drake", "Rap")

print(Song.get_count())  
print(Song.get_artists()) 
print(Song.get_genres())  
print(Song.get_genre_count()) 
print(Song.get_artist_count())  
