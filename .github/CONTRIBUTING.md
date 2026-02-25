# Contributing to Tatetí Game

Thank you for your interest in contributing! This project was developed as a university assignment, but any improvements, bug fixes, or new ideas are more than welcome to make this classic game even more enjoyable.

## How to Contribute

1. **Fork** the repository.
2. Create your branch: `git checkout -b feature/new-functionality`.
3. Make your changes and commit them: `git commit -m "Add new functionality"`.
4. Push your branch: `git push origin feature/new-functionality`.
5. Open a **Pull Request**.

## Ideas for Contribution

- **New Game Modes:** Implement a "Best of 3" system or a simple AI (Player vs CPU) using the Minimax algorithm.
- **Visual Improvements:** Add animations when a player wins, customizable themes (dark mode), or different symbols for X and O.
- **Sound Effects:** Add feedback sounds for placing marks, winning, or drawing.
- **Code Refactoring:** Improve the structured programming logic or refactor the project to an Object-Oriented (OOP) approach.
- **UI Enhancements:** Create a main menu, a reset button within the interface, or a score tracker for the current session.

## Development Tips

- **Structured Logic:** This project currently follows structured programming principles. Try to keep the logic modular and clear within `src/tateti.py`.
- **Gamelib Events:** Pay close attention to how mouse click coordinates are mapped to the 3x3 grid cells in the `inter_gráfica.py` or main loop.
- **Winning Logic:** If you modify the win detection, ensure you test horizontal, vertical, and both diagonal conditions.

Thank you for your collaboration! 🎉
