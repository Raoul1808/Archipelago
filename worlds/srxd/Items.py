from typing import NamedTuple, Optional

from BaseClasses import Item


class SrxdItem(Item):
    game = "Spin Rhythm XD"


class SrxdItemData(NamedTuple):
    song_id: Optional[int]
#     dlc_pack: Optional[str]
