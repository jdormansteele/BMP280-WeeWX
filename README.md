# BMP280-WeeWX 
This project provides a service definition file that supports use of a [Bosch BMP280](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) pressure sensor as a secondary data source for [WeeWX](http://www.weewx.com/) weather station software. The need for the service grew out of updates to a personal weather station I built in 2020. [My original setup](https://oneeyedman.net/posts/2020052301-weatherstation.html) involved an antiquated BMP180 braometric pressure sensor that became unmaintainable over time. My new setup uses a more accurate BMP280 sensor and belatedly enters the Python3 era.

Many (too many) personal weather stations take their barometric pressure measurements from a sensor in an indoor console. This creates a problem for WeeWX users who use software-defined radio (SDR) to collect the rest of their data from an outdoor instrument cluster. A solution is to install an additional sensor on the WeeWX server host and to merge its output with the radio data. However, this requires two pieces of software: 1) a driver to extract data from the sensor hardware, and 2) a service definition that wraps the data in loop packets readable by WeeWX. The driver software is already available from [Adafruit Industries](https://www.adafruit.com/), but a service definition for the BMP280 was missing until now.

The service definition was developed and tested for a weather station with the elements listed below. It is assumed that you have something funtionally equivalent before tackling the procedure described here. 
* An [Ambient Weather WS-2902A](https://ambientweather.com/mwdownloads/download/link/id/600) weather station kit (six years old and still going)
* A Raspberry Pi 3B+ (also old) running Debian GNU/Linux 6.1.21, Python 3.13.5, and python3-pip 25.1.1 (up-to-date as of April 2026)
* A [Nooelec NESDR Smart v4 SDR dongle](https://www.nooelec.com/store/sdr/sdr-receivers/smart.html)
* WeeWX 5.3.1 

# Installing the BMP280 hardware
The Raspberry Pi 3B+ circuit board includes a [general-purpose input/output (GPIO)](https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/) header that the BMP280 sensor can connect to. 

An [Adafruit BMP280 I2C or SPI Barometric Pressure & Altitude Sensor - STEMMA QT](https://www.adafruit.com/product/2651)
The [Adafruit_CircuitPython_BMP280](https://github.com/adafruit/Adafruit_CircuitPython_BMP280) driver

## Hardware driver setup

## Install the WeeWX service
* The BMP280-WeeWX service definition described here
* 
## Test



## Acknowledgements

This software is indebted to the following prior work.

* The [weewx_pi_sensors](https://github.com/eyesnz/weewx_pi_sensors) project by [eyesnz](https://github.com/eyesnz).
* The [Adafruit BMP280 Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout) tutorial and associated [driver](https://pypi.org/project/adafruit-circuitpython-bmp280/).
* [Customizing the WeeWX service engine: Adding a second data source](https://weewx.com/docs/4.10/customizing.htm#Adding_2nd_source) in the WeeWX developer documentation.


