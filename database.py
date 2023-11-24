from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from model import SongLyric

class LyricsDatabase:
    # You can create your Atlas MongoDB account and change your username and password
    uri = "mongodb+srv://user:<password>@cluster0.qjxcral.mongodb.net/?retryWrites=true&w=majority"
    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    database = client.songs
    collection = database.songlyrics
    
    # GET request method
    def getSongs(self):
        return self.collection.find({})
    
    # GET request method for 1 song finding by a song_name
    def getSong(self, song_name: str): 
        return self.collection.find_one({"song_name" : song_name},{"group_name": 1,"song_name":1,
                                            "song_lyrics": 1, "_id": False} )

    # POST method to add a song to the database
    def addSong(self, song: SongLyric):
        return self.collection.insert_one({"group_name": song.group_name,
                                            "song_name": song.song_name,
                                            "song_lyrics": song.song_lyrics})
   
    # PUT method by a song_name
    def updateSongByName(self, song_name: str, songUpdated: SongLyric):
        return self.collection.find_one_and_update({"song_name": song_name},{"$set": {"group_name": songUpdated.group_name,
                                                                            "song_name": songUpdated.song_name,
                                                                            "song_lyrics":songUpdated.song_lyrics}})
                            
    # PUT method by id
    def updateSongById(self, id: str, songUpdated: SongLyric):
        return self.collection.find_one_and_update({"_id": ObjectId(id)},{"$set": {"group_name": songUpdated.group_name,
                                                                          "song_name": songUpdated.song_name,
                                                                          "song_lyrics":songUpdated.song_lyrics}})

    # DELETE method by a song_name
    def deleteSongByName(self, song_name: str):
        return self.collection.delete_one({"song_name": song_name})