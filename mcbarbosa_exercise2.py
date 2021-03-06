""" Aling Nena's Reward System Challenge
Author:
Description: This summer, Aling Nena’s Sari-sari store wants to implement a
reward system where customers can redeem a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>

>> Please enter text: 1 nicole i. tibay f

The system will then reply the following:
Hi <Customer’s name first letters upper case>! You have successfully redeem
reward #<reward number> - <reward>! Thank you for choosing Aling Nena’s
Sari-sari store.

>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank you for choosing Aling Nena’s Sari-sari store.
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
rewards = [
    "Coke sakto",  # index 0
    "Boy Bawang",  # index 1
    "15pcs. Yucky candy",  # index 2
    "15pcs. Pintura candy",  # index 3
    "15PHP load",  # index 4
    "3 pcs. Dove conditioner",  # index 5
    "Cottonbuds",  # index 6
    "One sheet of Biogesic",  # index 7
    "100mL Pepper/Pintura",  # index 8
]
data = input('Please enter text: ')
break_data = data.split(' ')
reward_number = break_data[0]
reward_value = rewards[int(reward_number) - 1 ]
name = '{} {} {}'.format(break_data[1], break_data[2], break_data[3])
gender = break_data[4]
print(f'Hi {name} You have successfully redeem reward #{reward_number} - {reward_value}! \nThank your for choosing Aling Nena’s Sari-sari store')