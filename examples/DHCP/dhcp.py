from microbit import *
from usocket import socket
import network

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K() 
    nic.active(True)
    
    nic.ifconfig('dhcp')
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)
        
def main():
    w5x00_init()

if __name__ == "__main__":
    main()