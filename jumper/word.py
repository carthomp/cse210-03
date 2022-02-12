import csv
import random
from turtle import rt
       
class Word:

    def __init__(self):

        self.word_list = ["house","boy","girls","python"]
        self.random_word_number = random.randint(0,3)
        self.word = self.word_list[self.random_word_number]
        
    def set_word (self):
        return self.word

    def pick_word(self):

        # self.word=self.word_list[self.random_word_number]


        # with open ("./jumper/words.csv","rt") as csv_file:

        #     reader = csv.reader(csv_file)
        #     next(reader)
        #     for row in reader:
        #         self.word_list.append(row)

        #     # self.random_word_number = random.randint(0,len(self.word_list))
        #     # self.word = self.word_list[self.random_word_number]
        #     # self.word = self.word.strip()
        
        # self.word=random.choice(self.word_list)
        # self.word=self.word[0].upper()
            

        
