"""Personalized welcome message."""


def welcome_message(first_name, greeting="Welcome"):
    """Return a welcome message for ``first_name``.

    Blank, empty, or whitespace-only names always fall back to
    "Welcome, Guest!", regardless of ``greeting``.
    """
    if first_name is None:
        return "Welcome, Guest!"

    name = first_name.strip()
    if not name:
        return "Welcome, Guest!"

    return f"{greeting}, {name}!"
