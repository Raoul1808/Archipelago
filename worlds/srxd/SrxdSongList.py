from typing import Dict


def load_text_file(name: str) -> str:
    import pkgutil
    return pkgutil.get_data(__name__, name).decode()


class SrxdSongList:
    songs: Dict[int, str]

    def __init__(self):
        songs = {}
        songs_file = load_text_file("SongList.txt")
        for line in songs_file.splitlines():
            elems = line.split('|')
            song_id = int(elems[0])
            song_name = elems[1]
            songs[song_id] = song_name
        self.songs = songs
