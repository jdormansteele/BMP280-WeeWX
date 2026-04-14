import syslog
import weewx
import time
import board
from weewx.wxengine import StdService
import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Standard pressure (hPa) at sea level
# bmp280.sea_level_pressure = 1013.25
# Adjusted for this station:
bmp280.sea_level_pressure = 1019.08

class BMP280Service(StdService):
    def __init__(self, engine, config_dict):
        super(BMP280Service, self).__init__(engine, config_dict)
        d = config_dict.get('BMP280Service', {})
        # Use the loop packet event as that allows data to still get into the WeeWX database
        self.bind(weewx.NEW_LOOP_PACKET, self.load_data)

    def load_data(self, event):
        try:
            self.get_bmp280(event)
        except Exception as e:
            syslog.syslog(syslog.LOG_ERR, "BMP280 service: cannot read value: %s" % e)

    # Get BMP280 data
    def get_bmp280(self, event):
        temperature = bmp280.temperature
        pressure = bmp280.pressure
        altitude = bmp280.altitude
        syslog.syslog(syslog.LOG_DEBUG, "BMP280 service: found temperature value of %s °C" % temperature)
        syslog.syslog(syslog.LOG_DEBUG, "BMP280 service: found pressure value of %s hPa" % pressure)
        syslog.syslog(syslog.LOG_DEBUG, "BMP280 service: found altitude value of  %s meters" % altitude)
        event.packet['pressure'] = float(pressure)
