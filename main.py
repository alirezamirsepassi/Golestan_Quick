# Farbod Shahinfar
# 13/11/95
# Bot Entekhab Vahed Golestan
# IUST-CE
import pyautogui


def scroll_up():
    pyautogui.scroll(300)


def create_new_line(line_counts):
    scroll_up()
    btn_pos = (1471,190)
    scroll_up()
    pyautogui.click(btn_pos)
    scroll_up()


def choose_ie_window():
    pyautogui.click(1000,200)


def find_new_line(line_counts):
    x = 1465
    y = 17 * line_counts + 230
    print(y)
    scroll_up()
    pyautogui.moveTo(x, y, duration=0.25)
    pyautogui.click()


def click_done():
    btn_pos = (1596, 931)
    pyautogui.click(btn_pos)


def enter_data(data):
    pyautogui.typewrite(data)


def wait_to_load():
    while True:
        img = pyautogui.locateOnScreen("blue.png")
        if img is None:
            break


def main():
    choose_ie_window()
    scroll_up()
    number_of_courses = 2
    line_counts = 7
    data = ["141108747","141109233", "161111706", "221102501", "221129302", "221129501", "901109410"]
    for i in range(number_of_courses):
        create_new_line(line_counts)
        line_counts += 1
        find_new_line(line_counts)
        enter_data(data[i])
        click_done()
        wait_to_load()
    print("Done!")


main()
