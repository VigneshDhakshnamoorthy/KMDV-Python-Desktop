from pywinauto_recorder.recorder import Recorder
from pywinauto_recorder.player import UIPath, send_keys, find, click, menu_click, move, mouse_wheel, playback

recorder = Recorder()
recorder.process_menu_click_mode = True
recorder.start_recording()