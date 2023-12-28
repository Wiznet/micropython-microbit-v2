# How to Test Loopback Example


## Step 1: Prepare Software

The following serial terminal program is required for **TCP Loopback** test, download and install from below links.

&#10004;[**Thonny**][link-thonny] and &#10004; [**Hercules**][link-hercules]


## Step 2: Prepare hardware

1. Combine WIZnet Ethernet Product with micro:bit
2. Connect ethernet cable to Ethernet port.
3. Connect micro:bit to desktop or laptop using 5 pin micro USB cable.


## Step 3: Setup TCP Loopback Example

To test the **TCP Loopback example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_config]


2. Initialize device network informaion.

The parameters for the `nic.ifconfig` function are entered in the order of __('device IP', 'netmask', 'gateway IP', 'DNS')__

```python
def w5x00_init():
    
    ...
    #None DHCP
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    ...
    
```

3. How to operate as a **Loopback Server**.

```py
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
```

4. How to operate as a **Loopback Client**.

```python
def client_loop():
    s = socket()
    s.connect(('192.168.11.100', 5000)) #Destination IP Address
    
    print("Loopback start!")
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data)
```



## Step 4: Upload and Run

### Loopback Server Mode

1. When the `server_loop()` function is invoked in the main, the device switches to server mode and starts listening for incoming connection.

![][link-loopback_server_1]

2. Open the Hercules program to set **[IP Address]** and **[PORT number]** and Connect to the Server.

![][link-loopback_server_2]

3. If you send the phrase Loopback Test, you can see that you are sending and receiving data.

![][link-loopback_server_3]



### Loopback Client Mode

1. Open the server in the Hercules program. If you put in the port number and press Listen, the server will open.

![][link-loopback_client_1]

2. When the `server_loop()` function is invoked in the main, the device switches to client mode and connect to server.

![][link-loopback_client_2]

3.  If you send the data from the server, you can receive the data you sent.

![][link-loopback_client_3]


 [**¢¸ Go to Ethernet example structure**](#ethernet_example_structure)




<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-hercules]: https://www.hw-group.com/software/hercules-setup-utility

[link-thonny_config]: https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Thonny_conf_1.png

[link-loopback_server_1]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_server_1.png
[link-loopback_server_2]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_server_2.png
[link-loopback_server_3]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_server_3.png

[link-loopback_client_1]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_client_1.png
[link-loopback_client_2]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_client_2.png
[link-loopback_client_3]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_client_3.png

