# Farbod Shahinfar
# 13/11/95
# Bot Entekhab Vahed Golestan
# IUST-CE

import pyautogui

def scroll_up():
    pyautogui.scroll(300)

def create_new_line():
    btn_pos = (100,100)
    scroll_up()
    pyautogui.click(btn_pos)
    scroll_up()
