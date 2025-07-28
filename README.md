# 🤖 Rock Paper Scissors AI (freeCodeCamp Challenge)

This is a machine learning-inspired Rock, Paper, Scissors bot built as part of the [freeCodeCamp Machine Learning curriculum](https://www.freecodecamp.org/).

The goal: **beat 4 advanced bots** with at least a 60% win rate over 1000 games.

---

## 🧠 How It Works

The core AI logic is implemented in `RPS.py`. It:
- Tracks opponent moves
- Learns patterns of up to 3-move sequences
- Counters the opponent’s most likely next move
- Uses fallback strategies when patterns are weak
- Adapts to beat bots like Quincy, Abbey, Kris, and Mrugesh

---

## 🧪 Win Rates

Against 1000 rounds each:

- ✅ Quincy: ~99%
- ✅ Abbey: ~60%+
- ✅ Kris: ~80%+
- ✅ Mrugesh: ~85%+

---

## 📁 File Overview

| File           | Purpose                                           |
|----------------|---------------------------------------------------|
| `RPS.py`       | Main AI logic for the player                     |
| `rps_game.py`  | Game engine and built-in opponent bots           |
| `test_module.py` | Automated unit tests (using `unittest`)       |
| `main.py`      | Entry point for running the game manually        |

---

## 🚀 Try It Yourself

```bash
# Run matches vs all bots
python main.py

# Run unit tests
python test_module.py
