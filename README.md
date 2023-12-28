
<a name="Ethernet_Example_Getting_Started"></a>

Ethernet Example Getting Started
===========================


These sections will guide you through a series of steps from configuring development environment to running ethernet examples using the **micro:bit with WIZnet's ethernet products**.


- [Ethernet Example Getting Started](#ethernet-example-getting-started)
- [Hardware requirements](#hardware-requirements)
- [Development environment configuration](#development-environment-configuration)
- [Wiznet5K Library](#wiznet5k-library)
  - [Building](#building)
  - [Deploying firmware to the device](#deploying-firmware-to-the-device)
- [Ethernet example structure](#ethernet-example-structure)




<a name="hardware_requirements"></a>

# Hardware requirements


The Ethernet examples make use of the WIZnet Ethernet Products' Ethernet I/O module, which incorporates WIZnet's [__W5100S__][link-w5100s] or [__W5500__][link-w5500] Ethernet chip, in conjunction with the __micro:bit__ board.


### Pin Diagram

[link-microbit_pinmap]


| I/O  | Pin Name | Descri  ption                       |
| :--- | -------- | ------------------------------------|
| O    | P_16   | Connected to **CSn**  on WIZnet Chip|
| O    | P_15   | Connected to **MOSI** on WIZnet Chip|
| I    | P_14   | Connected to **MISO** on WIZnet Chip|
| O    | P_13   | Connected to **SCLK** on WIZnet Chip|
| O    | P_12   | Connected to **RSTn** on WIZnet Chip|
| I    | P_9    | Connected to **INTn** on WIZnet Chip|


<a name="development_environment_configuration"></a>

# Development environment configuration
To test the ethernet examples, the development environment must be configured to micro:bit and WIZnet.

- Required development environment
   - [Thonny](https://thonny.org/) (that makes it easier to use micropython) 
- If you must be need to compile the micropython ,your pc should be use Linux or Unix environment.

    To compile microbit-micropython, use a Docker image instead of setting up a separate environment. For instructions on how to use Docker, refer to the following Git page.
    - [docker-microbit-toolchain](https://github.com/carlosperate/docker-microbit-toolchain?tab=readme-ov-file#how-to-use-this-docker-image-with-github-codespaces)


------

<a name="wiznet5k"></a>
# Wiznet5K Library

<a name="Building"></a>
## Building

1. Download

If the ethernet examples are cloned, the library set as a submodule is an empty directory. Therefore, if you want to download the library set as a submodule together, clone the ethernet examples with the following Git command.

```cpp
/* Change directory */
// change to the directory to clone
$ cd [user path]

/* Clone */
$ git clone https://github.com/Wiznet/micropython-microbit-v2.git
```
2. Patch

Some libraries configured as submodules need to be manually patched using the Git commands found in their respective library directories. To do this, execute the shell script provided below. This action is only required to be performed once.

 ```cpp
$ cd micropython-microbit-v2
$ git submodule init
$ git submodule update
$ ./run_patchs.sh
 
 ```

3. compile

The build steps from this example have been obtained from [the project README](https://github.com/microbit-foundation/micropython-microbit-v2/blob/v2.0.0-beta.1/README.md).
Proceed with the compilation.

```cpp
# First we prepare the project, this initial docker command only has to be run once
$ docker run -v $(pwd):/home --rm ghcr.io/carlosperate/microbit-toolchain:latest make -C lib/micropython/mpy-cross
# Now we are ready to build using the Makefile in the src folder
$ docker run -v $(pwd):/home --rm ghcr.io/carlosperate/microbit-toolchain:latest make -C src

```

The compilation is finished, a `MICROBIT.hex`file will be generated in the `/src`directory.

<a name="Deploying firmware to the device"></a>
## Deploying firmware to the device

If you want to use the firmware without build, you can use the below firmware.

 - Releases : https://github.com/Wiznet/micropython-microbit-v2/releases/

Upload the `MICROBIT.hex` firmware to the micro:bit board. Connecting the micro:bit board to your PC. Copy the firmware into the microbit folder.

<a name="ethernet_example_structure"></a>

# Ethernet example structure

Ethernet examples are available at [micropython-microbit-v2/examples](https://github.com/Wiznet/RP2040-HAT-MicroPython/tree/main/examples) directory. As of now, following examples are provided.

- [**Loopback**][link-loopback]
- [**DHCP**][link-DHCP]
- [**HTTP**][link-HTTP]
  - [WebServer][link-WebServer]
  - [WebClient][link-WebClient]
- [**MQTT**][link-MQTT]
  - [Publish][link-MQTT_Pub]
  - [Subscribe][link-MQTT_Sub]

<a name="Ethernet_example_testing"></a>

_[▲ Back to Top](#Ethernet_Example_Getting_Started)_ 

<!--

Link

-->

[link-Installing Micropython]:https://thonny.org/
[link-w5100s]: https://docs.wiznet.io/Product/iEthernet/W5100S/overview
[link-w5500]: https://docs.wiznet.io/Product/iEthernet/W5500/overview

[link-microbit_pinmap]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/static/images/microbit_pinmap.png
[link-loopback]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Loopback
[link-DHCP]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/DHCP
[link-HTTP]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Http
[link-WebServer]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Http/server
[link-WebClient]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Http/client
[link-MQTT]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Mqtt
[link-MQTT_Pub]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Mqtt/Publish
[link-MQTT_Sub]:https://github.com/Wiznet/micropython-microbit-v2/tree/main/examples/Mqtt/Subscribe



