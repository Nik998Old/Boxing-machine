import time
import board # error when no device found?
import adafruit_adxl34x

i2c = board.I2C()  # uses board.SCL and board.SDA
accel = adafruit_adxl34x.ADXL345(i2c)

while True:
    #print("%f %f %f"%accelerometer.acceleration)
    print("x: {}\ty: {}\tz: {}".format(accel.raw_x,accel.raw_y,accel.raw_z))
    time.sleep(1)