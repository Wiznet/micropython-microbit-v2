# How to WebClient Example


## Step 1: Prepare Software

The following serial terminal program is required for **Webclient** test, download and install from below links.

### &#10004;[**Thonny**][link-thonny]




## Step 2: Prepare hardware

1. Combine WIZnet Ethernet Product with micro:bit
2. Connect ethernet cable to Ethernet port.
3. Connect micro:bit to desktop or laptop using 5 pin micro USB cable.


## Step 3: Setup WebClinet Example

To test the **Webclient example**, minor settings shall be done in code.

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

4. HTML request, Access **HTML **.

```python
    r = urequests.get('http://httpbin.org/get')
    #r.raise_for_status
    print(r.status_code)
    print(r.text)

```



## Step 4: Upload and Run

1. Use DNS to access the address of the server. After that, it accesses the server in each URL and prints the contents. The text of each URL is as follows.
![][link-webclient_1]


<!--
Link
-->

[link-thonny]: https://thonny.org/

[link-thonny_http]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/Thonny_conf_1.png
[link-webclient_1]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/webclient_1.png


