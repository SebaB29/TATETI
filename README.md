# ❌⭕️ Tatetí Game

Welcome to **Tatetí**, a classic implementation of the iconic Tic-Tac-Toe game in Python. Challenge a friend in this two-player local game where strategy and quick thinking determine who gets three marks in a row first.

# 📸 Demo
<div align="center">
    <img alt="Tatetí Gameplay" src="img/tateti.jpg" width="350px">
    <img alt="Winner Screen" src="img/ganador.jpg" width="350px">
</div>

# 📍 Table of Contents
- [📝 Description](#-description)
  - [🧩 Key Features](#-key-features)
  - [🧱 Project Structure](#-project-structure)
  - [🛠️ Technologies](#️-technologies)
- [🚀 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [⚙️ Installation](#️-installation)
- [💡 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

# 📝 Description
This project focuses on **structured programming** and graphical event handling. It provides a clean, 3x3 grid interface where players can interact via mouse clicks to compete in a local multiplayer environment.

## 🧩 Key Features
- **Local Multiplayer:** Smooth turn-based system for two players.
- **Win Detection:** Automatic detection of horizontal, vertical, and diagonal win conditions.
- **Draw Logic:** Smart detection for "Cats Game" (draw) when the grid is full.
- **Intuitive UI:** Clean graphical rendering using mouse-click coordinates.

## 🧱 Project Structure
```text
Tateti/
├── graphics/    # Rendering logic and gamelib integration
├── img/         # Gameplay screenshots
├── src/         # Core game mechanics (tateti.py)
├── main.py      # Application entry point
└── LICENSE      # MIT License
```

## 🛠️ Technologies
* **Python 3.x**
* **Gamelib**: A lightweight thread-based rendering library for Python interfaces.

# 🚀 Getting Started
## 📋 Prerequisites
* Python 3.10 or higher installed on your system.

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/SebaB29/tateti.git](https://github.com/SebaB29/tateti.git)
   cd tateti
   ```

# 💡 Usage
To start the game, simply run the main script:
```bash
python main.py
```

1. The game starts with Player 1 (❌).
2. Click on any empty cell of the 3x3 grid to place your mark.
3. The game will automatically switch to Player 2 (⭕️).
4. The first player to get 3 marks in a row wins!

# 🤝 Contributing
1. Fork the project.
2. Create your Feature Branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the Branch (git push origin feature/AmazingFeature).
5. Open a Pull Request.

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
