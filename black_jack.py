#black jack
#massive project number 2
import random
DECK =['A',1,2,3,4,5,6,7,8,9,10,'K','Q','J']
def round():
#classes
        class Player:
                def __init__(self,bet):
                    self.cards = []
                    self.bet = bet
        class Dealer:
            def __init__(self,*player_obj_list):
               self.cards = []
               self.players = [*player_obj_list]
               self.dealer_total = []


            def deal_cards(self):
               for num in range(2):
                   self.cards.append(random.choice(DECK))
                   for player in self.players:
                       player.cards.append(random.choice(DECK))
            def __str__(self):
                    return self.cards
            def show_cards(self,reveal):
                nums = len(self.players)
                players_cards = []
                for num in range(nums):
                    players_cards.append(self.players[num-1].cards)
                if reveal == False:
                        return f"""
                    Players cards : {players_cards}
                    Dealer cards : {self.cards[0]} ?
                        """
                else:
                     return f"""
                 Players cards : {players_cards}
                 Dealer cards : {self.cards}
                     """
            def stay_hit(self):
                    for player in self.players:
                       option = input('Do you wanna stay or wanna go for a hit?or you hit black jack(bj) : ').lower()
                       if option == 'hit':
                           ind = self.players.index(player)
                           self.players[ind-1].cards.append(random.choice(DECK))
                       elif option == 'bj':
                           print(f'Congratulbations player {self.players.index(player)+1} you get back twice as much as your inital bet from the dealer back that is {player.bet * 2}.')
                           self.players.remove(player)
            def calc(self):
                #first checking if dealer should get a card or # NOTE:
                dlr_total = 0
                for card in self.cards:
                    if card == 'A':
                        dlr_total += 1
                    if card == 'K' or card == 'Q' or card == 'J':
                        dlr_total += 10
                    if type(card) == int:
                        dlr_total += card
                if dlr_total +10 <=21:
                    dlr_total += 10
                if dlr_total <=16:
                    self.cards.append(random.choice(DECK))
                self.dealer_total.append(dlr_total)
                self.dealer_total.append(dlr_total > 21)
                return self.dealer_total

            def check_dealer_bust(self,total):
               if total > 21:
                     print(f'Holy crap! Dealer busted everyone gets twice as their inital bet back from the dealer.')
                     num = 1
                     for player in self.players:
                         print(f'Player {num} gets {player.bet * 2} dollars back from the dealer.')
                         players.remove(player)
                         num += 1
            def check_totals(self,dlr_total):
                print(dlr_total[0])
                if dlr_total[0] <= 16:
                    self.cards.append(random.choice(DECK))
                dlr_total = self.calc()
                if dlr_total[1] == True:
                   self.check_dealer_bust(dlr_total[0])
                else:
                   for player in self.players:
                       player.total = int(input('Enter the total with the preferred value of ace if there : '))
                       print(player.total)
                       if player.total < dlr_total[0]:
                           print(f'Woops you don\'t have a hand higher than the dealer\'s total.You are out from the game loosing your inital bet.')

                       else:
                           print(f'Whoa you have a hand higher than or equal to the dealer\'s total. You get 1.5 times your initial bet back from the dealer.{player.bet * 1.5}')
                   self.players.remove(player)

        #instantiating classes
        #main game function
        def game_start():
            num_of_players = int(input('Enter the number of players : '))
            players = []
            for num in range(num_of_players):
               players.append(Player(float(input('Place your bet : '))))
            dealer = Dealer(*players)
            dealer.deal_cards()
            print(dealer.show_cards(False))
            status = 'not-done'
            while status != 'done':
              dealer.stay_hit()
              print(dealer.show_cards(False))
              check = input('Does anyone wants to go for a hit again? (y/n) : ').lower()
              if check =='n':
                  status = 'done'
            print(dealer.show_cards(True))
            dealer_total = dealer.calc()
            dealer.check_totals(dealer_total)
        game_start()
        player_again = input('Wanna go for another round guys ? (y/n) : ').lower()
        if player_again == 'y' :
                    round()
round()
