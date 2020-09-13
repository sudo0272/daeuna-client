from konlpy.tag import Mecab

class Pronunciation:
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__mecab = Mecab()
        self.__parsedSentence = self.__mecab.pos(self.__sentence)
    
