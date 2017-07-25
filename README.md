# Plan for craps command line game

## Goal
- Create a game command line game that will allow multiple players to play craps

## Outline
- Multiple players join, each with a certain amount of money to start
- Code tells each player they're current pot and each player places a bet (ie an amount on a specific set of numbers (or a color) or can choose to sit out the round
- Code randomly selets a number, calculates and winnings/loss and lists the new amounts held by each player
- Each player has the chance to bet again, or to leave the game
- Game ends when one of these conditions is met
  - All players are out of money
  - All players have left the game
- At the end of the game name the player that left with the most money as the winner

## Coding notes
- Try to use classes as much as possible
  - Player class for each player
    - Attributes: Name[string], bet[2d array], pot[integer], initial pot
    - Methods: Place bet, Leave game, Calc winnins
  - Wheel class representing the Roullete wheel
    - Attributes: selection[integer]
    - Methods: spin
