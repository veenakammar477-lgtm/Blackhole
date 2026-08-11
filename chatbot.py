import wikipedia


def get_response(message):
    message = message.lower().strip()

    # Greeting
    if message in ["hello", "hi", "hey"]:
        return "Hello! I am BlackHole AI. 🌌"

    # Name
    if "your name" in message:
        return "My name is BlackHole AI. ⚫"

    # Black hole
    if "what is a black hole" in message or "what is black hole" in message:
        return (
            "A black hole is a region of space where gravity is extremely "
            "strong, so even light cannot escape."
        )

    # Event horizon
    if "event horizon" in message:
        return (
            "The event horizon is the boundary around a black hole "
            "beyond which nothing can escape."
        )

    # Singularity
    if "singularity" in message:
        return (
            "A singularity is a region at the center of a black hole "
            "where matter is compressed to an extremely high density."
        )

    # Formation
    if (
        "how are black holes formed" in message
        or "how black holes form" in message
    ):
        return (
            "Black holes can form when a very massive star runs out of "
            "fuel and collapses under its own gravity."
        )

    # Types
    if "types of black holes" in message:
        return (
            "The main types of black holes are stellar-mass black holes, "
            "intermediate-mass black holes, and supermassive black holes."
        )

    # Supermassive
    if "supermassive" in message:
        return (
            "Supermassive black holes are extremely massive black holes "
            "found at the centers of many galaxies."
        )

    # Light
    if "can light escape" in message or "light escape" in message:
        return (
            "No. Once light crosses the event horizon, "
            "it cannot escape the black hole."
        )

    # Gravity
    if "gravity" in message:
        return (
            "A black hole has extremely strong gravity because a large "
            "amount of mass is concentrated in a very small region."
        )

    # Goodbye
    if message in ["bye", "goodbye"]:
        return "Goodbye! Keep exploring the universe. 🌌"

    # Wikipedia search
    try:
        search_results = wikipedia.search(message)

        if search_results:
            result = wikipedia.summary(
                search_results[0],
                sentences=2
            )
            return result

    except Exception:
        pass

    return (
        "Sorry, I couldn't find information about that. "
        "Try asking me about black holes, event horizons, "
        "singularities, gravity, or galaxies."
    )
    


if __name__ == "__main__":
    print(get_response("hello"))