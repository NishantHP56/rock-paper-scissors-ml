import random
from collections import Counter

opponent_history = []
my_history = []

BEATS = {'R': 'P', 'P': 'S', 'S': 'R'}
BEATEN_BY = {'R': 'S', 'P': 'R', 'S': 'P'}

learned_patterns = {}
SEQUENCE_LENGTH = 3
overall_move_counts = Counter()

# Rotation pattern to bait Kris
KRIS_BAIT_SEQUENCE = ['R', 'S', 'P']

def player(prev_play, opponent_history_arg=[]):
    global opponent_history, my_history, learned_patterns, overall_move_counts

    if not prev_play:
        opponent_history.clear()
        my_history.clear()
        learned_patterns.clear()
        overall_move_counts.clear()

    if prev_play:
        opponent_history.append(prev_play)
        overall_move_counts[prev_play] += 1

        if len(opponent_history) >= SEQUENCE_LENGTH:
            seq = tuple(opponent_history[-(SEQUENCE_LENGTH + 1):-1])
            next_move = opponent_history[-1]
            if seq not in learned_patterns:
                learned_patterns[seq] = Counter()
            learned_patterns[seq][next_move] += 1

    my_next_move = random.choice(['R', 'P', 'S'])

    # --- 1. Pattern Learning ---
    if len(opponent_history) >= SEQUENCE_LENGTH:
        last_seq = tuple(opponent_history[-SEQUENCE_LENGTH:])
        if last_seq in learned_patterns:
            predicted = learned_patterns[last_seq].most_common(1)[0][0]
            my_next_move = BEATS[predicted]
            my_history.append(my_next_move)
            return my_next_move

    # --- 2. Quincy Detection ---
    if len(opponent_history) >= 6:
        last_6 = opponent_history[-6:]
        if last_6 == ['R', 'P', 'S', 'R', 'P', 'S']:
            predicted = {'R': 'P', 'P': 'S', 'S': 'R'}[opponent_history[-1]]
            my_next_move = BEATS[predicted]
            my_history.append(my_next_move)
            return my_next_move

    # --- 3. Kris Detection + Bait Trap ---
    if len(my_history) >= 3 and opponent_history[-1] == my_history[-3]:
        # We're in Kris territory — use bait loop to control him
        bait_move = KRIS_BAIT_SEQUENCE[len(my_history) % 3]
        predicted_copy = my_history[-2]  # What Kris will likely copy
        my_next_move = BEATS[predicted_copy]  # Beat what he's about to copy
        my_history.append(my_next_move)
        return my_next_move

    # --- 4. Abbey Handling ---
    if len(my_history) > 0: # We need at least one of our moves in history
        my_last_move = my_history[-1]
        return my_next_move

    # --- 5. Mrugesh Counter ---
    if len(my_history) >= 5:
        freq = Counter(my_history)
        common = freq.most_common(1)[0][0]
        my_next_move = BEATS[common]
        my_history.append(my_next_move)
        return my_next_move

    # --- 6. Most Frequent Opponent Counter ---
    if len(overall_move_counts) > 0:
        common = overall_move_counts.most_common(1)[0][0]
        my_next_move = BEATS[common]
        my_history.append(my_next_move)
        return my_next_move

    # --- 7. Fallback Random ---
    my_next_move = random.choice(['R', 'P', 'S'])
    my_history.append(my_next_move)
    return my_next_move
