# Monopoly'

To Dos:
- Create basic trade logic (game.end_turn())
- Simulate aggression


Key Assumptions:

Purchasing Logic:
- Players will purchase any unowned property they land on, assuming they have sufficient funds.

End of turn logic: while a player stays above a limit set by their aggressiveness trait,
1. First unmortage any monopolies they have, going from most least expensive4 to most expensive monopoly
2. Purchase as many houses/hotels as possible, going from most expensive to least expensive monopoly
3. Unmortage as many other properties as possible, going from most expensive to least expensive property

Jail Logic:
- Players will attempt to leave jail as quickly as possible, whether through using a Get out of Jail Free Card or paying $50

Liquidation Logic: In the case where players do have not enough cash to cover a debt, assets will be liquidated in the order:
1. Non-monopoly properties, from least worth to most worth
2. Monopoly properties, set by set
    - Monopolies with the least number of houses (measured by the property within each monopoly with the most houses)
    - A monopoly is fully liqudated (all properties are mortaged) before the next set is liqudated

Bankruptcy Logic: A player only recieves the proceeds of a Bankruptcy if they are the sole contributor to that bankruptcy. If not, 
the bank will recieve the assets.

Otherwise, standard monopoly rules (https://www.hasbro.com/common/instruct/00009.pdf)