from microbit import *
from usocket import socket
import network

#W5x00 chip init
def w5x00_init():
    nic = network.WIZNET5K()
    print("1")
    nic.active(True)
    print("2")
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    print('IP address :', nic.ifconfig())
    
    while not nic.isconnected():
        sleep(1)
    
def server_loop(): 
    s = socket()
    s.bind(('192.168.11.20', 5000)) #Source IP Address
    s.listen(5)
    
    print("Wait client ...")
    conn, addr = s.accept()
    print("Connect from:", addr) 
    print("Loopback start!")
    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL':
            conn.send(data)

def client_loop():
    s = socket()
    s.connect(('192.168.11.100', 5000)) #Destination IP Address
    
    print("Loopback start!")
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data)
        
def main():
    w5x00_init()
    
###TCP SERVER###
    #server_loop()

###TCP CLIENT###
    client_loop()


if __name__ == "__main__":
    main()