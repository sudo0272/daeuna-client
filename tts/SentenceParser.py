from konlpy.tag import Mecab

class SentenceParser:
    def __init__(self):
        self.__mecab = Mecab()

    def parse(self, sentence):
        return self.__mecab.pos(sentence)

