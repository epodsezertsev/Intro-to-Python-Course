#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.next_move = "0"

    def learn(self, my_move, their_move):
        self.next_move = their_move

    def move(self):
        if self.next_move == "0":
            return random.choice(moves)
        else:
            return self.next_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move = "0"

    def learn(self, my_move, their_move):
        self.last_move = my_move

    def move(self):
        if self.last_move == "rock":
            return "paper"
        elif self.last_move == "paper":
            return "scissors"
        elif self.last_move == "scissors":
            return "rock"
        else:
            return random.choice(moves)


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Rock, paper, scissors? > ").lower()
            if human_move in moves:
                break
        return human_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.")
        print(f"Player 2 played {move2}.")
        if move1 == move2:
            print("** IT'S A TIE! **")
        else:
            if beats(move1, move2) is True:
                self.score1 += 1
                print("** PLAYER 1 WINS! **")
            elif beats(move1, move2) is False:
                self.score2 += 1
                print("** PLAYER 2 WINS! **")
        print(f"Score: Player 1: {self.score1}, Player 2: {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def announce_winner(self):
        if self.score1 > self.score2:
            print("** YOU ARE THE FINAL WINNER! **")
        elif self.score1 < self.score2:
            print("** PLAYER 2 IS THE FINAL WINNER! **")
        else:
            print("GAME TIED!")

    def get_rounds(self):
        while True:
            rounds = input("How many rounds would you like to play? > ")
            if rounds.isnumeric() is True:
                return int(rounds)

    def play_game(self):
        print("Game start!")
        rounds = self.get_rounds()
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        self.announce_winner()
        print("Game over!")


players = [Player(), ReflectPlayer(), RandomPlayer(), CyclePlayer()]


def play_again():
    while True:
        repeat = input("Would you like to play again? Yes or No > ").lower()
        if repeat == "yes":
            new_game = Game(HumanPlayer(), random.choice(players))
            new_game.play_game()
        elif repeat == "no":
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(players))
    game.play_game()
    play_again()
