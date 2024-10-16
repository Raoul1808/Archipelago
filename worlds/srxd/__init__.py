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

    item_name_to_id = {name: code for code, name in song_list.songs}
    location_name_to_id = {name: code for code, name in song_list.songs}

    def generate_early(self) -> None:
        for song_id in self.song_list.starting_songs:
            _, name = self.song_list.songs[song_id]
            self.multiworld.push_precollected(self.create_item(name))

    def create_item(self, name: str) -> SrxdItem:
        return SrxdItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        for song_id, song_name in self.song_list.songs:
            loc = SrxdLocation(self.player, song_name, self.location_name_to_id[song_name], menu_region)
            loc.access_rule = lambda state, place=song_name: state.has(place, self.player)
            menu_region.locations.append(loc)

    def create_items(self) -> None:
        for _, song in self.song_list.songs:
            self.multiworld.itempool.append(self.create_item(song))

    def fill_slot_data(self):
        return {
            "deathLink": self.options.death_link.value
        }
