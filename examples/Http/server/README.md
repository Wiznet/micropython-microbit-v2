# How to WebServer Example


## Step 1: Prepare Software

The following serial terminal program is required for **Webserver** test, download and install from below links.

### &#10004;[**Thonny**][link-thonny]


## Step 2: Prepare hardware

1. Combine WIZnet Ethernet Product with micro:bit
2. Connect ethernet cable to Ethernet port.
3. Connect micro:bit to desktop or laptop using 5 pin micro USB cable.


## Step 3: Setup Webserver Example

To test the **Webserver example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_http]

2. Create a new file by pressing the **New File** button. Copy the ***urequest.py*** library code into it. You can access the *urequest* library code in the following derectory. 
    - __[examples/Http/lib](https://github.com/Wiznet/micropython-microbit-v2/blob/master/examples/Http/lib)__


3. Initialize device network informaion.

The parameters for the `nic.ifconfig` function are entered in the order of __('device IP', 'netmask', 'gateway IP', 'DNS')__

```python
def w5x00_init():
    
    ...
    #None DHCP
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    ...
    
```

4. HTML request

```python
def http_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)

    while True:
        print("Wait client ...")        
        cl, addr = s.accept()
        print("Connect from:", addr)
        
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
    
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send('<html><body><h1>Hello, World!</h1></body></html>\r\n')
        cl.close()
```


## Step 4: Upload and Run

When you execute the code, it launches a web server. You connect to the device with the set IP, you can see the following screen.

![][link-webserver_1]



<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-thonny_http]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/Thonny_conf_1.png
[link-webserver_1]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/webserver_1.png
