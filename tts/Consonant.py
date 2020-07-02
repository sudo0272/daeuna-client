from tts.ArticulationMethod import ArticulationMethod
from tts.ArticulationPosition import ArticulationPostion

NO_SOUND = ''

class Consonant:
    def __init__(self, letter: str):
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
            pass  # All of consonants except Bottom Consonants in korean are evinced

        # Determine aspiration position
        if letter in ('ㅁ', 'ㅂ', 'ㅃ', 'ㅍ'):
            self.articulation_position = ArticulationPostion.BILABIAL
        
        elif letter in ('ㄴ', 'ㄷ', 'ㄸ', 'ㅌ', 'ㅅ', 'ㅆ', 'ㄹ'):
            self.articulation_position = ArticulationPostion.ALVEOLAR
        
        elif letter in ('ㅈ', 'ㅉ', 'ㅊ'):
            self.articulation_position = ArticulationPostion.PALATAL
        
        elif letter in ('ㅇ', 'ㄱ', 'ㄲ', 'ㅋ'):
            self.articulation_position = ArticulationPostion.VELAR
        
        elif letter in ('ㅎ'):
            self.articulation_position = ArticulationPostion.GLOTTAL
        
        else:
            pass  # All consonants except Bottom Consonants in korean are evinced
        
        
            
    def to_plain(self):
        return self.plain
    
    def to_tense(self):
        return self.tense
    
    def to_aspirated(self):
            return self.aspirated
    
    
