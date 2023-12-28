# How to Test DHCP Example


## Step 1: Prepare Software

The following serial terminal program is required for **DHCP** test, download and install from below links.

&#10004;[**Thonny**][link-thonny]


## Step 2: Prepare hardware

1. Combine WIZnet Ethernet Product with micro:bit
2. Connect ethernet cable to Ethernet port.
3. Connect micro:bit to desktop or laptop using 5 pin micro USB cable.


## Step 3: Setup DHCP Example

To test the **DHCP example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_config]


2. Initialize device network informaion.

The parameters for the `nic.ifconfig` function are entered in the order of __('dhcp')__

```python
def w5x00_init():
    
    ...
    #None DHCP
    nic.ifconfig(('dhcp'))
    ...
    
```


## Step 4: Upload and Run

When the file is executed, it displays the DHCP address that has been configured
![][link-dhcp]

<!--
Link
-->

[link-thonny]: https://thonny.org/

[link-thonny_config]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/Thonny_conf_1.png
[link-dhcp]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/dhcp.png
