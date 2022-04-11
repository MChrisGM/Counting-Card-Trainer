from os import listdir
from os.path import isfile, join
import cv2

cards_table = {
    '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'jack':11,'queen':12,'king':13,'ace':14,'clubs':1,'clubs2':0,'diamonds':2,'diamonds2':0,'hearts':3,'hearts2':0,'spades':4,'spades2':0,
}
cards_dir = "./cards"

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

if __name__=="__main__":
    
    pngs = [(str(f)) for f in listdir(cards_dir) if isfile(join(cards_dir, f))]

    deck = Deck(pngs)

    for card in deck.get_cards():
        card.show(pos=(0, 0))
        cv2.waitKey(0)
        cv2.destroyAllWindows()