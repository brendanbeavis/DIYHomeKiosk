import os
import PySimpleGUI as sg
from subprocess import check_call
import subprocess, signal

#set the theme
theme = "Dark Gray 11"
font_family = "Roboto"
font_size = 18

sg.theme(theme)
sg.set_options(font=(font_family,font_size))

#define the layout
menu = [
    ["M",["Reboot OS","Shutdown OS","---","Restart Browser","Quit Menu","---","   "]]
]

layout = [
        [sg.MenubarCustom(menu)]
]

#create the window
window = sg.Window("MENU", layout, no_titlebar=True, keep_on_top=True, finalize=True) #, takefocus=True)
window.keep_on_top_set()

#brightness up func
def brightness_up ():
   file=open('/sys/class/backlight/rpi_backlight/brightness','r+')
   data=file.read()
   newData=int(data)
   newData = newData + 26
   if newData > 255:
      newData=255
   file.write(str(newData))

#brightness down func
def brightness_down ():
   file=open('/sys/class/backlight/rpi_backlight/brightness','r+')
   data=file.read()
   newData=int(data)
   newData = newData - 26
   if newData < 15:
      newData=15
   file.write(str(newData))

#stop browser func
def close_browser():
   p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE);
   out, err = p.communicate();
   for line in out.splitlines():
      if b'chromium' in line:
         pid = int(line.split(None, 1)[0])
         os.kill(pid, signal.SIGTERM)

#start browser func
def open_browser():
   subprocess.Popen(['chromium-browser','--kiosk','http://192.168.0.5:8123'])

#move_window function
def move_window(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width), (screen_height - win_height)
    window.move(x, y)

move_window(window)

#the logical code
while True:
   event, values = window.read()
   print(event, values)
   if event in (sg.WINDOW_CLOSED, "Quit Menu"):
      break
   if event == "Reboot OS":
      check_call(["sudo","reboot"])
   if event == "Shutdown OS":
      check_call(['sudo', 'poweroff']);
   if event == "Restart Browser":
      close_browser()
      open_browser()

window.close()
