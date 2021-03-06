from deck_of_cards import deck_of_cards

# creating picture path
suits_set = {0: "S", 1: "H", 2: "D", 3: "C"}
ranks = {1: "A", 11: "J", 12: "Q", 13: "K"}


class ride_the_bus_game:
    suits = {"S": 0, "H": 1, "D": 2, "C": 3}
    black_cards = [0, 3]
    red_cards = [1, 2]
    suits_set = {0: "S", 1: "H", 2: "D", 3: "C"}
    ranks = {1: "A", 11: "J", 12: "Q", 13: "K"}

    def __init__(self):
        self.table = []
        self.number_decks = 0
        self.trys = 1
        self.deck_obj = deck_of_cards.DeckOfCards()

    """
    chooseRed is True for Red
    chooseRed is False for Black
    """

    def black_or_red(self, chooseRed):
        if chooseRed and self.table[0].suit in self.red_cards:
            return True
        elif not chooseRed and self.table[0].suit in self.black_cards:
            return True
        else:
            self.table.clear()
            self.trys += 1
            return False

    """
    chooseHigher is True for higher
    chooseHigher is False for lower
    """

    def higher_or_lower(self, chooseHigher):
        if self.table[0].value < self.table[1].value and chooseHigher:
            return True
        elif self.table[0].value > self.table[1].value and not chooseHigher:
            return True
        else:
            self.table.clear()
            self.trys += 1
            return False

    """
    choice is 0 it is inbetween
    choice is 1 it is outside
    choice is 2 it is posts
    """

    def inbetween_outside(self, choice):
        if self.table[0].value > self.table[1].value:
            higher = self.table[0].value
            lower = self.table[1].value
        elif self.table[0].value < self.table[1].value:
            higher = self.table[1].value
            lower = self.table[0].value
        if self.table[2].value > lower and self.table[2].value < higher and choice == 0:
            return True
        elif (self.table[2].value < lower or self.table[2].value > higher) and choice == 1:
            return True
        elif self.table[2].value == lower and self.table[2].value == higher and choice == 2:
            return True
        else:
            self.table.clear()
            self.trys += 1
            return False

    """
    choice is 0 for Spades
    choice is 1 for Hearts
    choice is 2 for Diamonds
    choice is 3 for Clubs
    """

    def suit(self, choice):
        if self.table[3].suit == choice:
            return True
        else:
            self.table.clear()
            self.trys += 1
            return False

    def draw_card(self):
        if len(self.deck_obj.deck) == 0:
            self.deck_obj = deck_of_cards.DeckOfCards()
            self.number_decks += 1
        card = self.deck_obj.give_random_card()
        card.image_path = "./PNG/" + \
            str(card.rank if ranks.get(card.rank) is None else ranks.get(
                card.rank)) + suits_set.get(card.suit) + ".png"
        if card.rank == 1:
            card.value = 14
        return card

    def ride_the_bus(self):
        playing = True
        while playing:
            self.table.append(self.draw_card())
            print(self.table[0].name)
            print(self.table[0].image_path)
            if(self.black_or_red(False)):
                self.table.append(self.draw_card())
                print(self.table[1].name)
                print(self.table[1].image_path)
                if(self.higher_or_lower(True)):
                    self.table.append(self.draw_card())
                    print(self.table[2].name)
                    print(self.table[2].image_path)
                    if(self.inbetween_outside(0)):
                        self.table.append(self.draw_card())
                        print(self.table[3].name)
                        print(self.table[3].image_path)
                        if(self.suit(self.suits.get("H"))):
                            playing = False
        print("got off bus after " + str(self.number_decks) +
              " decks and " + str(self.trys) + " trys")


if __name__ == "__main__":
    game = ride_the_bus_game()
    game.ride_the_bus()
