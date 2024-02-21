# DIY Home Automation Kiosk Touch Display

## Introduction

Thanks for your interest in my DIY Home Automation Kiosk Touch Display.
Here’s how to build your own Smart Home Kiosk with a touch display using a Raspberry Pi.
I am using this with a Home Assistant eco-system, but this will work with effectively ANY smart home solution.

> ### Note, there is a VIDEO guide to compliment this page, please consider watching:
>
> Watch the build and assembly guide video: [HERE](https://www.youtube.com/watch?v=n_zXSw7AeVA)

## Components Required

- Raspberry Pi models 3B+, 4, or 5.
- Genuine Raspberry Pi 7” touch display, or Elecrow Crowvision 7inch touch display
- 16gb or larger micro SD card
- A USB SD card reader, so we can write the OS to the SD card from your PC.
- Competent power supply to power the Pi.
- 3d printed housing to mount Pi and Display

All of these can be found on Amazon [HERE](https://www.amazon.com/hz/wishlist/ls/1XS56G6OG3PV?ref_=wl_share)  
Direct link for Elecrow Crowvision 7inch [HERE](https://www.elecrow.com/crowvision-7-0-inch-touch-screen-capacitive-portable-hdmi-1024-600-ips-lcd-monitor-rear-fixing-for-raspberry-pi.html?idd=5)  
Download the STL for the wall mount via [Printables](https://www.printables.com/model/774136-raspberry-pi-7-touch-display-flush-wall-mount-pane) or [Thingiverse](https://www.thingiverse.com/thing:6495742)

## Writing Image to SD Card

1. Firstly, head to https://www.raspberrypi.com/software/ and, download official RasPi imager.
2. Then install the imager software, and launch it.
3. Insert your SD card into the reader and plug that into your PC.
4. Then, using the imager software, we select our Pi device you’ll likely be selecting a Raspberry pi 3b, or 4 or 5.
5. For operating system, select the **Other** submenu, then choose the Raspberry pi **lite** image
6. For storage, select the appropriate SD card.
7. Write the image.
8. We can now remove the SD card from the PC and insert it into the Pi, then it's time to power up your Pi and verify it boots successfully.

- Note, first boot may take some time so give it a good 5 minutes.

## OS Update

Now with the Pi up and running, we need to set it up with all the software it needs with some console commands.  
You can do this directly on the device, just plug in your keyboard and away you go, or you do SSH onto it from another PC.  
`Ssh username@<hostname> (or ipaddress)`

Once you are in, first thing to do is Update the Pi, so we enter each of the following commands and follow the prompts:  
`sudo apt-get update -y`  
`sudo apt-get upgrade -y`

Then, we set the PI to autologin upon boot:  
`1. System options`  
`S5. boot auto login`  
`B2. Console auto login`  
`Finish`  
`Reboot`

## Software Installs

Install basic GUI (GUI kit used for Chomium)  
`sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox`

Install Chromium Web browser (We are using Chromium to display webpage - you can use others)  
`sudo apt-get install --no-install-recommends chromium-browser`

Next For our little OS python based menu, install python, Python toolkit, PIP & PySimpleGUI  
`sudo apt install python`  
`sudo apt-get install python3-tk`  
`install pip: 'sudo apt install python3-pip`  
`pip install --upgrade PySimpleGUI`

Install wmctrl which is a command that can be used to interact with running applications, and in this case we use it to brings the menu to the top and keep it on top of the browser  
`sudo apt install wmctrl`

## Scripts

First up, create Menu script  
`sudo nano ~/Menu.py`  
**_copy-paste_** content from _Meny.py_ file in this repo.  
Note, edit the URL that you want the browser to load on launch.  
Then, save and exit nano by pressing ctrl-x to request the exit then Y to confirm the save, and enter to complete the action and return to the console.

Edit Openbox config (Openbox Window manager edits)  
`sudo nano /etc/xdg/openbox/autostart`  
**_copy-paste_** content from _autostart_ file in this repo.  
Note, edit the URL that you want the browser to load on launch.  
Then, save and exit nano by pressing ctrl-x to request the exit then Y to confirm the save, and enter to complete the action and return to the console.

Next, we need to start start the X server UI on boot, so, create bash profile:  
`sudo nano ~/.bash_profile`  
Paste the following line in the file:  
`[[-z $DISPLAY && $XDG_VTNR -eq 1]] && startx -- -nocursor`  
Then, save and exit nano by pressing ctrl-x to request the exit then Y to confirm the save, and enter to complete the action and return to the console.

That’s it, time to Reboot Pi (To a hopefully working Kiosk!)  
`sudo reboot`

## Boot Up and Test!

The device should now restart, load into a blank desktop, then launch both the Chromium browser and the Python menu.  
The browser will load up the webpage we told it to link to, and since this integrates to HomeAssistant you will need to login on the first load. But that will be a one time activity, and its something you can't do over SSH, so consider just quickly plugging in a keyboard to get over that hurdle.  
I’d recommend creating a HomeAssistant user specific for the dashboard, you can name them something generic like "DashboardUser", and you can even set them up with their own dashboard layout.  
You can interact with the HomeAssistant dashboard using the touch interface, and if you need to restart the browser, or perhaps shutdown the Pi, then the python menu will always (eventually) pop back on screen.

## Your awesome new Home Automation Kiosk is now finished, congratulations!

### Thanks & Credits

Toni: creatingsmarthome.com  
Mark: https://www.youtube.com/watch?v=4hN0_yGVdUQ  

