from dataclasses import dataclass

from Options import PerGameCommonOptions, DeathLink, OptionSet, Choice, Range


# class SrxdDLC(OptionSet):
#     """Choose which DLCs should be added to the random pool."""
#     display_name = "Enabled DLCs"
#     default = {}
#     valid_keys = ["Supporter Pack", "Monstercat DLC", "Chillhop DLC"]


class SrxdDeathLink(DeathLink):
    """When you die, everyone who enabled death link dies. Of course, the reverse is true too.
    This option can also be toggled in-game."""


class SrxdClearCondition(Choice):
    """
    Sets the clear condition for a song to earn a location check.
    Regardless of setting, you need to clear the song to pass. Failing with or without No Fail on will not count.

    - Default: Pass the level.
    - Specific Medal: Earn the specified medal below to pass.
    - Accuracy Challenge: Pass a song without falling below the target accuracy defined below to pass.
    - Full Combo: Don't break combo to pass.
    - Perfect Full Combo: Get only perfect judgements to pass.
    """
    display_name = "Clear Condition"

    option_default = 0
    option_medal = 1
    option_accuracy = 2
    option_full_combo = 3
    option_perfect_full_combo = 4


class SrxdMedalRequirement(Choice):
    """Sets the medal requirement to earn a location check. Used only with clear condition set to Medal."""
    display_name = "Medal Requirement"

    option_d = 0
    option_d_plus = 1
    option_c = 2
    option_c_plus = 3
    option_b = 4
    option_b_plus = 5
    option_a = 6
    option_a_plus = 7
    option_s = 8
    option_s_plus = 9


class SrxdTargetAccuracy(Range):
    """Sets the minimum required accuracy to earn a location check.
    Used only with clear condition set to Accuracy."""
    display_name = "Target Accuracy"

    range_start = 0
    range_end = 100
    default = 80


@dataclass
class SrxdOptions(PerGameCommonOptions):
    death_link: SrxdDeathLink
    clear_condition: SrxdClearCondition
    medal_requirement: SrxdMedalRequirement
    target_accuracy: SrxdTargetAccuracy
#     enabled_dlc: SrxdDLC
