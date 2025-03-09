    # TIC-TAC-TOE
    #### Video Demo:  <https://youtu.be/ySl1Bv_sqVc>
    #### Description:

# CS50’s Introduction to Programming with Python (Final Project)

This project is a **Tic-Tac-Toe** game where the user competes against the machine for the title of winner. It is a simple, fast, and easy-to-learn game, ideal for all ages, especially for children, as it does not cause overstimulation.  
The project was developed as part of the **CS50’s Introduction to Programming with Python** course, with the objective of applying programming concepts such as classes, inheritance, list manipulation, conditionals, and randomness.

---

## 📋 Code Structure

This code is organized as follows:

### 🔹 1. `Players` Class:
- This class stores the names of the players (machine and user) and uses the `random` library to determine who will go first.

### 🔹 2. `Display` Class:
- This class inherits from the `Players` class and is responsible for managing each player's moves and placing either 'X' or 'O' on the board.
- After every move, it calls a global function to check if there is a winner or if the game ended in a draw.

### 🔹 3. `check_winner` Function:
- This function checks if there is a winner. Eight different patterns are tested to see if three identical player symbols ('X' or 'O') align.
- If all the spaces are filled, but no winning pattern is found, the game ends in a draw.

### 🔹 4. `show_board` Function:
- This function converts the board (which is a list in the class) into a string to be displayed to the user.

### 🔹 5. `generate_board` Function:
- This function generates the default Tic-Tac-Toe board, which is a list of nine empty spaces ready to be filled with player symbols.

---

## 🧪 Tests

There is also a test code used to ensure the integrity of the game. The tests ensure that the three main functions work correctly. The test functions are:

1️⃣ **`test_validate_correct_board`**:  
- Validates that the board is correctly converted from a list to a string. Spaces must be placed correctly to keep the board well formatted.

2️⃣ **`test_check_for_winners`**:  
- Verifies that, when receiving certain board patterns, the `check_winner` function correctly identifies the winner. There are three game-ending patterns, and the function should return "Player", "Machine", or "draw".

3️⃣ **`test_generate_board`**:  
- Ensures that the board is always correctly generated before starting a game.

---

## 🚀 Future Improvements

Some ideas for future improvements include:

1. **Graphical User Interface (GUI)**:  
- Create a GUI using libraries like `Tkinter` or `Pygame` to provide a more interactive game experience.

2. **Difficulty Levels**:  
- Implement difficulty levels to bring a more challenging experience for the player.

3. **Local Multiplayer Mode**:  
- Add the ability for two human players to play locally and have fun together.

4. **Scoring System**:  
- Implement a scoring system that tracks the player's performance over time, including wins, losses, and statistics.

5. **Improved AI**:  
- Implement a more natural AI to create a more challenging game experience.

---

## 📜 License

This project is licensed under the **MIT License**, allowing for modification and distribution.
