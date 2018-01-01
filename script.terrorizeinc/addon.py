import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello Brad The Butt Baby!"
line2 = "Hows Is Going?"
line3 = "Well OK Bye Now Butt Baby"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
