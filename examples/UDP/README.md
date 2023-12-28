# How to Test UDP Loopback Example


## Step 1: Prepare Software

The following serial terminal program is required for **UDP Loopback** test, download and install from below links.

&#10004;[**Thonny**][link-thonny] and &#10004; [**Hercules**][link-hercules]


## Step 2: Prepare hardware

1. Combine WIZnet Ethernet Product with micro:bit
2. Connect ethernet cable to Ethernet port.
3. Connect micro:bit to desktop or laptop using 5 pin micro USB cable.


## Step 3: Setup UDP Loopback Example

To test the **UDP Loopback example**, minor settings shall be done in code.

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

3. How to operate as a **Loopback**.

To bind a UDP socket, set the socket parameters as follows.

```py
def loopback ():
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 5000))

    print("Loopback start")
    while True:
        data, addr = s.recvfrom(1024)
        print("Received message:", data, addr)

        if data != 'NULL':
            s.sendto(data, addr)
```

## Step 4: Upload and Run

1. When the `loopback()` function is invoked in the main, UDP communication becomes possible.

![][link-loopback_udp_1]

2. Open the Hercules program to set **[IP Address]** and **[PORT number]**.

![][link-loopback_udp_2]

3. If you send the phrase Loopback Test, you can see that you are sending and receiving data and PC IP and port.

![][link-loopback_udp_3]



 [**¢¸ Go to Ethernet example structure**](#ethernet_example_structure)




<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-hercules]: https://www.hw-group.com/software/hercules-setup-utility

[link-thonny_config]: https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Thonny_conf_1.png

[link-loopback_udp_1]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_udp_1.png
[link-loopback_udp_2]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_udp_2.png
[link-loopback_udp_3]:https://github.com/Wiznet/micropython-microbit-v2/blob/main/static/images/Loopback_udp_3.png
