import json
from typing import Dict


def load_text_file(name: str) -> str:
    import pkgutil
    return pkgutil.get_data(__name__, name).decode()


class SrxdSongList:
    songs: Dict[int, str]

    def __init__(self):
        songs = {}
        song_list_raw = load_text_file("SongList.json")
        song_list = json.loads(song_list_raw)
        for song in song_list:
            song_id = song["Id"]
            song_name = song["Title"]
            song_name_duplicate_number = 1
            song_name_not_duplicate = song_name
            while song_name_not_duplicate in songs:
                song_name_not_duplicate = f"{song_name} ({song_name_duplicate_number})"
                song_name_duplicate_number += 1
            songs[song_id] = song_name_not_duplicate
        self.songs = songs
