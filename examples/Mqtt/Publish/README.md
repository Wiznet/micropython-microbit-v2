# How to Test MQTT Publish Example



## Step 1: Prepare Software

The following serial terminal program is required for **MQTT Publish** test, download and install from below links.

&#10004;[**Thonny**][link-thonny]  and  &#10004; [**Mosquitto**][link-mosquitto]


## Step 2: Prepare hardware

1. Combine WIZnet Ethernet Product with micro:bit
2. Connect ethernet cable to Ethernet port.
3. Connect micro:bit to desktop or laptop using 5 pin micro USB cable.

## Step 3: Setup MQTT Publish Example

To test the **MQTT Publish example**, minor settings shall be done in code.

1. Check COMport in [Device Manager] and then open **Thonny** Python IDE.

![][link-thonny_config]

2. Create a new file by pressing the **New File** button. Copy the ***umqttsimple.py*** library code into it. You can access the *umqttsimple* library code in the following derectory. 
    - __[examples/Mqtt/lib](https://github.com/Wiznet/micropython-microbit-v2/blob/master/examples/Mqtt/lib)__


3. Initialize device network informaion.

The parameters for the `nic.ifconfig` function are entered in the order of __('device IP', 'netmask', 'gateway IP', 'DNS')__

```python
def w5x00_init():
    
    ...
    #None DHCP
    nic.ifconfig(('192.168.11.20','255.255.255.0','192.168.11.1','8.8.8.8'))
    ...
    
```

4. In the MQTT configuration, the broker IP address is the IP of your desktop.

```python
mqtt_server = '192.168.11.100'
client_id = 'wiz'
topic_pub = b'topic'
topic_msg = b'Hello I am microbit'

...

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client
    
```

5. How to use MQTT Publish.

```python
def main():
    w5x00_init()
    
    client = mqtt_connect()

    while True:
        client.publish(topic_pub, topic_msg)
        sleep(1000)

    client.disconnect()
    
```


## Step 4: Upload and Run

1. Create broker using mosquitto by executing the following command. If the broker is created normally, the broker's IP address is the current IP of your desktop or laptop, and the port is 1883 by default.

```
mosquitto -c mosquitto.conf -p 1883 -v
```

![][link-mqtt_1]

2. If the MQTT publish example operates normally on the micro:bit, it connects to the broker and publishes a message every second

![][link-mqtt_2]

3. Subscribe to the broker with the above command. Subscribe will receive a message from the broker.

```
mosquitto_sub -h 'broker IP'-t 'topic'

#e.g.
mosquitto_sub -h 192.168.11.100 -t topic
```

![][link-mqtt_3]



## Appendix

- In Mosquitto versions earlier than 2.0 the default is to allow clients to connect without authentication. In 2.0 and up, you must choose your authentication options explicitly before clients can connect. Therefore, if you are using version 2.0 or later, refer to following link to setup 'mosquitto.conf' in the directory where Mosquitto is installed.

    - [**Authentication Methods**][link-authentication_methods]
    
    ![][link-mqtt_conf]


<!--
Link
-->

[link-thonny]: https://thonny.org/
[link-mosquitto]: https://mosquitto.org/download/

[link-thonny_config]:https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/Thonny_conf_1.png
[link-mqtt_1]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/MQTT_broker.png
[link-mqtt_2]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/MQTT_pub1.png
[link-mqtt_3]:  https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/MQTT_pub2.png
[link-mqtt_conf]: https://github.com/Wiznet/micropython-microbit-v2/blob/master/static/images/MQTT_conf.png

[link-authentication_methods]: https://mosquitto.org/documentation/authentication-methods/

