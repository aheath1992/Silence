from .escape_pod import room as escape_pod

rooms = [
    escape_pod
]

def reset():
    for room in rooms:
        room.has_been_entered_before = False
