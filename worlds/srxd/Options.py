from dataclasses import dataclass

from Options import PerGameCommonOptions, DeathLink, OptionSet


# class SrxdDLC(OptionSet):
#     """Choose which DLCs should be added to the random pool."""
#     display_name = "Enabled DLCs"
#     default = {}
#     valid_keys = ["Supporter Pack", "Monstercat DLC", "Chillhop DLC"]


@dataclass
class SrxdOptions(PerGameCommonOptions):
    death_link: DeathLink
#     enabled_dlc: SrxdDLC
