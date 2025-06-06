# My Python Desktop Games Collection

Welcome to my personal collection of classic desktop games! This project is a fun exploration of building simple, standalone desktop applications using Python for the backend logic and web technologies (HTML/CSS) for the user interface.

## About The Project

The goal of this repository is to create a series of self-contained games that are easy to run and fun to play. Each game is built with a consistent technology stack, making it a great way to practice and showcase development skills.

---

### Core Technologies

This project is powered by a combination of modern and flexible tools:

* **Python:** For all backend logic and game state management.
* **Flask:** A lightweight web framework to serve the UI and handle requests.
* **pywebview:** A fantastic library that wraps the Flask app in a native desktop window.
* **HTML & CSS:** For creating beautiful, colorful, and interactive user interfaces.

---

## Games Collection

Here are the games currently available in this collection.

### 🎮 Tic-Tac-Toe

A colorful and modern take on the classic two-player game. Features a dynamic UI, custom player names, and a celebratory confetti animation for the winner.

![Tic-Tac-Toe Screenshot](https://placehold.co/600x400/667eea/ffffff?text=Tic-Tac-Toe+Game)

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3 installed on your system.

### Installation & Setup

1.  **Clone the repository** (or simply have your `GAMES` folder ready).

2.  **Create and activate a virtual environment** in your terminal. This keeps the project's dependencies separate.
    ```bash
    # Create the virtual environment
    python -m venv .venv

    # Activate it (on Windows)
    .venv\Scripts\activate

    # Activate it (on Mac/Linux)
    source .venv/bin/activate
    ```

3.  **Install the required packages** from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

### How to Run a Game

1.  Navigate to the specific game's folder in your terminal.
    ```bash
    # Example for Tic-Tac-Toe
    cd TicTacToe
    ```
2.  Run the main Python script. A desktop window will open with the game.
    ```bash
    python run_game.py
    ```

---

## Contributing

This is a personal project, but ideas and suggestions are always welcome! Feel free to fork the repository and experiment with your own game ideas.
