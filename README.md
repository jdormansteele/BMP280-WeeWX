# BMP280-WeeWX 
This project offers a service definition to add a [Bosch BMP280 pressure sensor](https://) as a secondary data source for [WeeWX](http://www.weewx.com/) weather station software running on a Raspberry Pi 3b+. This service grew out of a 2020 COVID project when I set up a personal weather station, deployed a WeeWX server, and used a Software Defined Radio (SDR) dongle to connect the two. [My original setup](https://oneeyedman.net/posts/2020052301-weatherstation.html) involved an antiquated BMP180 sensor that became unmaintainable over time. The new setup uses a more accurate sensor and belatedly enters the Python3 era.

Many (too many) personal weather stations take their barometric pressure measurements from a sensor in an indoor console. This creates a problem for WeeWX users who use SDR to collect the rest of their data from an outdoor instrument cluster. A solution is to install an additional sensor on the WeeWX server host and to merge its output with the radio data. However, this requires two pieces of software: 1) a driver to extract data from the sensor hardware, and 2) a service definition that wraps the data in loop packets readable by WeeWX. The driver software is already available from Adafruit. A service definition specific to the BMP280 was missing until now.

TO DO

***Acknowlegments***

This software is indebted to the following prior work.

* The [weewx_pi_sensors](https://github.com/eyesnz/weewx_pi_sensors) project by [eyesnz](https://github.com/eyesnz).
* The [Adafruit BMP280 Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout) tutorial and associated [driver](https://pypi.org/project/adafruit-circuitpython-bmp280/).
* [Customizing the WeeWX service engine: Adding a second data source](https://weewx.com/docs/4.10/customizing.htm#Adding_2nd_source) in the WeeWX developer documentation.


