"""
This modules handles the interface and the logic behind creating the player's
character.
"""

from . import interface
from .combat_entity import CombatEntity
from .player import Player
from . import attack

_ENTITY_DISPLAY_NAME = "You"
_CRITICAL_HIT_CHANCE = 4

_PUNCH_ATTACK = attack.Attack(
    name="punch",
    display_name="Punch",
    type_=attack.MELEE,
    damage=1,
    stamina_cost=2,
    description_of_being_used="punch"
)

_SPACEMAN_ENTITY = CombatEntity(
    display_name=_ENTITY_DISPLAY_NAME,
    attacks=[_PUNCH_ATTACK],
    maximum_health=30,
    maximum_stamina=30,
    strength=8,
    defence=10,
    dexterity=20,
    composure=20,
    critical_hit_chance=_CRITICAL_HIT_CHANCE
)


def create_player():
    """
    Display an interface that allows the player to create their character.

    Returns
    -------
    Player
        The Player instance representing the player.
    """

    return Player(_SPACEMAN_ENTITY, "Spaceman")
