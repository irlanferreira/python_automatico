import pyautogui, keyboard, time

time.sleep(3)
pyautogui.hotkey('win')
keyboard.write('bloco de notas', delay=0.01)
pyautogui.hotkey('enter')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'n')
keyboard.write("Relatório iniciado. Este é um teste do PyAutoGUI.")
time.sleep(0.5)
pyautogui.shortcut("ctrl", 's')