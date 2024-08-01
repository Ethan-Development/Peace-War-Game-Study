# Coded by Ethan Y, please do not use assets without written permission. Data findings is open source.

# This is a simulation of the peace war game. Find more information here:
# https://en.wikipedia.org/wiki/Peace_war_game

# Here is the powerpoint where I feature this code: https://docs.google.com/presentation/d/1L1T7BsVbefX_-UAzAVP8Lda_0lgQkYu4P_HkFIy9ACo/edit?usp=sharing

# <-- Page Break -->

import random

### Declare Variables

totalGames = []
totalPlayers = 2

startingResource = 2

minTurnsPerGame = 2
maxTurnsPerGame = 10

class player():
    def __init__(self, order, s_level, category):
    # Creating a player that keeps track of its order of play and satisfaction level (s_level). The category determines the type of player: Reciporical Altrism, Tit for Tat or Peace unless Agreesive. The last thing it checks is your move history.
        self.o = order
        self.s = s_level # Satisfaction of The Previous Tern
        self.c = category
        self.h = [] # History
        self.netEarnings = 0

    def decision(self):
        if currentTern == 1 and self.c != "PLA":
            d_randomizer = random.randint(0,1) # 0 is peace, 1 is war
            if d_randomizer == 0:
                self.action = d_randomizer; self.h.append(0) 
            if d_randomizer == 1:
                self.action = d_randomizer; self.h.append(1)
        elif currentTern == 1 and self.c == "PLA":
            self.action = 0; self.h.append(0)

        if currentTern > 1:
            self.netEarnings = self.netEarnings + self.s
            if self.c == "RA":
                if self.s == 0:
                    self.action = 0; self.h.append(0)
                if self.s > 0 or self.s == -2:
                    self.action = 1; self.h.append(1)
                if self.s == -1:
                    d_randomizer = random.randint(0,1)
                    self.action = d_randomizer
                    self.h.append(d_randomizer)
            if self.c == "TT":
                if self.s == 0 or self.s > 0:
                    self.action = 0; self.h.append(0)
                if self.s < 0:
                    self.action = 1; self.h.append(1)
            if self.c == "PLA":
                if self.s == 0 or self.s == 1:
                    self.action = 0; self.h.append(0)
                if self.s < 0:
                    self.action = 1; self.h.append(1)


def simulateGame():
    global currentTern
    currentTern = 1
    p1 = player(1, 0, "RA")
    p2 = player(2, 0, "RA")

    for _ in range(maxTurnsPerGame):
        p1.decision()
        p2.decision()

        # Evaluating Decisions and Selecting a Winner
        if p1.action == 0:
            if p2.action == 0:
                p1.s += 0; p2.s += 0;
            if p2.action == 1:
                p1.s -= 2; p2.s += 2;
        if p1.action == 1:
            if p2.action == 0:
                p1.s += 2; p2.s -= 2;
            if p2.action == 1:
                p1.s -= 1; p2.s -= 1;

        currentTern += 1

    # Return Results
    print("Test Complete! Here are the results:")
    print(f"""--------------------------
Type of Player:
P1 Type: {p1.c}
P2 Type: {p2.c}
--------------------------
Net Earnings:
P1 Net Earnings: {p1.netEarnings}
P2 Net Earnings: {p2.netEarnings}
--------------------------
Net History:
P1 Attack History: {p1.h.count(1)}
P1 Peace History: {p1.h.count(0)}

P2 Attack History: {p2.h.count(1)}
P2 Peace History: {p2.h.count(0)}
--------------------------
Full History (p1): {p1.h}
Full History (p2): {p2.h}
--------------------------""")




if __name__ == "__main__":
    simulateGame()
