from database import SongLyric
from fastapi import HTTPException  


def check_lyrics_lenghts(song: SongLyric):
    if len(song.song_lyrics) >= 2000:
        raise HTTPException(status_code=400, detail="Sorry. It seems that your song is too long =( ).")
    if len(song.song_lyrics) <= 3:
        raise HTTPException(status_code=400, detail="Sorry. It seems that your song is too short =( ).")

def check_song_in_db(song: SongLyric):
    if song == None:
        raise HTTPException(status_code=404, detail = "Song not found.")
