# BMP280-WeeWX 

UNDER CONSTRUCTION

This project provides a service definition file that supports use of a [Bosch BMP280](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) pressure sensor as a secondary data source for [WeeWX](http://www.weewx.com/) weather station software. The need for the service grew out of updates to a personal weather station I built in 2020. [My original setup](https://oneeyedman.net/posts/2020052301-weatherstation.html) involved an antiquated BMP180 braometric pressure sensor that became unmaintainable over time. My new setup uses a more accurate BMP280 sensor and belatedly enters the Python3 era.

Many (too many) personal weather stations take their barometric pressure measurements from a sensor in an indoor console. This creates a problem for WeeWX users who use software-defined radio (SDR) to collect the rest of their data from an outdoor instrument cluster. A solution is to install an additional sensor on the WeeWX server host and to merge its output with the radio data. However, this requires two pieces of software: 1) a driver to extract data from the sensor hardware, and 2) a service definition that wraps the data in loop packets readable by WeeWX. The driver software is already available from [Adafruit Industries](https://www.adafruit.com/), but a service definition for the BMP280 was missing until now.

The service definition was developed and tested for a weather station with the elements listed below. It is assumed that you have something functionally equivalent before tackling the procedure described here. 
* An [Ambient Weather WS-2902A](https://ambientweather.com/mwdownloads/download/link/id/600) weather station kit (six years old and still going)
* A Raspberry Pi 3B+ (also old) running Debian GNU/Linux 6.1.21, Python 3.13.5, and python3-pip 25.1.1 (up-to-date as of April 2026)
* A [Nooelec NESDR Smart v4 SDR dongle](https://www.nooelec.com/store/sdr/sdr-receivers/smart.html)
* WeeWX 5.3.1 

# Physically connect the BMP280 and enable I2C
The BMP280 sensor board that I used is the [Adafruit BMP280 I2C or SPI Barometric Pressure & Altitude Sensor - STEMMA QT](https://www.adafruit.com/product/2651). It needs to be wired to the Pi's [general-purpose input/output (GPIO)](https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/) header, and then the [I2C bus](https://en.wikipedia.org/wiki/I2C) must be enabled in software and tested. Complete the following steps.
<ol>
  <li>Adafruit includes a strip of header pins with its sensor board, pictured below. <image src="https://cdn-learn.adafruit.com/assets/assets/000/093/021/original/adafruit_products_BMP280_top_header.jpg"> Solder these to the board as shown in the Adafruit <a href="https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/assembly">tutorial</a>.</li>    
  <li>Connect the leads between the sensor board and the GPIO header. I recommend using a ribbon of 1/10-inch female-to-female connector cables <a href="https://www.amazon.com/Antrader-Breadboard-Dupont-Arduino-Raspberry/dp/B07RXK9SLW">like this one from Amazon</a>. The diagram below shows the pinouts for the the Raspberry Pi GPIO header. <image src="https://oneeyedman.net/images/pi-gpio-pinout.png"> The relevant pins for this application are 1, 3, 5, and 9. Connect them to the BMP280 board as shown in this table:
    <table>
      <thead>
        <tr>
         <th>GPIO header</th>
         <th>BMP280 board</th>      
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>(Pin 1) 3V3 power</td>
          <td>3Vo</td>
        </tr>
        <tr>
          <td>(Pin 3) GPIO 2 (SDA)</td>
          <td>SDI</td>
        </tr>
        <tr>
          <td>(Pin 5) GPIO 3 (SCL)</td>
         <td>SCK</td>
        </tr>
        <tr>
          <td>(Pin 9) Ground</td>
          <td>Ground</td>
        </tr>
      </tbody>
    </table>
    See also the assembly instructions in the Adafruit <a href="https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/assembly">tutorial</a>.</li> 
  <li>Install the I2C driver. On my Debian system, this meant installing three packages:
    <ul>
      <li>i2c-tools</li>
      <li>libi2c0</li>
      <li>python3-smbus</li>
    </ul>
  </li>
  <li>Set I2C device permissions. After an initial permission failure I temporarily fixed the problem by running 
    <pre># chmod 666 /dev/i2c-*</pre> as root. This did not persist through reboot. The permanent fix was to add the weewx user to the i2c group by doing 
    <pre># groupmod -U weewx -a i2c</pre> 
    as root and then rebooting.
  </li>
  <li>Confirm that the I2C interface works by using the following command.
  <pre>$ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- 77</pre>
The result shown indicates that the BMP280 is detected as device 0x77.
  
  </li>
</ol> 

## Install the driver for the sensor board
The [Adafruit_CircuitPython_BMP280](https://github.com/adafruit/Adafruit_CircuitPython_BMP280) driver can be downloaded directly from the GitHub site, but I couldn't get it working via that route. Instead I installed the driver and its dependencies with pip. That meant getting past the warning that pip packages might break my managed Python setup, contribute to global warming, and bring on a third Trump administration. I calculated that since this is a single-use Raspberry Pi system, I could risk those outcomes. If you, too, are brave enough, and you are root, install the driver as follows.
<pre># pip3 install adafruit-circuitpython-bmp280 --break-system-packages</pre>

## Install and configure the BMP280-WeeWX service definition
<ol>
<li>Copy to file. TO DO</li>
<li>Configure weewx.conf. TO DO</li>
</ol>

## Restart WeeWX and test
<ol>
<li>Restart weewx etc. TO DO</li>
</ol>

## Acknowledgements

This software is indebted to the following prior work.

* The [weewx_pi_sensors](https://github.com/eyesnz/weewx_pi_sensors) project by [eyesnz](https://github.com/eyesnz).
* The [Adafruit BMP280 Barometric Pressure + Temperature Sensor Breakout](https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout) tutorial and associated [driver](https://pypi.org/project/adafruit-circuitpython-bmp280/).
* In the WeeWX developer documentation, the section [Customizing the WeeWX service engine: Adding a second data source](https://weewx.com/docs/4.10/customizing.htm#Adding_2nd_source).


