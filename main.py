import keytranslater
import pyperclip
import pyautogui
import time
from pynput import keyboard

def translating():
	kbt = keytranslater.KeyboardTranslater(pyperclip.paste())
	pyperclip.copy(kbt.translater())

def choose_translating():
	kbt = keytranslater.KeyboardTranslater(pyperclip.paste())
	lang = pyautogui.confirm('Выбери язык', 'Язык', ('Ru', 'En'))
	pyperclip.copy(kbt.choose_translate(lang))

def exit_from_prog():
	exit()

def replase_word():
	
	with keyboard.GlobalHotKeys({'<ctrl>+<alt>+q': translating,'<ctrl>+<alt>+l': choose_translating, '<ctrl>+e': exit_from_prog	}) as h:
		time.sleep(.6)
		pyautogui.hotkey('ctrl', 'v')
		h.join()

if __name__ == '__main__':
	replase_word() 

