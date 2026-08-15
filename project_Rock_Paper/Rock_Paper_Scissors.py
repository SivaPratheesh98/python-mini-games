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

import random
my_list=[rock,paper,scissors]
my_selection=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
print(my_list[my_selection])

computer_list=[rock,paper,scissors]
computer_choice=random.randint(0,2)
print(computer_list[computer_choice])
if my_selection==computer_choice :
    print("play once more")
elif my_selection==0 and  computer_choice==1:
    print("you lose")
elif my_selection==2 and  computer_choice==1:
    print("you win")
elif my_selection==1 and  computer_choice==2:
    print("you lose")
elif my_selection==2 and computer_choice== 0:
    print("you lose")
elif my_selection == 1 and computer_choice == 0:
    print("you win")
else :
    print("you have selected inappropriate")