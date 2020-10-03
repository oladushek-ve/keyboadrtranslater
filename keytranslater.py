from typing import Dict

class KeyboardTranslater:

    TO_RUS: Dict[str, str] = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
        'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', '{': 'х', 
        ']': 'ъ', '}': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 
        'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', 
        ':': 'ж', "'": "э", '"': 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 
        'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', 
        '/': '.', '?': ',', '&': '?'
    }
    TO_EN: Dict[str, str] = {v: k for k, v in TO_RUS.items()}
    
    def __init__(self, word: str):
        if not word:
            raise ValueError('For the translation, write a word')
        self.word = word.lower()
    
    def translater(self):
        res_word = ''
        for i in self.word:
            try:
                res_word += KeyboardTranslater.TO_RUS[i]
            except KeyError:
                try:
                    res_word += KeyboardTranslater.TO_EN[i]
                except KeyError:
                    res_word += i
        return res_word
    
    def choose_translate(self, language: str='Ru'):
        res_word = ''
        for i in self.word:
                try:
                    if language == 'En':
                        res_word += KeyboardTranslater.TO_EN[i]
                    else:
                        res_word += KeyboardTranslater.TO_RUS[i]
                except KeyError:
                    res_word += i
        return res_word