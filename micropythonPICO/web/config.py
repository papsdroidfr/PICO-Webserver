''' config global variables of the web module:
    - WIFI-SSID: wifi ssid to connect
    - WIFI-PASSWORD: my wifi password
    - STATION: is the network.WLAN to activate
    - LED: led of PICO for managing connection status
        blinking: waiting for a wifi connection 
        green: web server started
        off: not wifi connexion.
'''

from .led import Led

#########################################
WIFI_SSID = "my wifi ssid"
WIFI_PASSWORD = "my wifi password"
LED = Led()
#########################################