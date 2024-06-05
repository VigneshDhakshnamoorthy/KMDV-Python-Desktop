from pywinauto.application import Application, WindowSpecification
from pywinauto.keyboard import send_keys
import time

app: Application = Application().start("notepad.exe")
notepad: WindowSpecification = app.UntitledNotepad
notepad.wait('ready')
notepad.print_control_identifiers()
notepad.Edit.type_keys("Hello, this is a test. Let's replace some text using Pywinauto.", with_spaces=True)

notepad.menu_select("Edit->Replace")

replace_dlg: WindowSpecification = app.Replace
replace_dlg.wait('ready')
replace_dlg.print_control_identifiers()


find_input = replace_dlg.child_window(title="Fi&nd what:", class_name="Static").wrapper_object()
find_input.click_input(double=True)
send_keys('^a{DEL}')
find_input = replace_dlg.child_window(title="Fi&nd what:", class_name="Static").wrapper_object()
find_input.click_input(double=True)
find_input.type_keys("test", with_spaces=True)
