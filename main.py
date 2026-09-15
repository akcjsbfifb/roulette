import random


def bets_for_round(notebooks: list[list[int]]) -> list[int]:
    bets = [0] * 6
    for i in range(6):
        #If at some point the notebook is empty because he crossed out all the numbers, 
        #then he starts over with the initial sequence.
        if not notebooks[i]:
            notebooks[i] = [1, 2, 3, 4]
        nb = notebooks[i]
        if len(nb) > 1:
            bet = nb[0] + nb[-1]
        else:
            #If at some point he only has one number left,
            #that's his bet (he doesn't have to double it as if he was adding both extremes).
            bet = nb[0]

        # If the bet he needs to place is out of the table boundaries (max and min),
        # he starts over with the initial sequence.
        if bet < 5 or bet > 4000:
            notebooks[i] = [1, 2, 3, 4]
            bet = 5
        bets[i] = bet
    return bets


def main() -> None:
    notebooks = [[1, 2, 3, 4] for _ in range(6)]
    balances = [0] * 6
    winners = [[] for _ in range(37)]
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

    for number in range(37):
        if number == 0:
            continue
        won = [
            0 if number in red_numbers else 1,
            2 if number >= 19 else 3,
            4 if number % 2 == 1 else 5,
        ]
        winners[number] = won

    for _ in range(10000):
        n = random.randint(0, 36)
        bets = bets_for_round(notebooks)
        for j in range(6):
            if j in winners[n]:
                balances[j] += bets[j]
                notebooks[j].append(bets[j])
            else:
                balances[j] -= bets[j]
                # algo raro de slices  para sacar primer y ultimo elemento
                notebooks[j] = notebooks[j][1:-1]
        #print(n, balances, sum(balances))

    total = sum(balances)
    print(total)
    if total > 0:
        print("equipo gano")
    elif total < 0:
        print("equipo perdio")
    else:
        print("barke even")


if __name__ == "__main__":
    main()
