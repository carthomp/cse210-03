import csv
import random

       
class Word:

    def _init_(self):     
        self._word_list = []
        self._word = ""
               
    def set_word (self):
        return self._word

    def pick_word(self):
        with open ("jumper\words.csv") as csv_file:
            reader = csv.reader(csv_file)
            self._word_list = list(reader)
            for row in reader:
                self._word_list.append(row)

            random_word_number = random.randint(0,len(self._word_list))
            self._word = self._word_list[random_word_number]
        

    
            
            