# Minesweeper Game in Python

This Python program is an implementation of the classic game **Minesweeper**. Minesweeper is a single-player puzzle game where the player must uncover all empty cells in a grid while avoiding hidden mines.

## How to Play

1. **Game Grid**: The game grid is represented as a 2D list. Each cell can be either empty (represented as "-") or contain a mine (represented as "#").

2. **Rules**:
   - The objective is to uncover all empty cells without clicking on a mine.
   - Clicking on a mine results in losing the game.
   - The numbers displayed in empty cells indicate the count of adjacent mines.

3. **Game Mechanics**:
   - The program uses nested loops to iterate through each cell in the grid.
   - For each empty cell, it counts the number of adjacent mines by examining neighboring cells in all eight directions.
   - The count of adjacent mines is then displayed in the cell.
   - The game continues until all empty cells are uncovered or a mine is clicked.

## Getting Started

To run the Minesweeper game, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/minesweeper-python.git
   cd minesweeper-python
   ```

2. **Run the Game**:
   ```
   python minesweeper.py
   ```

3. **Play the Game**:
   - The game grid will be displayed in the terminal.
   - Use your input to uncover cells and avoid mines.

## Features

- Customizable grid size and mine density.
- A user-friendly interface for playing Minesweeper.
- Displays the count of adjacent mines for each cell.
- Supports interactive gameplay.

## Contribution

Contributions to this Minesweeper implementation are welcome! If you'd like to add new features, fix bugs, or improve the code, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the original repository.


Enjoy playing Minesweeper and have fun exploring the code! If you have any questions or suggestions, feel free to reach out.
