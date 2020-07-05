from tts.Consonant import Consonant

class Batchim(Consonant):
    GIYUK_CONSONANTS = ('ㄱ', 'ㄲ', 'ㅋ', 'ㄳ', 'ㄺ')
    NIEUN_CONSONANTS = ('ㄴ', 'ㄵ')
    DIGUT_CONSONANTS = ('ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ')
    RIEUL_CONSONANTS = ('ㄹ', 'ㄼ', 'ㄽ', 'ㄾ')
    MIEUM_CONSONANTS = ('ㅁ', 'ㄻ')
    BIEUP_CONSONANTS = ('ㅂ', 'ㅍ', 'ㅄ', 'ㄿ')
    IEUNG_CONSONANTS = ('ㅇ')

    def __init__(self, batchim: str):
        super.__init__()
        self.__batchim = batchim

        if self.__batchim in self.GIYUK_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㄱ'
        
        elif self.__batchim in self.NIEUN_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㄴ'
        
        elif self.__batchim in self.DIGUT_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㄷ'
        
        elif self.__batchim in self.RIEUL_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㄹ'

        elif self.__batchim in self.MIEUM_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㅁ'

        elif self.__batchim in self.BIEUP_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㅂ'

        elif self.__batchim in self.IEUNG_CONSONANTS:
            self.__bottom_consonant_representative_sound = 'ㅇ'

        else:
            self.__bottom_consonant_representative_sound = ''

    def get_representative_sound(self):
        return self.__bottom_consonant_representative_sound

    def get_batchim(self):
        return self.__batchim
