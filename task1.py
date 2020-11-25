import datetime
from random import shuffle
import random

# task 1

# class Clock:
#     """Текущее время"""
#     def time(self):
#         print(datetime.datetime.now())

# class Alarm:
#     """Включение и выключение будильника"""
#     def alrm(self):
#         Alarm.alarm = True
#         print('alarm turn on')
#     def ofalarm(self):
#         Alarm.alarm = False
#         print('alarm turn off')

# class AlarmClock(Clock, Alarm):
#     """При вызове включается будильник"""
#     def clock(self, d=0, h=0, m=0):
#         # print('turn on')
#         tm = datetime.datetime.now()
#         if str(tm.hour) == h and str(tm.minute) == m and str(tm.day) == d:
#                 print('aaaaaaa')

# co = Clock()
# co.time()
# c = Alarm()
# c.alrm()
# cl = AlarmClock()
# cl.clock(d='24',h='15',m='12')


# task 2

# class Coder:
#     experience = 0
#     count_code_time = 0

#     def get_info(self):
#         pass

#     def coding(self):
#         pass


# class Backend(Coder):

#     def init(self, languages_backend):
#         self.experience = languages_backend

#     def get_info(self):
#         print(f'время выполнения кода {self.count_code_time}с')

#     def coding(self, time):
#         self.count_code_time += time

# class Frontend(Coder):

#     def init(self, languages_frontend):
#         self.experience = languages_frontend

#     def get_info(self):
#         print(f'время выполнения кода {self.count_code_time}с')

#     def coding(self, time):
#         self.count_code_time += time


# class FullStack(Frontend, Backend, Coder):
#     def init(self, languages_frontend):
#         self.experience = languages_frontend

# fs = FullStack()
# fs.coding(0.536)
# fs.get_info()


# task 3

# class Deck:
#     cards = [(suit, value) for suit in ['червы', 'бубны', 'трефы', 'пики'] for value in [str(i) for i in range(2, 11)] + list("JKQA")]

#     class Card:
#         def deal(self):
#             card = random.choice(Deck.cards)
#             print(f"карты {card} в колоде карт больше нету")
#             crd = Deck.cards.index(card)
#             del(Deck.cards[crd])

#         def mix(self):
#             Deck.cards = [(suit, value) for suit in ['червы', 'бубны', 'трефы', 'пики'] for value in [str(i) for i in range(2, 11)] + list("JKQA")]
#             random.shuffle(Deck.cards)


# card = Deck.Card()
# card.deal()
# print(Deck.cards)
# card.mix()


# task 4 

# def hackerrankInString(s):
#     target = 'hackerrank'
#     n = len(target)
    
#     i = 0
#     for char in s:
#         if char == target[i]:
#             i += 1
#             if  i == n:
#                 return 'YES'
#     return 'NO'











