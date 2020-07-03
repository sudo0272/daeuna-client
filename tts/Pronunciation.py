from tts.Hangul import Hangul

class Pronunciation:
    def is_hangul(self, letter: str) -> bool:
        return ord('가') <= ord(letter) <= ord('힣')

    def __init__(self, sentence: str):
        self.__non_hangul_letter_index = []
        self.__letters = []
        self.__sentence = sentence

        for current_index, current_letter in enumerate(sentence):
            if self.is_hangul(current_letter):
                self.__letters.append(Hangul(current_letter, current_index > 0 and sentence[current_index - 1] == ' '))

            else:
                self.__non_hangul_letter_index.append(current_index)
    
    def fluctuate(self):
        # TODO: 표준 발음법 제5항 다만 1

        for letter_index, letter in enumerate(self.__letters):
            # 표준 발음법 제5항 다만 2
            # This rule is only accepted rule but being implemented for native pronunciation
            if (letter.get_jungsung() == 'ㅖ' and
                (letter.get_letter() != '예' or
                 letter.get_letter() != '례')):
                self.__letters[letter_index].set_jungsung('ㅔ')

            # 표준 발음법 제5항 다만 3
            elif (letter.is_first_articulation() and
                  letter.get_jungsung == 'ㅢ'):
                self.__letters[letter_index].set_jungsung('ㅣ')

            # TODO: 표준 발음법 제5항 다만 4

            # TODO: 표준 발음법 제6항
            # TODO: 표준 발음법 제6항 다만
