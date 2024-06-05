import time
from pywinauto.application import Application, WindowSpecification
from pywinauto.keyboard import send_keys
from pywinauto.mouse import move, press, release

app: Application = Application(backend="uia").start('notepad.exe')

notpad: WindowSpecification = app.UntitledNotepad
notpad.type_keys("Hello World !!!"+"{ENTER}0"*50, with_spaces=True)
notpad.print_control_identifiers()

notpad.menu_select("Edit -> Replace")
replace: WindowSpecification = notpad.Replace
find_what: WindowSpecification = replace.child_window(title="Find what:", control_type="Edit")
find_what.type_keys('^a{DEL}')
find_what.type_keys("World", with_spaces=True)

replace_with: WindowSpecification = replace.child_window(title="Replace with:", control_type="Edit")
replace_with.type_keys('^a{DEL}')
replace_with.type_keys("CES", with_spaces=True)


replace_all_button: WindowSpecification = replace.child_window(title="Replace All", control_type="Button")
replace_all_button.click()


cancel_button: WindowSpecification = replace.child_window(title="Cancel", control_type="Button")
cancel_button.click()

close_button: WindowSpecification = notpad.child_window(title="Close", control_type="Button")  
close_button.click()


save_changes_window: WindowSpecification = notpad.child_window(title="Notepad")  

cancel_save_changes_button: WindowSpecification = save_changes_window.child_window(title="Cancel", control_type="Button")
cancel_save_changes_button.click()


scroll_bar = notpad.Edit.child_window(title="Vertical", control_type="ScrollBar")
scroll_bar_rect = scroll_bar.rectangle()

# Function to click and drag the scroll bar
def drag_scroll_bar(scroll_bar_rect, direction="down", distance=100) -> None:
    if direction == "down":
        start_y = scroll_bar_rect.top + 10
        end_y = start_y + distance
    else:
        start_y = scroll_bar_rect.bottom - 10
        end_y = start_y - distance

    start_x = (scroll_bar_rect.left + scroll_bar_rect.right) // 2
    move(coords=(start_x, start_y))
    press(button="left", coords=(start_x, start_y))
    move(coords=(start_x, end_y))
    release(button="left", coords=(start_x, end_y))

time.sleep(2)
# Drag the scroll bar down
drag_scroll_bar(scroll_bar_rect, direction="up", distance=5000)

time.sleep(2)
# Drag the scroll bar up
drag_scroll_bar(scroll_bar_rect, direction="down", distance=1000)

time.sleep(2)

notpad.menu_select("File -> Exit")

dont_save_changes_button: WindowSpecification = save_changes_window.child_window(title="Don't Save", control_type="Button")
dont_save_changes_button.click()