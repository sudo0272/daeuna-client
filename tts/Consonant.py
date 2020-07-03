from tts.ArticulationMethod import ArticulationMethod
from tts.ArticulationPosition import ArticulationPostion
from tts.BottomConsonantRepresentativeSound import BottomConsonantRepresentativeSound
from tts.LetterType import LetterType

NO_SOUND = ''

class Consonant:
    def __init__(self, letter: str, letter_type: LetterType):
        self.__letter = letter
        self.__letter_type = letter_type

        # Set plain, tense and aspirated
        if self.__letter in ('ㄱ', 'ㄲ', 'ㅋ'):
            self.__plain = 'ㄱ'
            self.__tense = 'ㄲ'
            self.__aspirated = 'ㅋ'
            
        elif self.__letter in ('ㄷ', 'ㄸ', 'ㅌ'):
            self.__plain = 'ㄷ'
            self.__tense = 'ㄸ'
            self.__aspirated = 'ㅌ'

        elif self.__letter in ('ㅂ', 'ㅃ', 'ㅍ'):
            self.__plain = 'ㅂ'
            self.__tense = 'ㅃ'
            self.__aspirated = 'ㅍ'

        elif self.__letter in ('ㅅ', 'ㅆ'):
            self.__plain = 'ㅅ'
            self.__tense = 'ㅆ'
            self.__aspirated = NO_SOUND

        elif self.__letter in ('ㅈ', 'ㅉ', 'ㅊ'):
            self.__plain = 'ㅈ'
            self.__tense = 'ㅉ'
            self.__aspirated = 'ㅊ'
        
        else:
            self.__plain = NO_SOUND
            self.__tense = NO_SOUND
            self.__aspirated = NO_SOUND
        
        # Determine articulation method
        if self.__letter in ArticulationMethod.PLOSIVE_PLAIN_CONSONANTS:
            self.__articulation_method = ArticulationMethod.PLOSIVE_PLAIN

        elif self.__letter in ArticulationMethod.PLOSIVE_TENSE_CONSONANTS:
            self.__articulation_method = ArticulationMethod.PLOSIVE_TENSE

        elif self.__letter in ArticulationMethod.PLOSIVE_ASPIRATED_CONSONANTS:
            self.__articulation_method = ArticulationMethod.PLOSIVE_ASPIRATED

        elif self.__letter in ArticulationMethod.AFFRICATE_PLAIN_CONSONANTS:
            self.__articulation_method = ArticulationMethod.AFFRICATE_PLAIN

        elif self.__letter in ArticulationMethod.AFFRICATE_TENSE_CONSONANTS:
            self.__articulation_method = ArticulationMethod.AFFRICATE_TENSE

        elif self.__letter in ArticulationMethod.AFFRICATE_ASPIRATED_CONSONANTS:
            self.__articulation_method = ArticulationMethod.AFFRICATE_ASPIRATED

        elif self.__letter in ArticulationMethod.FRICATIVE_PLAIN_CONSONANTS:
            self.__articulation_method = ArticulationMethod.FRICATIVE_PLAIN

        elif self.__letter in ArticulationMethod.FRICATIVE_TENSE_CONSONANTS:
            self.__articulation_method = ArticulationMethod.FRICATIVE_TENSE

        elif self.__letter in ArticulationMethod.NASAL_CONSONANTS:
            self.__articulation_method = ArticulationMethod.NASAL

        elif self.__letter in ArticulationMethod.LIQUID_CONSONANTS:
            self.__articulation_method = ArticulationMethod.LIQUID

        else:
            self.__articulation_method = ArticulationMethod.INVALID_LETTER


        # Determine aspiration position
        if self.__letter in ArticulationPostion.BILABIAL_CONSONANTS:
            self.__articulation_position = ArticulationPostion.BILABIAL
        
        elif self.__letter in ArticulationPostion.ALVEOLAR_CONSONANTS:
            self.__articulation_position = ArticulationPostion.ALVEOLAR
        
        elif self.__letter in ArticulationPostion.PALATAL_CONSONANTS:
            self.__articulation_position = ArticulationPostion.PALATAL
        
        elif self.__letter in ArticulationPostion.VELAR_CONSONANTS:
            self.__articulation_position = ArticulationPostion.VELAR
        
        elif self.__letter in ArticulationPostion.GLOTTAL_CONSONANTS:
            self.__articulation_position = ArticulationPostion.GLOTTAL
        
        else:
            self.__articulation_position = ArticulationPostion.INVALID_LETTER  # All consonants except Bottom Consonants in korean are evinced
        
        # Determine the representative sound of the letter only if the letter is a bottom letter
        if self.__letter_type == LetterType.JONGSUNG:
            if self.__letter in BottomConsonantRepresentativeSound.GIYUK_CONSONANTS:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.GIYUK
            
            elif self.__letter in BottomConsonantRepresentativeSound.NIEUN_CONSONANTS:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.NIEUN
            
            elif self.__letter in BottomConsonantRepresentativeSound.DIGUT_CONSONANTS:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.DIGUT
            
            elif self.__letter in BottomConsonantRepresentativeSound.RIEUL_CONSONANTS:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.RIEUL

            elif self.__letter in BottomConsonantRepresentativeSound.MIEUM_CONSONANTS:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.MIEUM

            elif self.__letter in BottomConsonantRepresentativeSound.IEUNG_CONSONANTS:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.IEUNG

            else:
                self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.INVALID_LETTER

        else:
            self.__bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.NOT_BOTTOM_CONSONANT

    def to_plain(self):
        return self.__plain
    
    def to_tense(self):
        return self.__tense
    
    def to_aspirated(self):
            return self.__aspirated
    
    def get_articulation_method(self):
        return self.__articulation_method
    
    def get_articulation_position(self):
        return self.__articulation_position

    def get_bottom_consonant_representative_sound(self):
        return self.__bottom_consonant_representative_sound
