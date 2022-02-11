import csv
import random
       
class Word:

    def _init_(self):

        self.word_list = []
        self.random_word_number = random.randint(0,1831)
        with open ("word.csv") as csv_file:

            reader = csv.reader(csv_file)
            for row in reader:
                self.word_list.append(row)

            self.random_word_number = random.randint(0,len(self.word_list))
            self.word = self.word_list[self.random_word_number].strip()
            
    def set_word (self):
        return self.word

    def pick_word(self, current_word):
        self.word = current_word

        
