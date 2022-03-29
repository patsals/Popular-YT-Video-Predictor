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
        self.__db_name = db_name
        self.__conn = sqlite3.connect(db_name + ".db")
        self.__cur = self.__conn.cursor()

    def generate_title1(self):
        NP1 = self.get_word_by_POS("NNP")
        NP2 = self.get_word_by_POS("NNP")
        N = self.get_word_by_POS("NN")
        V1 = self.get_word_by_POS("V")
        V2 = self.get_word_by_POS("V")
        V3 = self.get_word_by_POS("V")
        Dt = self.get_word_by_POS("DT")
        JJ = self.get_word_by_POS("JJ")

        VPt = V3 + " " + JJ
        NPt = Dt + " " + N
        S = NPt + " " + VPt
        VPt = V2 + " " + S
        S = NP2 + " " + VPt
        VPt = V1 + " " + S
        phrase = NP1 + " " + VPt

        self.__conn.close()
        return phrase


    def get_word_by_POS(self, POS_prefix):
        query = "SELECT word FROM " + self.__db_name + " WHERE POS LIKE \"" + POS_prefix + "%\""
        self.__cur.execute(query)
        results = self.__cur.fetchall()
        if len(results) > 0:
            return results[random.randint(0, len(results)-1)][0]
        else:
            return ""


