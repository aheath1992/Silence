"""This modules contains the code representing the items in the game."""

from . import item, attack

plasma_sword = item.Item(
    display_name="Plasma sword",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="strength", modifier=5), item.ItemEffect(stat="dexterity", modifier=-2)],
    attacks=[
        attack.Attack(
            name="stab",
            display_name="Stab",
            type_=attack.MELEE,
            damage=3,
            stamina_cost=2,
            description_of_being_used="stab"
        ),
        attack.Attack(
            name="slash",
            display_name="Slash",
            type_=attack.MELEE,
            damage=5,
            stamina_cost=4,
            description_of_being_used="slash"
        )
    ]
)

blaster = item.Item(
    display_name="Blaster",
    type_=item.EQUIPPABLE,
    equip_location="arms",
    effects=[item.ItemEffect(stat="range", modifier=5), item.ItemEffect(stat="dexterity", modifier=-1)],
    attacks=[
        attack.Attack(
            name="shoot",
            display_name="Shoot",
            type_=attack.RANGED,
            damage=3,
            stamina_cost=1,
            description_of_being_used="shoot"
        )
    ]
)


def health_potion():
    return item.Item(
        display_name="Health potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="health", modifier=10)]
    )

def stamina_potion():
    return item.Item(
        display_name="Stamina potion",
        type_=item.CONSUMABLE,
        effects=[item.ItemEffect(stat="stamina", modifier=10)]
    )
