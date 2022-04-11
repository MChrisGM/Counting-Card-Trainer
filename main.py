from os import listdir
from os.path import isfile, join
import cv2
import random

cards_table = {
    '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':11,'queen':12,'king':13,'ace':14,'clubs':1,'clubs2':0,'diamonds':2,'diamonds2':0,'hearts':3,'hearts2':0,'spades':4,'spades2':0,
}
cards_dir = "./cards"

def pressed_key():
    while True:
        k = cv2.waitKey(0)
        if k == ord('='):
            return 1
        elif k == ord('-'):
            return -1
        elif k == ord('0'):
            return 0

class Card:
    def __init__(self, filename):
        self.value, self.face, self.face_name = self.calculate_value(filename)
        self.png = cv2.imread(cards_dir+'/'+filename)
        return
    def calculate_value(self, filename):
        n = filename.split("_")
        v = cards_table[str(n[0])]
        f = cards_table[str(n[2].split('.')[0])]
        fn = str(n[2].split('.')[0])
        return v, f, fn
    def show(self, pos):
        cv2.namedWindow(str(self))
        cv2.moveWindow(str(self), pos[0], pos[1])
        cv2.imshow(str(self), self.png)
    def get_value(self):
        return self.value
    def __str__(self):
        return str(self.value) + " of "+str(self.face_name)

class Deck:
    def __init__(self, pngs):
        self.cards = []
        for i in pngs:
            if not (i.startswith("red") or i.startswith("black")):
                c = Card(i)
                if c.face != 0:
                    self.cards.append(c)
        return
        
    def get_cards(self):
        return self.cards

    def show(self, pos):
        for card in self.get_cards():
            card.show(pos=pos)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def practice_recognition(self):
        score = 0
        counter = 0
        for card in self.get_cards():
            card.show(pos=(0, 0))
            key = pressed_key()
            correct = 0
            if 2<=card.get_value()<=6:
                correct = 1
            if 7<=card.get_value()<=9:
                correct = 0
            if 10<=card.get_value()<=14:
                correct = -1
            if key == correct:
                score += 1
            counter += 1
            print(score,'/',counter)
            cv2.destroyAllWindows()
        return

if __name__=="__main__":
    pngs = [(str(f)) for f in listdir(cards_dir) if isfile(join(cards_dir, f))]
    deck = Deck(pngs)
    deck.shuffle()
    # deck.show(pos=(0, 0))
    deck.practice_recognition()
