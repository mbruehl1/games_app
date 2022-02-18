try:
    from cards import Cards
    from coin import Coin
    from dice import Dice
except ModuleNotFoundError:
    print("ERROR:  Required modules not found.  Please ensure all .py files are in same directory.")
    exit()
    
import csv


class Game:
    """ Play a game of chance with 3 modules"""

    def __init__(self):
        """ Create game objects and initialize variables"""
        self.deck_of_cards = Cards()
        self.coin = Coin()
        self.die = Dice()
        self.match_count = 0
        self.counter = 1

    def play(self):
        """ Execute the game mechanics"""
        # First open an output file to record results:
        try:
            out_file = open('GameResults.csv','w',newline='')
        except OSError:
            print("Unable to create the output file 'GameResults.csv'.  Please check directory or enable write permissions.")
            exit()
        # Create a CSV stream to the output file:
        csv_output = csv.writer(out_file)
        # Write the csv header fields to the results file:
        csv_output.writerow(["Iteration","DICE","CARD","COIN"])

        while self.match_count < 4:
            # match_count will reach 3 when all three conditions are met:
            self.match_count = 1
            
            # Draw a card and check if it matches a win condition:
            my_card = self.deck_of_cards.draw()
            if my_card == ("J-Spades" or "A-Diamonds"): self.match_count += 1
            
            # Flip a coin and check is matches the win condition:
            my_coin = self.coin.flip()
            if my_coin == "HEADS": self.match_count += 1
            
            # roll the die and check if it matches the win condition:
            my_die = self.die.roll()
            if my_die == 6: self.match_count += 1

            # Save the current tuple to a file:
            csv_output.writerow([self.counter,my_die,my_card,my_coin])
            self.counter += 1

        # Close the results file:
        out_file.close()
        print("Congratulations! You win!  See your run results in the file 'GameResults.csv'")

if __name__ == '__main__':
    """Enter main runtime to play the game"""
    game = Game()
    game.play()
    
