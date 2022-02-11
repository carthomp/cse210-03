import csv
import random
       
class Word:

    def _init_(self):

        self.word_list = []
        self.random_word_number = random.randint(0,1831)
        self.word = ""
        
    def set_word (self):
        return self.word

    def pick_word(self):
        with open ("word.csv") as csv_file:

            reader = csv.reader(csv_file)
            for row in reader:
                self.word_list.append(row)

            self.random_word_number = random.randint(0,len(self.word_list))
            self.word = self.word_list[self.random_word_number]
            self.word = self.word.strip()
            

        
