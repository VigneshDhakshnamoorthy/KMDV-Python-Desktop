from typing import Any
from pywinauto import Desktop, Application
from pywinauto.application import WindowSpecification

Application().start('explorer.exe "C:\\Program Files"')

app: Application = Application(backend="uia").connect(path="explorer.exe", title="Program Files")

app.ProgramFiles.set_focus()
common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
common_files.right_click_input()
app.ContextMenu.Properties.invoke()

Properties: Any | WindowSpecification = Desktop(backend='uia').Common_Files_Properties
Properties.print_control_identifiers()
Properties.Cancel.click()
Properties.wait_not('visible')