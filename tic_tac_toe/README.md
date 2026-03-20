# TicTacToe Game

Console-based TicTacToe game written in Python using Object-Oriented Programming and design patterns.

## Features
- Human vs Human
- Human vs Bot
- Easy Bot (random moves)
- Medium Bot
- Hard Bot (Minimax algorithm)

## AI (Minimax Algorithm)
The Hard Bot uses the Minimax algorithm to choose the best possible move.

- The algorithm simulates all possible future moves
- It assumes the opponent plays optimally
- It chooses the move that maximizes its chance of winning

Scores:
- Win → +1
- Loss → -1
- Draw → 0

## Architecture
The project is structured:

- Board → handles game state
- Rules → game logic (win, draw)
- Game → game loop
- Player / Factory → player creation
- BotStrategy → bot behavior (Strategy Pattern)
- Menu → user interaction

## Design Patterns
- Strategy Pattern → bot behaviors (Easy, Medium, Hard)

The Strategy Pattern is used to define different bot behaviors.
Each bot (Easy, Medium, Hard) implements its own move logic,
and the game can switch between them without changing the core logic.


## How to Run
```bash
python main.py
```