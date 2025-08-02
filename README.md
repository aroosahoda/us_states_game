# 🗺️ States Game

An interactive U.S. geography quiz built with Python, Turtle graphics, and Pandas. The goal is to name all 50 U.S. states, and see them appear on a map as you go!

## 🎮 Gameplay

- The game displays a map of the United States.
- You're prompted to guess state names one at a time.
- Correct guesses appear in their geographical positions on the map.
- Type `Exit` to quit anytime—un-guessed states will be saved in a CSV for further study.

## 📦 Project Structure

```
states-game/
│
├── main.py                  # Main game logic
├── 50_states.csv            # Contains state names and x-y coordinates
├── us_states.gif            # Background image of the U.S.
└── states_to_learn.csv      # Auto-generated list of missed states
```

## 🛠 Requirements

- Python 3.x
- `turtle` (standard Python library)
- `pandas` library

Install `pandas` using pip:

```bash
pip install pandas
```

## 🚀 Getting Started

1. Clone this repo or download the files.
2. Ensure all required files are in the same directory.
3. Run the game with:

```bash
python main.py
```

## 💡 Features

- Smart input handling (case-insensitive, auto-capitalized).
- Saves progress for continued learning.
- Fun and visual way to memorize U.S. states.

## 📚 Educational Use

Perfect for students, educators, or curious minds looking to learn U.S. geography through play.

---

Feel free to fork, improve, or remix this project! If you'd like a badge section or a license snippet, I can add that too.
``` 
