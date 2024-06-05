from pywinauto.application import Application, WindowSpecification

app: Application = Application(backend="uia").start('notepad.exe')

notpad: WindowSpecification = app.UntitledNotepad
notpad.type_keys("Hello World !!!", with_spaces=True)
notpad.print_control_identifiers()

edit_button: WindowSpecification = notpad.menu_select("Edit -> Replace")
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

dont_save_changes_button: WindowSpecification = save_changes_window.child_window(title="Don't Save", control_type="Button")
dont_save_changes_button.click()

