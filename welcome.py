"""Personalized welcome message."""


def welcome_message(first_name):
    """Return a welcome message for ``first_name``.

    Blank, empty, or whitespace-only names fall back to "Guest".
    """
    if first_name is None:
        return "Welcome, Guest!"

    name = first_name.strip()
    if not name:
        return "Welcome, Guest!"

    return f"Welcome, {name}!"
