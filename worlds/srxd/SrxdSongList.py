import random

from typing import Dict


def load_text_file(name: str) -> str:
    import pkgutil
    return pkgutil.get_data(__name__, name).decode()


class SrxdSongList:
    songs = Dict[int, str]
    starting_songs = [int]

    def __init__(self):
        songs = []
        starting_songs = []
        songs_file = load_text_file("SongList.txt")
        for line in songs_file.splitlines():
            elems = line.split('|')
            song_id = int(elems[0])
            song_name = elems[1]
            songs.append((song_id, song_name))
        song_indices = list(range(len(songs)))
        for _ in range(3):
            starting_songs.append(song_indices.pop(random.randint(0, len(song_indices) - 1)))
        SrxdSongList.songs = songs
        SrxdSongList.starting_songs = starting_songs
