import random

def bets_for_round(notebooks: list[list[int]]) -> list[int]:
    bets = [0] * 6
    for i in range(6):
        #Reset notebooks if empty
        if not notebooks[i]:
            notebooks[i] = [1, 2, 3, 4]
        nb = notebooks[i]
        if len(nb) > 1:
            bet = nb[0] + nb[-1]
        else:
            #If at some point he only has one number left, that's his bet.
            bet = nb[0]
        # If the bet he needs to place is out of the table boundaries (max and min),
        # he starts over with the initial sequence.
        if bet < 5 or bet > 4000:
            notebooks[i] = [1, 2, 3, 4]
            bet = notebooks[i][0] + notebooks[i][-1]

        bets[i] = bet
    return bets

def winners_per_number() -> list[list[int]]:
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    winners = [[] for _ in range(37)]

    # for each number 0-36, precalculates who wins (0 red, 1 black, 2 high, 3 low, 4 odd, 5 even)
    for number in range(37):
        if number == 0:
            continue
        won = [
            0 if number in red_numbers else 1,
            2 if number >= 19 else 3,
            4 if number % 2 == 1 else 5,
        ]
        winners[number] = won
    return winners

def main() -> None:
    notebooks = [[1, 2, 3, 4] for _ in range(6)]
    balances = [0] * 6

    winners = winners_per_number()

    for _ in range(10000):
        n = random.randint(0, 36)
        bets = bets_for_round(notebooks)
        for j in range(6):
            if j in winners[n]:
                # if player won, update his balance and add current bet to notebook
                balances[j] += bets[j]
                notebooks[j].append(bets[j])
            else:
                # update balance and delete first and last element of notebook
                balances[j] -= bets[j]
                if len(notebooks[j]) <= 2:
                    notebooks[j].clear()
                else:
                    del notebooks[j][0]
                    del notebooks[j][-1]

    total = sum(balances)
    print(total)
    if total > 0:
        print("equipo gano")
    elif total < 0:
        print("equipo perdio")
    else:
        print("broke even")


if __name__ == "__main__":
    main()
