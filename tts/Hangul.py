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

    class NotChosungError(Exception):
        pass
    
    class NotJungsungError(Exception):
        pass

    class NotJongsungError(Exception):
        pass

    def __init__(self, letter: str, is_first_articulation: bool):
        self.__letter = letter

        base_code = ord(letter) - Hangul.UNICODE_START
        self.__chosung_index = base_code // Hangul.NUMBER_OF_JUNGSUNG // Hangul.NUMBER_OF_JONGSUNG
        temp = base_code - self.__chosung_index * Hangul.NUMBER_OF_JUNGSUNG * Hangul.NUMBER_OF_JONGSUNG
        self.__jungsung_index = temp // Hangul.NUMBER_OF_JONGSUNG
        self.__jongsung_index = temp - (self.__jungsung_index * Hangul.NUMBER_OF_JONGSUNG)

        self.__splitted = [
            self.CHOSUNG[self.__chosung_index],
            self.JUNGSUNG[self.__jungsung_index],
            self.JONGSUNG[self.__jongsung_index]
        ]

        self.__is_first_articulation = is_first_articulation
    
    def is_chosung(self, letter):
        return letter in self.CHOSUNG
    
    def is_jungsung(self, letter):
        return letter in self.JUNGSUNG
    
    def is_jongsung(self, letter):
        return letter in self.JONGSUNG

    def split(self):
        return self.__splitted

    def merge(self):
        self.__letter = chr(
            self.UNICODE_START +
            self.__chosung_index * self.NUMBER_OF_JUNGSUNG * self.NUMBER_OF_JONGSUNG +
            self.__jungsung_index * self.NUMBER_OF_JONGSUNG +
            self.__jongsung_index
        )

    def get_letter(self):
        return self.__letter

    def get_chosung(self):
        return self.__splitted[self.CHOSUNG_INDEX]
    
    def set_chosung(self, chosung):
        if len(chosung) == 1 and self.is_chosung(chosung):
            self.__splitted[self.CHOSUNG_INDEX] = chosung
            self.__chosung_index = self.CHOSUNG.index(chosung)

            self.merge()
        
        else:
            raise self.NotChosungError(f'''Letter '{chosung}' is not a Chosung character''')
    
    def get_jungsung(self):
        return self.__splitted[self.JUNGSUNG_INDEX]

    def set_jungsung(self, jungsung):
        if len(jungsung) == 1 and self.is_jungsung(jungsung):
            self.__splitted[self.JUNGSUNG_INDEX] = jungsung
            self.__jungsung_index = self.JUNGSUNG.index(jungsung)
            
            self.merge()
        
        else:
            raise self.NotJungsungError(f'''Letter '{jungsung}' is not a Jungsung character''')

    def get_jongsung(self):
        return self.__splitted[self.JONGSUNG_INDEX]
    
    def set_jongsung(self, jongsung):
        if len(jongsung) == 1 and self.is_jongsung(jongsung):
            self.__splitted[self.JONGSUNG_INDEX] = jongsung
            self.__jongsung_index = self.JONGSUNG.index(jongsung)

            self.merge()
        
        else:
            raise self.NotJongsungError(f'''Letter '{jongsung}' is not a Jungsung character''')

    def is_first_articulation(self):
        return self.__is_first_articulation
