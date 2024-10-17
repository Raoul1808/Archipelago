from dataclasses import dataclass

from Options import PerGameCommonOptions, DeathLink, OptionSet


# class SrxdDLC(OptionSet):
#     """Choose which DLCs should be added to the random pool."""
#     display_name = "Enabled DLCs"
#     default = {}
#     valid_keys = ["Supporter Pack", "Monstercat DLC", "Chillhop DLC"]


class SrxdDeathLink(DeathLink):
    """When you die, everyone who enabled death link dies. Of course, the reverse is true too.
    This option can also be toggled in-game."""


@dataclass
class SrxdOptions(PerGameCommonOptions):
    death_link: SrxdDeathLink
#     enabled_dlc: SrxdDLC
