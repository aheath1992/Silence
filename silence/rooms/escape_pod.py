from .. import interface
from ..util import move
from ..room import Room

map_ = """Lorem ipsum dolor sit amet, consectetur adipiscing elit
Vestibulum placerat aliquam erat, id blandit nisi facilisis sit amet. 
Aenean sit amet risus tincidunt sapien mattis hendrerit."""

def enter(room, player):
    talked_to_computer = False

    if room.has_been_entered_before:
        interface.print_multiple_lines(
            lines=[
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "Vestibulum placerat aliquam erat, id blandit nisi facilisis sit amet"
            ],
            delay=4
        )
    else:
        interface.print_multiple_lines(
            lines=[
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum placerat aliquam erat, id"
                "blandit nisi facilisis sit amet. Aenean sit amet risus tincidunt sapien mattis hendrerit. Sed"
                "fermentum ante id porta euismod. Donec eu arcu sit amet orci ultricies dapibus. Class aptent taciti"
                "sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec volutpat felis sed"
                "justo tincidunt, at dictum felis tempor. Vivamus sit amet metus dolor. Duis fermentum elit nec nulla"
                "feugiat congue. Etiam aliquet nisl eu tristique malesuada. "

            ],
            delay=4
        )

    while True:
        additional_commands = ["talk"]

        if (
                room.has_been_entered_before or \
                (talked_to_computer)
        ):
            additional_commands = ["move"]

        command = interface.get_game_command(player, room, additional_commands)

        if command == "talk":
            npc = interface.get_command(
                ["computer", "cancel"],
                True
            )

            if npc == "computer":
                interface.print_multiple_lines(
                    lines=[
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum placerat aliquam erat, id"
                        "blandit nisi facilisis sit amet. Aenean sit amet risus tincidunt sapien mattis hendrerit. Sed"
                        "fermentum ante id porta euismod. Donec eu arcu sit amet orci ultricies dapibus. Class aptent taciti"
                        "sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Donec volutpat felis sed"
                        "justo tincidunt, at dictum felis tempor. Vivamus sit amet metus dolor. Duis fermentum elit nec nulla"
                        "feugiat congue. Etiam aliquet nisl eu tristique malesuada. "
                    ],
                    delay=4
                )
                interface.print_()
                talked_to_computer = True
        else:
            place_to_move = move(["outside"])

            if place_to_move == "outside":
                room.has_been_entered_before = True
                from .center_of_town import room as center_of_town
                center_of_town.enter(player)

room = Room(
    map_=map_,
    enter=enter
)
