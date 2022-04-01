"""

following this phrase structure guideline:
https://linguistics.stackexchange.com/questions/29972/phrase-structure-trees-for-different-languages
https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk
https://www.nltk.org/book_1ed/ch08.html following 10b diagram

NN == NNP == NNPS == NNS
JJ == JJS
PRP == PRP$
RB == RBR == RBS
VB == VBD == VBG == VBP == VBPZ
WDT == WRB == WP
"""

import nltk
import sqlite3
import random
import time

class TitleGenerator:
    def __init__(self, db_name):
        self.__db_name = db_name.replace(" ","") + "_popular_words"


    def generate_simple_title1(self):
        N1 = self.get_word_by_POS("NN")
        V = self.get_word_by_POS("VBD")
        N2 = self.get_word_by_POS("NN")
        title = N1 + " " + V + " " + N2

        return " ".join([word.capitalize() for word in title.split(" ")])

    def generate_simple_title2(self):
        N1 = self.get_word_by_POS("NN")
        N2 = self.get_word_by_POS("NN")
        DT1 = self.get_word_by_POS("DT")
        DT2 = self.get_word_by_POS("DT")
        P = self.get_word_by_POS("P%")
        V = self.get_word_by_POS("VBD")
        NP = self.get_word_by_POS("NN%")

        NPt = DT1 + " " + N1
        PPt = P + " " + NPt
        NPt = DT2 + " " + N2
        VPt = V + " " + NPt
        VPt = VPt + " " + PPt
        title = NP + " " + VPt

        return " ".join([word.capitalize() for word in title.split(" ")])

    def generate_title1(self):
        N1 = self.get_word_by_POS("NN")
        N2 = self.get_word_by_POS("NN")
        JJ1 = self.get_word_by_POS("JJ")
        JJ2 = self.get_word_by_POS("JJ")
        JJ3 = self.get_word_by_POS("JJ3")
        DT1 = self.get_word_by_POS("DT")
        DT2 = self.get_word_by_POS("DT")
        V = self.get_word_by_POS("VBD")

        NOMt = JJ1 + " " + N1
        NOMt = JJ2 + " " + NOMt
        NPt = DT1 + " " + NOMt
        VPt = V + " " + NPt
        NOMt = JJ3 + " " + N2
        NPt = DT2 + " " + NOMt
        title = NPt + " " + VPt

        return " ".join([word.capitalize() for word in title.split(" ")])

    def generate_title2(self):
        NP1 = self.get_word_by_POS("NN%")
        NP2 = self.get_word_by_POS("NN%")
        N = self.get_word_by_POS("NN")
        V1 = self.get_word_by_POS("VBD")
        V2 = self.get_word_by_POS("VBD")
        V3 = self.get_word_by_POS("VBD")
        Dt = self.get_word_by_POS("DT")
        JJ = self.get_word_by_POS("JJ")

        VPt = V3 + " " + JJ
        NPt = Dt + " " + N
        S = NPt + " " + VPt
        VPt = V2 + " " + S
        S = NP2 + " " + VPt
        VPt = V1 + " " + S
        title = NP1 + " " + VPt

        return " ".join([word.capitalize() for word in title.split(" ")])


    def get_word_by_POS(self, POS_prefix):
        conn = sqlite3.connect(self.__db_name + ".db")
        cur = conn.cursor()

        query = "SELECT word FROM " + self.__db_name + " WHERE POS LIKE \"" + POS_prefix + "\""
        cur.execute(query)
        results = cur.fetchall()

        conn.close()
        if len(results) > 0:
            return results[random.randint(0, len(results)-1)][0]
        else:
            return ""


