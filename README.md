# Guess the Right Room Game

### Overview

The “Guess the Right Room” game provides players with a choice of difficulty levels, where they pick rooms and receive either bonuses or penalties based on their selections. The game features two difficulty modes: easy and hard.

### Features

The code includes the following functions:

	1.	main(): The main function of the game. It manages the flow by calling other functions to run the game. Players are prompted to select a difficulty level.
	2.	startgame(strt: str): This function sets the game difficulty based on player input. It also gives a brief description of the rules and instructions.
	3.	simplegame(): Implements the easy mode of the game. Players select rooms and receive bonuses or penalties, with the goal of reaching level 20.
	4.	hardgame(): Implements the hard mode, similar to simplegame(), but with additional rules such as rooms being removed as the game progresses.
	5.	choosedifficulty(difficulty: str): This function allows players to choose the difficulty level and starts the appropriate game mode.

#### Libraries Used

	•	random: Used for generating random numbers to determine room selections and outcomes.

### Gameplay

The game begins with the main() function, where players are prompted to choose a difficulty level: easy or hard. Players then pick rooms, with each choice leading to either bonuses or penalties.

#### Easy Mode (simplegame()):

	•	Players aim to reach level 20.
	•	They must avoid penalty rooms and try to gather bonuses to increase their score.

#### Hard Mode (hardgame()):

	•	Similar to easy mode, but the difficulty increases over time.
	•	Some rooms are removed as the player progresses, making choices more challenging.

### Controls and Rules:

	•	Players can choose to exit the game at any time by entering “0”.
	•	At certain milestones (such as reaching level 10), players are asked if they want to restart or continue.
	•	Room selection results in random bonuses or penalties using the random library. Some bonuses are multiplied, while penalties may halve the player’s score.
	•	The game ends either when a player reaches the maximum level or chooses to quit.

### How the Code Works:

In startgame(), the player selects a difficulty, and the game begins based on their input. If the player opts to exit by entering “0”, they are asked to confirm their choice. Depending on the level and bonuses accumulated, different prompts or bonuses are triggered. The core gameplay revolves around room selection, random outcomes, and progressing through levels.

Each room selection is processed by checking whether it matches the “losing” room, and penalties or bonuses are applied accordingly. The game ends when the player loses all points or reaches the highest level.
