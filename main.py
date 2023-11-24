import uvicorn
from fastapi import FastAPI
from model import SongLyric
from database import LyricsDatabase
import exceptions
import schema
import clean_lyric

app = FastAPI()
db = LyricsDatabase()

@app.get("/")
def root() -> dict[str, str]:
    return({"message" : "Welcome to your lyrics book! Put here a song's lyrics without quotation marks and in one line."})

# Route to get songs from a database
@app.get("/getsongs")
def getallSongs():# -> list[dict[str, Any]]:
    songs = schema.list_serial(db.getSongs())
    return songs

# Route to get song by name
@app.get("/findsong/{song_name}")
def getSongByName(song_name: str):# -> dict[str, Any | None]:
# Check if the song is in library
    my_song = db.getSong(song_name)
    return {"result" : my_song}

# Route to add a lyrics
@app.post("/addsong")
# Warning: Put here a song's lyrics WITHOUT QUOTATION MARKS and in ONE LINE.
# Tip: You can use the function clean_lyric.encode(text) to encode your lyrics into json format. 
def addSong(song: SongLyric) -> dict[str, str]:
    exceptions.check_lyrics_lenghts(song)
    db.addSong(song = song)
    return {"message" : "successfull"}

# Route to update song by it's name
@app.put("/updatesong/byname/{song_name}")
def putSongByName(song_name, songUpdated: SongLyric) -> dict[str, str]:
    db.updateSongByName(song_name, songUpdated = songUpdated)
    return {"result" : "Song updated."}

# Route to update song by it's id
@app.put("/updatesong/byid/{id}")
def putSongById(id, songUpdated: SongLyric) -> dict[str, str]:
    db.updateSongById(id, songUpdated = songUpdated)
    return {"result" : "Song updated."}

# Route to delete a song by song_id
@app.delete("/deletesong/{song_name}")
def deleteSongByName(song_name: str) -> dict[str, str]:
    # Check if the song is in library
    mysong = db.getSong(song_name)
    exceptions.check_song_in_db(mysong)
    # Delete a song from the database
    db.deleteSongByName(song_name)
    return {"result" : "Song deleted."}

if __name__ == "__main__":
    uvicorn.run("main:app",
                host='127.0.0.1',
                port=8000,
                reload=True,
                log_level="info")