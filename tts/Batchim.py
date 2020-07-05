class Batchim:
    GIYUK = 0
    GIYUK_CONSONANTS = ('ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ')
    NIEUN = 1
    NIEUN_CONSONANTS = ('ㄴ', 'ㄵ')
    DIGUT = 2
    DIGUT_CONSONANTS = ('ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ')
    RIEUL = 3
    RIEUL_CONSONANTS = ('ㄹ', 'ㄼ', 'ㄽ', 'ㄾ')
    MIEUM = 4
    MIEUM_CONSONANTS = ('ㅁ', 'ㄻ')
    BIEUP = 5
    BIEUP_CONSONANTS = ('ㅂ', 'ㅍ', 'ㅄ', 'ㄿ')
    IEUNG = 6
    IEUNG_CONSONANTS = ('ㅇ')
    NOT_BOTTOM_CONSONANT = 7
    INVALID_LETTER = 8

    def __init__(self, letter: str):
        self.__letter = letter

        if self.__letter in self.GIYUK_CONSONANTS:
            self.__bottom_consonant_representative_sound = self.GIYUK
        
        elif self.__letter in self.NIEUN_CONSONANTS:
            self.__bottom_consonant_representative_sound = self.NIEUN
        
        elif self.__letter in self.DIGUT_CONSONANTS:
            self.__bottom_consonant_representative_sound = self.DIGUT
        
        elif self.__letter in self.RIEUL_CONSONANTS:
            self.__bottom_consonant_representative_sound = self.RIEUL

        elif self.__letter in self.MIEUM_CONSONANTS:
            self.__bottom_consonant_representative_sound = self.MIEUM

        elif self.__letter in self.IEUNG_CONSONANTS:
            self.__bottom_consonant_representative_sound = self.IEUNG

        else:
            self.__bottom_consonant_representative_sound = self.INVALID_LETTER

    def get_representative_sound(self):
        return self.__bottom_consonant_representative_sound
