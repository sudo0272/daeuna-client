from tts.Hangul import Hangul

class Pronunciation:
    def is_hangul(self, letter: str) -> bool:
        return ord('가') <= ord(letter) <= ord('힣')

    def __init__(self, sentence: str):
        self.__non_hangul_letter_index = []
        self.__compressed_sentence = ''
        self.__sentence = sentence

        for current_index, current_letter in sentence:
            if self.is_hangul(current_letter):
                self.__compressed_sentence += current_letter
            else:
                self.__non_hangul_letter_index.append(current_index)
        