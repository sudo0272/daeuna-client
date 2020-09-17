import ctypes
from ISO_639_1_ISO_637_2_T_Map import ISO_639_1_ISO_637_2_T_Map
from HangulNames import HangulNames
from NumberNames import NumberNames
from Hangul import Hangul
import langdetect
import hanja

class LetterConverter:
    class NotSupportedLanguageError(Exception):
        pass

    def __init__(self):
        # load hangulize
        libconvert_to_hangul = ctypes.cdll.LoadLibrary('./libconvert_to_hangul.so')
        self.__convert_to_hangul = libconvert_to_hangul.convert_to_hangul
        self.__convert_to_hangul.argtypes = [ ctypes.c_char_p, ctypes.c_char_p ]
        self.__convert_to_hangul.restype = ctypes.c_char_p

    def __convert_ISO_639_1_to_ISO_637_2_T(self, language_code):
        if language_code in ISO_639_1_ISO_637_2_T_Map.keys():
            result = ISO_639_1_ISO_637_2_T_Map[language_code]

            return result

        else:
            raise self.NotSupportedLanguageError(f'Language code {language_code} is not supported yet')

    def __convert_number_to_hangul(self, number, has_nnbc):
        result = ''

        # number's digit is bigger than 16 (quadrillian)
        # simple reading
        if len(number) > 16:
            for i in number:
                result += NumberNames[1][0][ord(i) - ord('0')]

        # hangul-method reading
        elif len(number) <= 2 and has_nnbc:
            if len(number) == 2:
                result += NumberNames[0][1][ord(number[0]) - ord('0')]

                number = number[1]

            result += NumberNames[0][0][ord(number[0]) - ord('0')]

        # hanja-method reading
        else:
            chunks = []

            while number != '':
                chunks.append(number[-4:])
                number = number[:-4]
            
            for i in range(len(chunks)):
                chunk = chunks[i]
                chunk_size = len(chunk)
                temp = ''

                for j in range(chunk_size - 1, -1, -1):
                    n = int(chunk[chunk_size - 1 - j])

                    if n > 1 or (n == 1 and i > 1 and j == 0):
                        temp += NumberNames[1][0][n]

                    if n >= 1:
                        temp += NumberNames[1][1][j]

                temp += NumberNames[1][2][i]
                result = temp + result

        return result

    def convert(self, sentence, parsed_sentence):
        sentence_index = 0
        converted_sentence = []

        for parsed_word_index,  parsed_word in enumerate(parsed_sentence):
            tags = tuple(parsed_word[1].split('+'))

            is_first_articulation = sentence[sentence_index] == ' '

            if is_first_articulation:
                print(sentence_index)
                sentence_index += 1

            # letter is foreign language
            if 'SL' in tags:
                iso_693_1_language_code = langdetect.detect(parsed_word[0])
                iso_637_2_t_language_code = self.__convert_ISO_639_1_to_ISO_637_2_T(iso_693_1_language_code)

                hangul_word = \
                    self.__convert_to_hangul( \
                        iso_637_2_t_language_code.encode('utf-8'), \
                        parsed_word[0].encode('utf-8') \
                    ).decode('utf-8')

                for j in range(len(hangul_word)):
                    converted_sentence.append((Hangul(hangul_word[j], j == 0), ('NNG', )))

                sentence_index += len(parsed_word)

            # letter is hanja
            # TODO: distinguish korean, japanese and chinese kanji
            elif 'SH' in tags:
                hangul_word = hanja.translate(parsed_word, 'substitution')
                for j in hangul_word:
                    converted_sentence.append((Hangul(j, is_first_articulation), ('NNG', )))
                
                
            # TODO: letter is number
            # TODO: consider ',' which is used to split numbers
            elif 'SN' in tags:
                is_hangul_number \
                    = parsed_word_index + 1 < len(converted_sentence) and \
                      'NNBC' in converted_sentence[parsed_word_index + 1][1]
                
                
                converted_numbers \
                    = self.__convert_number_to_hangul( \
                        parsed_word[0], \
                        is_hangul_number \
                    )

                for j in converted_numbers:
                    converted_sentence.append((Hangul(j, is_first_articulation), ('NNG', )))
                    is_first_articulation = False
                
                sentence_index += len(parsed_word[0])

            # letter is a special character
            elif len({'SF', 'SE', 'SC', 'SY'}.intersection(tags)):
                sentence_index += 1

            # TODO: when letter's type is SSO or SSC, add wait sign so that
            #       listener can distinguish if the content is for describing
                
            # letter is hangul
            else:
                for j in parsed_word[0]:
                    # print(j, sentence_index, sentence)

                    # j is single letter hangul
                    if j in HangulNames.keys():
                        # convert to hangul's name
                        letter = HangulNames[j]

                        for k in letter:
                            converted_sentence.append((Hangul(k, is_first_articulation), ('NNG', )))
                            is_first_articulation = False

                        sentence_index += 1
                        
                    else:
                        converted_sentence.append((Hangul(j, is_first_articulation), tags))
                        print(j, sentence_index)

                        sentence_index += 1

                    is_first_articulation = False
        return converted_sentence

