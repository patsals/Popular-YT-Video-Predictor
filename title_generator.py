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

class PhraseGenerator:
    def __init__(self, freqd):
        #print(nltk.pos_tag(freqd.keys()))
        print(sorted(set(dict(nltk.pos_tag(freqd.keys())).values())))


f = {'Saint': 1, 'Peter': 1, 's': 8, 'vs': 2, 'Purdue': 1, 'Sweet': 1, '16': 1, 'NCAA': 1, 'tournament': 1, 'extended': 1, 'highlights': 1, 'Could': 1, 'he': 1, 'do': 1, 'this': 1, 'with': 3, 'a': 5, 'football': 1, 'shorts': 3, 'How': 2, 'Teachers': 1, 'Help': 1, 'You': 1, 'During': 1, 'Tests': 1, 'Shorts': 2, 'Summer': 1, 'Walker': 1, 'SZA': 1, 'Cardi': 1, 'B': 2, 'No': 1, 'Love': 1, 'Extended': 2, 'Version': 2, 'Official': 8, 'Video': 8, 'Soy': 2, 'El': 2, 'Unico': 2, 'Yahritza': 2, 'Y': 2, 'su': 1, 'Esencia': 2, 'Festival': 1, 'Announces': 1, 'Taylor': 2, 'Hawkins': 2, 'Passing': 1, '1': 3, 'Hour': 1, 'Before': 1, 'Foo': 2, 'Fighters': 2, 'Performance': 1, 'Nicki': 1, 'Minaj': 1, 'feat': 2, 'Fivio': 1, 'Foreign': 1, 'We': 2, 'Go': 2, 'Up': 3, 'Audio': 1, 'Machine': 1, 'Gun': 1, 'Kelly': 1, 'maybe': 1, 'Bring': 1, 'Me': 1, 'The': 4, 'Horizon': 1, 'Music': 3, 'World': 2, 'Cutest': 1, 'Animals': 1, 'Is': 3, 'Creatine': 1, 'safe': 1, 'for': 2, 'you': 1, 'U': 1, 'Know': 1, 'What': 1, 'From': 1, 'Disney': 1, 'and': 4, 'Pixar': 1, 'Turning': 1, 'Red': 1, 'Every': 2, 'Blue': 1, 'Sky': 1, 'Studios': 1, 'Movie': 1, 'Ranked': 1, 'DDG': 1, 'Elon': 1, 'Musk': 1, 'ft': 2, 'Gunna': 1, 'Bawby': 1, 'shows': 1, 'Matt': 1, 'his': 1, 'iPod': 1, 'Drummer': 1, 'Has': 1, 'Passed': 1, 'Away': 1, 'At': 1, '50': 1, 'Musicians': 1, 'Pay': 1, 'Tribute': 1, 'Eliminatorias': 2, 'Argentina': 1, '3': 1, '0': 2, 'Venezuela': 1, 'Sushi': 1, 'Married': 1, 'Making': 1, 'Slime': 2, 'Chef': 1, 'Again': 1, 'Batman': 2, 'Arkham': 1, 'Deleted': 2, 'Scene': 2, '2022': 1, 'Robert': 1, 'Pattinson': 1, 'Barry': 1, 'Keoghan': 1, 'Se': 1, 'Acabo': 1, 'Oficial': 1, 'Lenin': 1, 'Ramirez': 1, 'Fuerza': 1, 'Regida': 1, 'y': 1, 'Banda': 1, 'Renovacion': 1, 'COME': 1, 'ON': 1, 'LET': 1, 'S': 1, 'GO': 1, 'These': 1, 'are': 1, 'Putin': 1, 'sanctions': 2, 'Understanding': 1, 'the': 3, 'economic': 1, 'against': 1, 'Russia': 2, 'ODA': 1, 'WE': 1, 'CAN': 1, 'T': 2, 'STOP': 1, 'SMILING': 1, 'Luffy': 2, 'Gear': 1, '5': 3, 'Sun': 1, 'God': 1, 'Nika': 1, 'Mode': 1, 'EXPLAINED': 1, 'HITO': 2, 'FRUIT': 2, 'JOY': 1, 'BOY': 1, 'Laughing': 1, 'yelling': 1, 'at': 1, 'TikTok': 1, 'WILDCAT': 1, 'Nogla': 1, 'Trapped': 1, 'For': 1, '100': 2, 'Days': 1, 'in': 4, 'Minecraft': 3, 'Zombie': 1, 'Town': 1, 'Reacting': 1, 'to': 2, 'most': 1, 'INSANE': 1, 'Speedrun': 1, 'All': 1, 'Advancements': 1, 'Record': 1, 'VS': 1, '29': 1, '000': 1, 'House': 1, '118': 1, 'days': 1, 'later': 1, 'Smartest': 1, 'way': 1, 'RickRoll': 1, 'anyone': 1, 'Latto': 1, 'Sunshine': 1, 'Visualizer': 1, 'Lil': 1, 'Wayne': 1, 'Childish': 1, 'Gambino': 1, 'ROLE': 1, 'MODEL': 1, 'neverletyougo': 1, 'Mfs': 1, 'switch': 1, 'up': 1, 'after': 1, 'taking': 1, 'shower': 1, 'Classroom': 1, 'has': 1, 'one': 1, 'Types': 1, 'of': 2, 'Students': 1, 'Mrs': 1, 'Woolley': 1, '5th': 1, 'bridgerton': 1, 'teacher': 1, 'Brasil': 1, '4': 1, 'Chile': 1, 'Fecha': 1, '17': 1, 'SUN': 1, 'GOD': 1, 'LUFFY': 1, 'GEAR': 1, 'REVEALED': 1, 'HIS': 1, 'DEVIL': 1, 'ISN': 1, 'WHAT': 1, 'YOU': 1, 'THINK': 1, 'One': 1, 'Piece': 1, 'Chapter': 1, '1044': 2, 'Squid': 1, 'Game': 1, 'Parody': 1, 'Season': 1, '2': 2, 'Ep': 1, 'TIP': 1, 'FROM': 1, 'THE': 2, 'START': 1, 'AT': 1, 'BAR': 1, 'Hundreds': 1, 'Jets': 1, 'Are': 1, 'Stuck': 1, 'Fight': 1, 'Between': 1, 'West': 1, 'WSJ': 1, 'Su': 1, 'Pepe': 1, 'Office': 1, 'J': 1, 'Balvin': 1, 'Ed': 1, 'Sheeran': 1, 'Sigue': 1, 'JayDaYoungan': 1, 'Heaven': 1, 'Gates': 1, 'Yungeen': 1, 'Ace': 1, 'Kodak': 1, 'Black': 1, 'A': 1, 'M': 1, 'Lyric': 1, 'Cactus': 1, 'Beatbox': 1, 'beatbox': 1, 'tiktok': 1, 'I': 3, 'Transformed': 1, 'VILLAGE': 1, 'Hardcore': 1, 'what': 1, 'i': 1, 'did': 1, 'valentine': 1, 'day': 1, 'If': 1, 'This': 1, 'Secret': 1, 'Behind': 1, 'New': 1, 'Powers': 1, 'll': 1, 'Cry': 1, 'Explained': 1, 'Elden': 1, 'Ring': 1, 'dunkview': 1, 'GAVE': 1, 'MY': 1, 'CAT': 1, 'CATNIP': 1, 'Joker': 1, 'My': 1, 'Thoughts': 1}

PhraseGenerator(f)

def generate_phrase1(NP1, V1, NP2, V2, Dt, N, V3, JJ):

    VPt = V3 + JJ
    NPt = Dt + N
    S = NPt + VPt
    VPt = V2 + S
    S = NP2 + VPt
    VPt = V1 + S
    phrase = NP1 + VPt
    return phrase



def assemble(*args):
    return args[0] + " " + args[1]
