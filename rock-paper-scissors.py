# import random module for the rock_paper_scissors game
import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    # Initialize instance of Player
    def __init__(self):
        # Player's own score
        self.score = 0
        # Player's own move
        self.mov = ''

    # Player chooses a move
    def move(self):
        # Always return "rock"
        self.mov = 'rock'
        return self.mov

    # Placeholder function to learn the opponent's move
    def learn(self, first_player_move):
        pass

    # Check if user's move beats opponent's move
    def beats(self, opponent_move):
        return ((self.mov == 'rock' and opponent_move == 'scissors') or
                (self.mov == 'paper' and opponent_move == 'rock') or
                (self.mov == 'scissors' and opponent_move == 'paper'))


class RandomPlayer(Player):

    # Initialize instance of RandomPlayer
    def __init__(self):
        # Access the  initializer of super class "Player"
        super().__init__()

    # Make the choice to move
    def move(self):
        # Make random selection of move and return the result
        self.mov = random.choice(moves)
        return self.mov

    # Placeholder function to learn the opponent's move
    def learn(self, first_player_move):
        pass

    # Check if user's move beats opponent's move
    def beats(self, opponent_move):
        return ((self.mov == 'rock' and opponent_move == 'scissors') or
                (self.mov == 'paper' and opponent_move == 'rock') or
                (self.mov == 'scissors' and opponent_move == 'paper'))


class ReflectPlayer(Player):

    # Initialize instance of ReflectPlayer
    def __init__(self):
        # Access the  initializer of super class "Player"
        super().__init__()
        # Initialize variable used to learn opponent's move
        # with an empty string
        self.reflect_move = ''

    # Make a choice to move
    def move(self):
        # Provides self.reflect_move is empty, choose a move to take
        # Return the result
        if self.reflect_move == '':
            self.mov = random.choice(moves)
            return self.mov
        else:
            # Make self.reflect_move the value of the variable self.move
            # Return the result
            self.mov = self.reflect_move
            return self.mov

    # Learn opponent player's move
    def learn(self, first_player_move):
        self.reflect_move = first_player_move

    # Check if user's move beats opponent's move
    def beats(self, opponent_move):
        return ((self.mov == 'rock' and opponent_move == 'scissors') or
                (self.mov == 'paper' and opponent_move == 'rock') or
                (self.mov == 'scissors' and opponent_move == 'paper'))


class CyclePlayer(Player):

    # Initialize instance of CyclePlayer
    def __init__(self):
        # Access the  initializer of super class "Player"
        super().__init__()

    # Continuous cycle of move to be chosen
    def move(self):
        if self.mov == '':
            self.mov = 'rock'
            return self.mov
        if self.mov == 'rock':
            self.mov = 'paper'
            return self.mov
        if self.mov == 'paper':
            self.mov = 'scissors'
            return self.mov
        if self.mov == 'scissors':
            self.mov = 'rock'
            return self.mov

    # Placeholder function to learn opponent's move
    def learn(self, first_player_move):
        pass

    # Check if user's move beats opponent's move
    def beats(self, opponent_move):
        return ((self.mov == 'rock' and opponent_move == 'scissors') or
                (self.mov == 'paper' and opponent_move == 'rock') or
                (self.mov == 'scissors' and opponent_move == 'paper'))


class HumanPlayer(Player):

    # Initialize instance of HumanPlayer
    def __init__(self):
        # Access the  initializer of super class "Player"
        super().__init__()

    # Make a choice to move
    def move(self):
        while True:
            # Take user's mov
            self.mov = input("Rock, paper, scissors? > ").lower()
            # Verify if mov is in the list of 'moves' provided
            if self.mov in moves:
                return self.mov
                break

    # Placeholder function to learn opponent's move
    def learn(self, my_move, their_move):
        pass

    # Check if user's move beats opponent's move
    def beats(self, opponent_move):
        return ((self.mov == 'rock' and opponent_move == 'scissors') or
                (self.mov == 'scissors' and opponent_move == 'paper') or
                (self.mov == 'paper' and opponent_move == 'rock'))


class Game:

    # Initialize instance of Game
    def __init__(self, p1, p2):
        # Initialize the two player objects
        self.p1 = p1
        self.p2 = p2

    # When game ends, display winner to the console
    def winningPlayer(self):
        print("*** TOTAL SCORE ***")
        print(f"FIRST PLAYER: {self.p1.score}\nSECOND PLAYER: {self.p2.score}")
        if self.p1.score > self.p2.score:
            print("FIRST PLAYER WINS!")
        elif self.p1.score < self.p2.score:
            print("SECOND PLAYER WINS")
        else:
            print("IT WAS A TIE!")

    # When a round ends, check and display the winner to the console
    def checkWinningPlayer(self, value_1, value_2):
        if value_1 == value_2:
            print("** TIE **")
            print(f"""Score: First Player {self.p1.score}, """ +
                  f"""Second Player {self.p2.score}""")
        elif value_1:
            print("** FIRST PLAYER WINS **")
            self.p1.score += 1
            print(f"""Score: First Player {self.p1.score}, """ +
                  f"""Second Player {self.p2.score}""")
        elif value_2:
            print("** SECOND PLAYER WINS **")
            self.p2.score += 1
            print(f"""Score: First Player {self.p1.score}, """ +
                  f"""Second Player {self.p2.score}""")

    # Players play game round-by-round
    def each_game_round(self):
        # First Player plays game
        first_player_move = self.p1.move()
        # First Player's move displayed in the console
        print(f"You played {self.p1.mov}.")
        # Second Player plays game
        player_two_move = self.p2.move()
        # Learn First Player's move
        self.p2.learn(first_player_move)
        # Second Player's move displayed in the console
        print(f"Opponent played {self.p2.mov}.")
        # Check if first player beats second player
        bool1 = self.p1.beats(self.p2.mov)
        # Check if second player beats first player
        bool2 = self.p2.beats(self.p1.mov)
        # Check who won between the players
        self.checkWinningPlayer(bool1, bool2)

    # Print current status of game
    def game_start_end(self, status_of_game):
        print("====================")
        print("GAME " + status_of_game + "!")
        print("====================")

    # Play game based on number of rounds
    def play_game(self, roundsNumberToPlay):
        self.game_start_end('START')
        # Play the game in roundsNumberToPlay times
        for round in range(roundsNumberToPlay):
            print(f"Round {round + 1} --:")
            self.each_game_round()
        # Print game status
        self.game_start_end('ENDS')
        # Display the winner
        self.winningPlayer()


if __name__ == '__main__':
    # Empty list of opponent objects
    all_opponent_objects = []
    # Append all opponent player objects to the empty list
    all_opponent_objects.append(Player())
    all_opponent_objects.append(RandomPlayer())
    all_opponent_objects.append(ReflectPlayer())
    all_opponent_objects.append(CyclePlayer())
    while True:
        try:
            # Verify number of rounds to be played
            roundsNumberToPlay = input("How many rounds do you want to play? ")
            # Convert roundsNumberToPlay to an int
            convertNum = int(roundsNumberToPlay)
            if isinstance(convertNum, int):
                # Randomly choose an opponent player
                randomNumber = random.randint(0, 3)
                # Create a game object based on HumanPlayer and
                # randomly choosen object
                game = Game(HumanPlayer(), all_opponent_objects[randomNumber])
                # Start the game
                game.play_game(convertNum)
                break
        except ValueError:
            # User should choose the correct data type value
            print("Please enter the correct number of rounds!")
            continue
