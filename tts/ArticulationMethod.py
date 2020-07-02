from enum import Enum

class ArticulationMethod(Enum):
    NASAL = 0
    NASAL_CONSONANTS = ('ㅁ', 'ㄴ', 'ㅇ')
    AFFRICATE_PLAIN = 1
    AFFRICATE_PLAIN_CONSONANTS = ('ㅂ', 'ㄷ', 'ㅈ', 'ㄱ')
    AFFRICATE_TENSE = 2
    AFFRICATE_TENSE_CONSONANTS = ('ㅃ', 'ㄸ', 'ㅉ', 'ㄲ')
    AFFRICATE_ASPIRATED = 3
    AFFRICATE_ASPIRATED_CONSONANTS = ('ㅍ', 'ㅌ', 'ㅊ', 'ㅋ')
    FRICATIVE_PLAIN = 4
    FRICATIVE_PLAIN_CONSONANTS = ('ㅅ', 'ㅎ')
    FRICATIVE_TENSE = 5
    FRICATIVE_TENSE_CONSONANTS = ('ㅆ')
    LIQUID = 6
    LIQUID_CONSONANTS = ('ㄹ')
    
