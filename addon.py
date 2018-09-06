import xbmcaddon
#import xbmcgui
import os
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
setting = addon.getSetting('bt_mac_01')
line1 = "Connect to Bluetooth-Device"
line2 = "specially written for Korbi"
 
#xbmcgui.Dialog().ok(addonname, line1, line2)
os.system('echo -e "connect %s\nexit" | /usr/bin/bluetoothctl' % setting)