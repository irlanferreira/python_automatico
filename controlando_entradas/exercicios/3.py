import pyautogui, time

pyautogui.screenshot('print_automacao.png')
time.sleep(2)
pyautogui.click(194, 310, duration=0.1)
pyautogui.hotkey('delete')
pyautogui.hotkey('enter')
