import random

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    The boundaries mirror those in the Streamlit application.  Tests rely on
    this to verify secret values are within expected ranges.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def new_game_state(state: dict, difficulty: str):
    """Reset the given session-state dict for a new game.

    This mirrors the logic in the Streamlit app's `if new_game` block.
    It is useful for testing that all relevant fields are cleared and the
    secret value lies within the correct range for the chosen difficulty.
    """
    low, high = get_range_for_difficulty(difficulty)
    state["secret"] = random.randint(low, high)
    state["attempts"] = 0
    state["score"] = 0
    state["status"] = "playing"
    state["history"] = []


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # replicate the logic from app.py with correct hint directions
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
