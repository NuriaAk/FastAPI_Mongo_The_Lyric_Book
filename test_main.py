from main import app
from fastapi.testclient import TestClient

test_client = TestClient(app)


def test_read_songs():
    response = test_client.get("/getsongs")
    assert response.status_code == 200

def test_post_song():
    response = test_client.post("/addsong", json = {"group_name" : "Petite Noir", "song_name" : "Disappear", "song_lyrics" : "We are not the same Forever to the end of time, my love Ill never be the same I ll never be the same Standing in the dark I see the demons tryna take my heart Ill never be the same All we have in life will disappear All we have in life will disappеar Stranded out at sea The ocеan of the vultures welcomes me Killing for you love All the things I see"})
    assert response.status_code == 200
    assert response.json() == {'message': 'successfull'}
    test_client.delete("/deletesong/Disappear")

def test_find_song():
    test_client.post("/addsong", json = {"group_name" : "Petite Noir", "song_name" : "Disappear", "song_lyrics" : "We are not the same Forever to the end of time, my love Ill never be the same I ll never be the same Standing in the dark I see the demons tryna take my heart Ill never be the same All we have in life will disappear All we have in life will disappеar Stranded out at sea The ocеan of the vultures welcomes me Killing for you love All the things I see"})
    response = test_client.get("/findsong/Disappear")
    assert response.status_code == 200
    assert response.json() == {"result" : {"group_name" : "Petite Noir", "song_name" : "Disappear", "song_lyrics" : "We are not the same Forever to the end of time, my love Ill never be the same I ll never be the same Standing in the dark I see the demons tryna take my heart Ill never be the same All we have in life will disappear All we have in life will disappеar Stranded out at sea The ocеan of the vultures welcomes me Killing for you love All the things I see"}}
    test_client.delete("/deletesong/Disappear")

def test_updatesong_byname():
    test_client.post("/addsong", json = {"group_name" : "Petite Noir", "song_name" : "Disappear", "song_lyrics" : "We are not the same Forever to the end of time, my love Ill never be the same I ll never be the same Standing in the dark I see the demons tryna take my heart Ill never be the same All we have in life will disappear All we have in life will disappеar Stranded out at sea The ocеan of the vultures welcomes me Killing for you love All the things I see"})
    response = test_client.put("/updatesong/byname/Disappear", json = {"group_name" : "Petite Noir", "song_name" : "Disappear", "song_lyrics" : "Lyrics changed"})
    assert response.status_code == 200
    assert response.json() == {"result" : "Song updated."}
    test_client.delete("/deletesong/Disappear")

def test_delete_byname():
    test_client.post("/addsong", json = {"group_name" : "Petite Noir", "song_name" : "Disappear", "song_lyrics" : "We are not the same Forever to the end of time, my love Ill never be the same I ll never be the same Standing in the dark I see the demons tryna take my heart Ill never be the same All we have in life will disappear All we have in life will disappеar Stranded out at sea The ocеan of the vultures welcomes me Killing for you love All the things I see"})
    response = test_client.delete("/deletesong/Disappear")
    assert response.status_code == 200
    assert response.json() == {"result" : "Song deleted."}
    test_client.delete("/deletesong/Disappear")