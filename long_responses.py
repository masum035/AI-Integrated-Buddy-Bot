import random

R_EATING = "I don't want eating anything because I'm a bot obviously!"


def unknown():
    response = ["Could you please re-phase that?",
                "....",
                "Sounds about right?",
                "What does that mean?",
                "I can't understand what you are saying.."][random.randrange(5)]
    return response
