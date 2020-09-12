from tts.Hangul import Hangul
from tts.Batchim import Batchim
import konlpy.tag

class Pronunciation:
    def is_hangul(self, letter: str) -> bool:
        return ord('가') <= ord(letter) <= ord('힣')

    def __init__(self, sentence: str):
        self.__non_hangul_letters = []
        self.__letters = []
        self.__mecab = konlpy.tag.Mecab()
        self.__parsed = self.__mecab.pos(sentence)

        for current_index, current_letter in enumerate(sentence):
            if self.is_hangul(current_letter):
                self.__letters.append(Hangul(current_letter, current_index > 0 and sentence[current_index - 1] == ' '))

            else:
                self.__non_hangul_letters.append((sentence[current_index], current_index))
    
    def fluctuate(self):
        # TODO: 표준 발음법 제5항 다만 1

        for letter_index, letter in enumerate(self.__letters):
            batchim = Batchim(letter.get_jongsung())
            is_letter_last_letter = letter_index + 1 == len(self.__letters)

            next_letter_index = None if is_letter_last_letter else letter_index + 1
            next_letter = None if is_letter_last_letter else self.__letters[next_letter_index]

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

            # TODO: 표준 발음법 제6항 [붙임]

            # TODO: 표준 발음법 제6항 [붙임] 다만

            # TODO: 표준 발음법 제7항 1

            # TODO: 표준 발음법 제7항 1 다만

            # TODO: 표준 발음법 제7항 2

            # TODO: 표준 발음법 제7항 2 다만

            # TODO: 표준 발음법 제7항 2 [붙임]

            # 표준 발음법 제9항
            # 표준 발음법 제10항
            # 표준 발음법 제11항
            if batchim.get_batchim() != '':
                # 표준 발음법 제10항 다만
                if (not is_letter_last_letter and
                    letter.get_letter() == '밟' and
                    next_letter.get_chosung() != 'ㅇ'):
                    self.__letters[letter_index].set_jongsung('ㅂ')
                
                # 표준 발음법 제10항 다만
                elif (not is_letter_last_letter and
                    letter.get_letter() == '넓' and
                    (next_letter.get_letter() == '죽' or
                     next_letter.get_letter() == '둥')):
                    self.__letters[letter_index].set_jongsung('ㅂ')
                
                else:
                    self.__letters[letter_index].set_jongsung(batchim.get_representative_sound())

            # TODO: 표준 발음법 제11항 다만

    def get_letters(self):
        result = []
        
        for letter in self.__letters:
            result.append(letter.get_letter())
        
        for non_hangul_letter in self.__non_hangul_letters:
            result.insert(non_hangul_letter[1], non_hangul_letter[0])
        
        return ''.join(result)
