from tts.ArticulationMethod import ArticulationMethod
from tts.ArticulationPosition import ArticulationPostion
from tts.BottomConsonantRepresentativeSound import BottomConsonantRepresentativeSound
from tts.LetterType import LetterType

NO_SOUND = ''

class Consonant:
    def __init__(self, letter: str, letter_type: LetterType):
        self.letter = letter

        # Set plain, tense and aspirated
        if letter in ('ㄱ', 'ㄲ', 'ㅋ'):
            self.plain = 'ㄱ'
            self.tense = 'ㄲ'
            self.aspirated = 'ㅋ'
            
        elif letter in ('ㄷ', 'ㄸ', 'ㅌ'):
            self.plain = 'ㄷ'
            self.tense = 'ㄸ'
            self.aspirated = 'ㅌ'

        elif letter in ('ㅂ', 'ㅃ', 'ㅍ'):
            self.plain = 'ㅂ'
            self.tense = 'ㅃ'
            self.aspirated = 'ㅍ'

        elif letter in ('ㅅ', 'ㅆ'):
            self.plain = 'ㅅ'
            self.tense = 'ㅆ'
            self.aspirated = NO_SOUND

        elif letter in ('ㅈ', 'ㅉ', 'ㅊ'):
            self.plain = 'ㅈ'
            self.tense = 'ㅉ'
            self.aspirated = 'ㅊ'
        
        else:
            self.plain = NO_SOUND
            self.tense = NO_SOUND
            self.aspirated = NO_SOUND
        
        # Determine articulation method
        if letter in ArticulationMethod.NASAL_CONSONANTS:
            self.articulation_method = ArticulationMethod.NASAL

        elif letter in ArticulationMethod.AFFRICATE_PLAIN_CONSONANTS:
            self.articulation_method = ArticulationMethod.AFFRICATE_PLAIN
        
        elif letter in ArticulationMethod.AFFRICATE_TENSE_CONSONANTS:
            self.articulation_method = ArticulationMethod.AFFRICATE_TENSE
        
        elif letter in ArticulationMethod.AFFRICATE_ASPIRATED_CONSONANTS:
            self.articulation_method = ArticulationMethod.AFFRICATE_ASPIRATED
        
        elif letter in ArticulationMethod.FRICATIVE_PLAIN_CONSONANTS:
            self.articulation_method = ArticulationMethod.FRICATIVE_PLAIN
        
        elif letter in ArticulationMethod.FRICATIVE_TENSE_CONSONANTS:
            self.articulation_method = ArticulationMethod.FRICATIVE_TENSE
        
        elif letter in ArticulationMethod.LIQUID_CONSONANTS:
            self.articulation_method = ArticulationMethod.LIQUID
        
        else:
            self.articulation_method = ArticulationMethod.INVALID_LETTER  # All of consonants except Bottom Consonants in korean are evinced

        # Determine aspiration position
        if letter in ArticulationPostion.BILABIAL_CONSONANTS:
            self.articulation_position = ArticulationPostion.BILABIAL
        
        elif letter in ArticulationPostion.ALVEOLAR_CONSONANTS:
            self.articulation_position = ArticulationPostion.ALVEOLAR
        
        elif letter in ArticulationPostion.PALATAL_CONSONANTS:
            self.articulation_position = ArticulationPostion.PALATAL
        
        elif letter in ArticulationPostion.VELAR_CONSONANTS:
            self.articulation_position = ArticulationPostion.VELAR
        
        elif letter in ArticulationPostion.GLOTTAL_CONSONANTS:
            self.articulation_position = ArticulationPostion.GLOTTAL
        
        else:
            self.articulation_position = ArticulationPostion.INVALID_LETTER  # All consonants except Bottom Consonants in korean are evinced
        
        # Determine the representative sound of the letter only if the letter is a bottom letter
        if letter_type == LetterType.JONGSUNG:
            if letter in BottomConsonantRepresentativeSound.GIYUK_CONSONANTS:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.GIYUK
            
            elif letter in BottomConsonantRepresentativeSound.NIEUN_CONSONANTS:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.NIEUN
            
            elif letter in BottomConsonantRepresentativeSound.DIGUT_CONSONANTS:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.DIGUT
            
            elif letter in BottomConsonantRepresentativeSound.RIEUL_CONSONANTS:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.RIEUL

            elif letter in BottomConsonantRepresentativeSound.MIEUM_CONSONANTS:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.MIEUM

            elif letter in BottomConsonantRepresentativeSound.IEUNG_CONSONANTS:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.IEUNG

            else:
                self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.INVALID_LETTER

        else:
            self.bottom_consonant_representative_sound = BottomConsonantRepresentativeSound.NOT_BOTTOM_CONSONANT

    def to_plain(self):
        return self.plain
    
    def to_tense(self):
        return self.tense
    
    def to_aspirated(self):
            return self.aspirated
    
    def get_articulation_method(self):
        return self.articulation_method
    
    def get_articulation_position(self):
        return self.articulation_position

    def get_bottom_consonant_representative_sound(self):
        return self.bottom_consonant_representative_sound
