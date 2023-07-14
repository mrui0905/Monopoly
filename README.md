# Monopoly

This repository includes a simulation of Monopoly and three studies into optimal monopoly strategy.

All studies are done in .ipynb files, the game engine is written in .py files, and data referenced in studies is 
stored in data folder

**Instructions**

When not intending to simulate (the main() method in init.py should be called without parameters), you will be prompted for the following:
- Number of players. If single-player mode, the user will always be Player 1.
- Gamemode (0 is simulation mode, 1 is single-player mode)
- Aggression level- determines how aggressive CPU will be regarding trades and purchasing houses/properties. Can be custom set when simulating,
but defaults to Default (0.5), Aggressive (0.85), and Conservative (0.15).

**Findings**

The studies were conducted to analyze the expected ROI (return on investment) of every possible decision a player may make (purchasing properties, building houses, etc.). Further studies
analyze the winning percentage of aggression levels, concluding that players are overall better off playing rather conservatively. The optimal aggression level is determined
using a neural network trained to model win percentages of players given their aggression level.

1 million+ simulations were conducted to create data used to conduct studies and train models.

**Key Monopoly Assumptions:**

CPU/Simulation Purchasing Logic:
- Players will purchase any unowned property they land on, assuming they have sufficient funds.

End of turn logic: while a player stays above a limit set by their aggressiveness trait,
1. Conduct any possible trades
2. First unmortage any monopolies they have, going from most least expensive to the most expensive monopoly
3. Purchase as many houses/hotels as possible, going from most expensive to least expensive monopoly
4. Unmortage as many other properties as possible, going from most expensive to least expensive property

Trade Logic:
- Players will only conduct a trade if at least one side can complete a monopoly. If only one side can complete a monopoly, the trade value
needed to complete the deal will be substantially higher than if both players would complete a monopoly.

Jail Logic:
- Players will attempt to leave jail as quickly as possible, whether through using a Get out of Jail Free Card or paying $50

Liquidation Logic: In the case where players do have not enough cash to cover a debt, assets will be liquidated in the order:
1. Non-monopoly properties, from least worth to most worth
2. Monopoly properties, set by set
    - Monopolies with the least number of houses (measured by the property within each monopoly with the most houses)
    - A monopoly is fully liquidated (all properties are mortgaged) before the next set is liquidated

Bankruptcy Logic: A player only receives the proceeds of a Bankruptcy if they are the sole contributor to that bankruptcy. If not, 
the bank will receive the assets.

Otherwise, standard monopoly rules (https://www.hasbro.com/common/instruct/00009.pdf) apply and players are assumed to make logical
decisions.
