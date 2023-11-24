from model import SongLyric


def individual_serial(song: SongLyric):
    return{
        "id":str(song["_id"]),
        "group_name": song["group_name"],
        "song_name" : song["song_name"],
        "song_lyrics":song["song_lyrics"]
    }

def list_serial(songs):
    return[individual_serial(song) for song in songs]