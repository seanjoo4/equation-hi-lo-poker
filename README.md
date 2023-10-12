# equation-hi-lo-poker

## How to run server
1. python3 -m venv myenv
2. source myenv/bin/activate
3. pip install -r requirements.txt
4. python3 server/app.py
5. go to http://localhost:port/
6. deactivate to kill virtual environment

## Overview
Based on the Korean Netflix Gameshow: The Devil's Plan. Implemented this for fun, all credit to the tv show.

## Rules
1. You start off with three operator cards: +, -, /
2. At the start of the game the deck has 52 total cards:
    - number cards range from 0-10 and have four colors ranking from highest to lowest in the following order: gold, silver, bronze, and black
    - four multiplication cards
    - four square root cards
3. At the start of the first round, you will be given a hidden card(only you can see)
    - it will be a number card
4. Once you look at your card, two more cards will be given which everyone will be able to see
    - if a card is a multiplication card, you must discard an addition, subtraction, or multiplication card and will be given another number card
        - divison card cannot be discarded
    - if a card is a root card, you will be handed another number card
5. After all players get their cards, there are 4 rules for betting:
    - 1. there is a minimum bet of 1 chip
    - 2. a player can raise the chip count - if that is the case, everyone has to match this person
        - the maximum chip raise is the chip count of the player with the lowest amount of chips
    - 3. if you don't want to match the bet, you can fold
    - 4. you can also check, and not bet anything
6. after the initial betting round, every player will receive one new open number card
7. you can only root a single number
8. now all players will formulate an equation aiming for low(closest to 1) or high(closest to 20).
    - you can also pick to swing bet(aim for high and low) and formulate two equations
        - to win earnings, swing bets must win both high and low pots
    - equations can create negative numbers
9. one final betting round will start
10. Once the bets are completed, the players will reveal their formulas and their high and/or low choice
    - players will be against those who are betting for the same high/low option as them
11. The pot will be evenly split to the winner of the high and low pot
    - if equations come out to be the same value, then:
        - for the high pot: the person with the highest number in the equation wins
            - if the highest numbers are the same, then the player with the higher color wins
        - for the low pot: the person with the lowest number in the equation wins
            - if the lowest numbers are the same, then the player with the lower color wins
12. There will be 10 rounds or until there is one winner.
    - in the case of a tie at 10 rounds, it will be sudden death until one has more chips