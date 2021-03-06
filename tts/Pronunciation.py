from SentenceParser import SentenceParser
from LetterConverter import LetterConverter

class Pronunciation:
    class NotSupportedLanguageError(Exception):
        pass

    def __init__(self, sentence):
        # remove whitespaces
        self.__original_sentence = ' ' + ' '.join(sentence.split())
        self.__sentence = ''
        self.__parsed_sentence = []

        self.__sentence_parser = SentenceParser()
        self.__letter_converter = LetterConverter()
        
        # parse
        self.__parsed_sentence = self.__sentence_parser.parse(self.__original_sentence)
        self.__converted_sentence = self.__letter_converter.convert(self.__original_sentence, self.__parsed_sentence)


    def fluctuate(self):
        for i in self.__converted_sentence:
            print(i[0].get_letter(), i[0].is_first_articulation(), i[1])

