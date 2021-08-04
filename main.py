import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Canned results
r = ["I drew rock... it's a tie", "I drew paper... I win", "I drew scissors... I lost"]
p = ["I drew rock... I lost", "I drew paper... it's a tie", "I drew scissors... I win"]
s = ["I drew rock... I win", "I drew paper... I lost", "I drew scissors... it's a tie"]
result = [r, p, s]

#player input
player = input("Ready for rock paper scissors? Rock... Paper... Scissors... Shoot!\n")
player = player.lower()

#computer randomly chooses
computer = random.randint(0,2)

#results
if player == "rock":
  print(f"You chose\n{rock}\n ROCK\n")
  print(result[0][computer])
elif player == 'paper':
  print(f"You chose\n{paper}\n PAPER\n")
  print(result[1][computer])
else:
  print(f"You chose\n{scissors}\n SCISSORS\n")
  print(result[2][computer])
