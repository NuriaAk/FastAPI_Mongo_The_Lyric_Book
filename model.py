from pydantic import BaseModel, Field

class SongLyric(BaseModel):
    group_name: str = Field(...)
    song_name : str = Field(...)
    song_lyrics: str = Field(...)
