# Tatetí Game ❌⭕️

Welcome to **Tatetí**, a classic two-player game where the objective is to get three of your marks in a row on a 3x3 grid. This project is an implementation of the Tatetí game in Python, utilizing structured programming principles.

## 📜 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Symbols](#game-symbols)
- [Images](#images)
- [File Structure](#file-structure)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)
- [About This Project](#about)

## 🕹️ Features <a name="features"></a>

- Classic Tatetí gameplay with a 3x3 grid
- Two-player mode (Player vs Player)
- Graphical interface with intuitive controls
- Detects win conditions and draws

## 🚀 Installation <a name="installation"></a>

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SebaB29/tateti.git
   ```

2. Navigate to the project directory:
   ```bash
   cd tateti
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 Usage <a name="usage"></a>

To play the game, simply click on the grid to place your mark (❌ or ⭕️) in an empty cell. The game alternates between the two players until one player wins or the game ends in a draw.

## ⚙️ Game Symbols <a name="game-symbols"></a>

- **Player 1**: "❌" (X)
- **Player 2**: "⭕️" (O)

## 📷 Images <a name="images"></a>

<div style="display: flex;">
    <img alt="Img Tatetí" src="img/tateti.jpg" width="400px" height="400px">
    <img alt="Img Ganador" src="img/ganador.jpg" width="400px" height="400px">
</div>

## 📁 File Structure <a name="file-structure"></a>

The project structure is as follows:

```
Tateti/
├── graphics/
│   ├── gamelib.py
│   └── inter_gráfica.py
├── img/
│   └── [2 demo images of the game]
├── src/
│   └── tateti.py
├── main.py
├── LICENSE
├── README.md
└── .gitignore
```

- **graphics/**: Contains libraries for rendering the game (gamelib and graphical logic).
- **img/**: Includes demo images showcasing the game's functionality.
- **src/**: Contains the source code file for game logic (tateti).
- **main.py**: The entry point of the application.

## 🛠️ Technologies <a name="technologies"></a>

This project is built with:

- Python
- [Gamelib](https://github.com/dessaya/python-gamelib) (A library created by the instructor to facilitate the use of threads and rendering for the interface)

## 🤝 Contributing <a name="contributing"></a>

Contributions are welcome! If you'd like to improve the game, feel free to fork the repository and submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 📄 License <a name="license"></a>

Distributed under the MIT License. See `LICENSE` for more information.

## 📚 About This Project <a name="about"></a>

This project is an implementation of the classic Tatetí game in Python, focusing on game logic and graphical interface through structured programming principles.
