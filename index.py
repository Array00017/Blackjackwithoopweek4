## Python Blackjack
#For this project you will make a Blackjack game using Python. Click <a href="http://www.hitorstand.net/strategy.php">here</a> to familiarize yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

### Rules:

#`1. ` The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13. <br>
#**Note: No wildcards will be used in the program**

#`2. ` When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
 
`#3. ` The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.

`#4. ` If the dealer deals the Player cards equal to 21 on the **first** deal, the Player wins. This is referred to as Blackjack. Blackjack is **NOT** the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.

`#5. ` The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust. 

class card:


    deck = []
    suit = ["spade" "hearts" "dimonds" "clubs"]
    face = ["king" "queen" "jack" "Ace"]
    value = ["10" "10" "10" "11" "1" "2" "3" "4" "5" "6" "7" "8" "9"]



    def __player__(self,player):
        self.player = player 
        print input("what is your name")

    def __init__(self,suit,face,value,is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace


    def __shuffledeck__(self,deck,suit,face,value,):
        
        for x in deck.append(suit,face,value)
        if deck.apppend (randint.in range len(suit,face,value,))
        print (f"Dealer ready to deal")



    def __dealingcards__(self,deck,suit,face,value):

        twocards = []
        if deck == suit("") and face("") and value ("")
        twocards = deck.append(randint.in[1:52](2))
        print(twocards)

    def __addingcount__(self,value):
        for x in value += ("")
        if value("") > "21"
        print(f"bust")
    
    def __hitme__(self,deck,player,twocards)
        
        for x in deck 
        if player input("hitme") 
        print(twocards)


    def __standing__(self,player):
        if player input("stand")
        print (f"ok")

    def __blackjack__(self,value):

        if value == "21"
        print (f"blackjack, great game!")
        
    def __ingamewin__(self,dealer,player,cards):
        self.dealer = dealer
        self.player = player
        self.cards = cards
        
        if dealer.cards > player.cards
        print (f"delaer wins")
        else:
        print (f"blackjack")






        













        



        







        



        
