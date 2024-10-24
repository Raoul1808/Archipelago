from random import randint

from BaseClasses import Tutorial, Region, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import SrxdItem
from .Locations import SrxdLocation
from .Options import SrxdOptions
from .SrxdSongList import SrxdSongList


class SrxdWebWorld(WebWorld):
    theme = "partyTime"

    tutorials = [Tutorial(
        "Mod Setup and Use Guide",
        "A guide to setting up Spin Rhythm XD with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Raoul1808"]
    )]

class SrxdWorld(World):
    """Placeholder SRXD description I'm not good for this ;-;"""
    # TODO: Add actual description

    game = "Spin Rhythm XD"
    web = SrxdWebWorld()
    options = SrxdOptions
    options_dataclass = SrxdOptions

    song_list = SrxdSongList()
    boss_song: int
    starting_songs: [int]

    item_name_to_id = {name: code for code, name in song_list.songs.items()}
    location_name_to_id = {name: code for code, name in song_list.songs.items()}

    def generate_early(self) -> None:
        song_ids = [song_id for song_id, _ in self.song_list.songs.items()]
        self.starting_songs = []
        for _ in range(3):
            song_id = song_ids.pop(randint(0, len(song_ids) - 1))
            song_name = self.song_list.songs[song_id]
            self.starting_songs.append(song_id)
            self.multiworld.push_precollected(self.create_item(song_name))
        self.boss_song = song_ids.pop(randint(0, len(song_ids) - 1))

    def create_item(self, name: str) -> SrxdItem:
        return SrxdItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        for song_id, song_name in self.song_list.songs.items():
            loc = SrxdLocation(self.player, song_name, self.location_name_to_id[song_name], menu_region)
            loc.access_rule = lambda state, place=song_name: state.has(place, self.player)
            menu_region.locations.append(loc)

    def create_items(self) -> None:
        for song_id, song_name in self.song_list.songs.items():
            if song_id != self.boss_song and song_id not in self.starting_songs:
                self.multiworld.itempool.append(self.create_item(song_name))

    def fill_slot_data(self):
        return {
            "deathLink": self.options.death_link.value,
            "clearCondition": self.options.clear_condition.value,
            "medalRequirement": self.options.medal_requirement.value,
            "targetAccuracy": self.options.target_accuracy.value,
            "bossSong": self.boss_song,
            "clearsRequiredForGoal": self.options.goal_requirement.value,
        }
