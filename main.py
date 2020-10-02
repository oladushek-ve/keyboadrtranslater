import keytranslater
import pyperclip
import pyautogui
import time

def translating(kbt):
	pyperclip.copy(kbt.translater())

def choose_translating(kbt):
	lang = pyautogui.confirm('Выбери язык', 'Язык', ('Ru', 'En'))
	pyperclip.copy(kbt.choose_translate(lang))

def replase_word():	
	kt = keytranslater.KeyboardTranslater(pyperclip.paste())
	
	translating(kt)
	choose_translating(kt)

	time.sleep(.5)
	pyautogui.hotkey('alt', 'tab')
	time.sleep(.6)
	pyautogui.hotkey('ctrl', 'v')

if __name__ == '__main__':
	replase_word() 
