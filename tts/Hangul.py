class Hangul:
    UNICODE_START = 0xAC00
    CHOSUNG = ('ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    JUNGSUNG = ('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ')
    JONGSUNG = ('', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')
    NUMBER_OF_CHOSUNG = len(CHOSUNG)
    NUMBER_OF_JUNGSUNG = len(JUNGSUNG)
    NUMBER_OF_JONGSUNG = len(JONGSUNG)
    CHOSUNG_INDEX = 0
    JUNGSUNG_INDEX = 1
    JONGSUNG_INDEX = 2

    def __init__(self, letter: str):
        self.__letter = letter

        base_code = ord(letter) - Hangul.UNICODE_START
        self.__chosung_index = base_code // Hangul.NUMBER_OF_JUNGSUNG // Hangul.NUMBER_OF_JONGSUNG
        temp = base_code - self.__chosung_index * Hangul.NUMBER_OF_JUNGSUNG * Hangul.NUMBER_OF_JONGSUNG
        self.__jungsung_index = temp // Hangul.NUMBER_OF_JONGSUNG
        self.__jongsung_index = temp - (self.__jungsung_index * Hangul.NUMBER_OF_JONGSUNG)

        self.__splitted = (
            self.CHOSUNG[self.__chosung_index],
            self.JUNGSUNG[self.__jungsung_index],
            self.JONGSUNG[self.__jongsung_index]
        )

    def split(self):
        return self.__splitted
