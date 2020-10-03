import keytranslater
import pyperclip
import pyautogui
import time
from pynput import keyboard

def translating():
	kbt = keytranslater.KeyboardTranslater(pyperclip.paste())
	pyperclip.copy(kbt.translater())
	# pyautogui.hotkey('ctrl', 'v')

def choose_translating():
	kbt = keytranslater.KeyboardTranslater(pyperclip.paste())
	lang = pyautogui.confirm('Выбери язык', 'Язык', ('Ru', 'En'))
	pyperclip.copy(kbt.choose_translate(lang))
	# pyautogui.hotkey('ctrl', 'v')

def exit_from_prog():
	exit()

def replase_word():
	
	with keyboard.GlobalHotKeys({'<ctrl>+[': translating,'<ctrl>+]': choose_translating, '<ctrl>+e': exit_from_prog	}) as h:
		h.join()

if __name__ == '__main__':
	replase_word() 