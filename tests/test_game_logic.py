from logic_utils import check_guess, new_game_state, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, it should report Too High
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, it should report Too Low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_hint_direction_bug_fixed():
    # Previously the hints were reversed; ensure the message matches outcome
    # high guess -> LOWER message, low guess -> HIGHER message
    high_outcome, high_msg = check_guess(99, 50)
    assert high_outcome == "Too High"
    assert "LOWER" in high_msg

    low_outcome, low_msg = check_guess(1, 50)
    assert low_outcome == "Too Low"
    assert "HIGHER" in low_msg

def test_new_game_resets_state():
    # State should be initialized when a new game begins
    state = {
        "secret": 999,
        "attempts": 7,
        "score": 42,
        "status": "lost",
        "history": [1, 2, 3],
    }
    new_game_state(state, "Easy")
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
    low, high = get_range_for_difficulty("Easy")
    assert low <= state["secret"] <= high
