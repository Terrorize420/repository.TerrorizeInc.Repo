import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "[COLOR gold]Hello[/COLOR] [COLOR blue]Brad[/COLOR][COLOR gold] The Butt Baby![/COLOR]"
line2 = "[COLOR red]Hows Is Going?[/COLOR]"
line3 = "[COLOR freen]Well OK Bye Now Butt Baby[/COLOR]"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
