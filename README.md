# ShellyPool
A package to integrate Shelly Devices with MQTT Brokers. This package intends to integrate Shelly devices within the network and manage it as a pool of devices that can be accessible through the MQTT Broker.

## Introduction
The package is intended to establish an MQTT interface with the Shelly device. The equipment attributes will be readable in the MQTT Broker through a topic in the form _/\<level0>/\<level1>/attribute_. The equipment will be located within a hierarchy of levels in the MQTT Broker, being the device located into 2 levels, typically _location_ and _equipment_, and within the equipment all the attributes of this device.

The Shelly devices have the option to configure them to get MQTT topics. However these topics are limited to _shellies/\<shelly_device>_ only and any other form of topic is not configurable on the device. Unless the library is modified.

The special attribute _/\<level0>/\<level1>/\<command>_ is serving as a special attribute to send commands to the device. The commands are those available from the library ___pyShelly___ and the function behind this package simply wraps a json command with its arguments. This json content is simply passed onto the package ___pyShelly___ and executes the command onto the equipment. The json document including the execution of a command is in the form:
<pre>
{
	"action": "name of the method",
	"args": "{
				"arg1": "value 1",
				"arg2": "value 2",
				"argN": "value N"
			}
}
</pre>

The name of the the method is one of the ___pyShelly___ methods. 

## Workflow diagram
The device and the MQTT have the following communication diagram
```mermaid
sequenceDiagram
Device ->> ShellyPool: Device Status
ShellyPool -->> MQTT Broker: Publish Topics
MQTT Broker ->> User Program: Status attributes 
User Program ->> MQTT Broker: { command, args }
MQTT Broker -->> ShellyPool: Subscribe Topics<br/>(command)
ShellyPool ->> Device: Function call<br/> Execution command
Note right of User Program: Async calls to execute<br/>commands on device.
```
## Configuration file
The package gives the possibility to configure parameters through a configuration file. This file can be, as an example, like this:
>[shelly]
>logfile=shellypool.log
>topic=[ "shellies/shellyplug-s-ABC123", "shellies/shellyht-ABC456"] ]
>room=[ "Living Room", "Kids Room" ]
>device=[ "Home Cinema", "HT Device" ]
>
>[broker]
>ip=127.0.0.1
>port=1883

The configuration file will be splitted into two areas:
- [shelly]: this area defines the devices as a serie of MQTT Topics from device. The room name for the device. And the device name. It also gives the chance to log data to a logfile.
- [broker]: this is the broker ip:port to connect to. This broker is to be setup apart from this package.


## How to install
To install the library just execute:
> pip install ShellyPool

## Example
> import sys
import ShellyPool
>
>def main():
>     # Configuration of the Shelly device
>     config = ShellyPool.ShellyConfig(sys.argv[1])
>     params_shelly = config.read(section="shelly")
>     params_broker = config.read(section="broker")
>
> print(f"Shelly Devices Pool Version {ShellyPool.__version__}")
    print(f"Creating Pool of Shelly Devices . . . ", end="")
    pool = ShellyPool.ShellyPool(params_broker['ip'], int(params_broker['port']))
    print(f"[ OK ]")
>
>    print(f"Running the pool")
    pool.start(
        eval(params_shelly['topic']), 
        eval(params_shelly['room']), 
        eval(params_shelly['device'])
        )
   > 
   > print(f"Finalizing Shelly Pool . . . [ OK ]")
    >
>if __name__ == "__main__":
> main()

## Release Notes
**0.1.1** - Initial release

# Credits
 - pyShelly - https://pypi.org/project/pyShelly/
