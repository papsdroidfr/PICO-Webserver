''' this module try to connect to WIFI_SSID
    
    args: None
    
    properties:
    - is_connected: True/False
    - ip_adress: ip adress in str format.
    
    methods:
    - disconnect(): disconnect from network
    
'''
from web.config import WIFI_SSID, WIFI_PASSWORD, LED
from web.log import log_error, log_warn, log_info
import time, network, sys

class Wifi:
    '''  connect to WIFI_SSID
    '''
    def __init__(self):
        LED.off()
        self._wlan = network.WLAN(network.STA_IF)
        self._wlan.active(True)
        self._wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        try:
            while not self.is_connected:
                print(f'Waiting for connection on {WIFI_SSID}...')
                time.sleep(0.5)
                LED.blink()
        except KeyboardInterrupt:
            LED.off()
            sys.exit(1)
            
        LED.on()    
        print(f'my ip adress: {self.ip_adress}')
    
    @property
    def is_connected(self) -> bool:
        return self._wlan.isconnected()
    
    @property
    def ip_adress(self) -> str:
        return self._wlan.ifconfig()[0]
    
    
    def disconnect(self) -> None:
        '''Disconnect from network'''
        self._wlan.disconnect()
        LED.off()
        log_info('Disconnected')

if  __name__ == '__main__':
    print('test module wifi.py')
    my_wifi = Wifi()
    time.sleep(2)
    my_wifi.disconnect()
    print('bye')

