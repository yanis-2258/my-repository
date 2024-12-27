
'''  this  game is a multiplayer game  with a dice ,
if you got a +1 your score ganna be refreshed to 0 otherwise you won if your score reashed the maxscore which is
 50 before the other player'''

import random 

def roll():
  min_number = 1 
  max_number = 6 
  roll = random.randint(min_number,max_number)

  return roll


value=roll()


 #players loop
while True:
  player=input("inter number of players(2_4)  " )
  if player.isdigit():
    player=int(player)
    if 2<=player<=4:
      break
  else:
    print("try again 'number' error ")


#game loop
max_score=50
player_score=[0 for _ in range(player)]

while max(player_score)< max_score: 


  for player_idx in range(player):
    print (f'\n player  { player_idx +1 } has to play\n')


    while max(player_score)< max_score:
     decision = input("do you want to roll the dice ? (y/n)  ")
     current=0
     if decision.lower() !='y':
        break 
     else:
      value = roll()
      score=print(value) 

      if value ==1:
        print ("you rolled a 1 bonne chance next time !!")
        current ==0
        break
      else:
       current+=value
       player_score[player_idx]+=current
      print(f"player{player_idx +1} you gained  a : +{current}")
      print(f"your actual score is: {player_score[player_idx]}")
    print(f"your total score is {player_score[player_idx]}")
      
max_score  = max(player_score)      
winning_idx = player_score.index(max_score)
print(f"the winner is {player_idx } with a score of {max_score}")