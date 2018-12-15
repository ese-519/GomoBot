# Find Circles Example
#
# This example shows off how to find circles in the image using the Hough
# Transform. https://en.wikipedia.org/wiki/Circle_Hough_Transform
#
# Note that the find_circles() method will only find circles which are completely
# inside of the image. Circles which go outside of the image/roi are ignored...

import sensor, image, time, math, pyb

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # grayscale is faster
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()
uart = pyb.UART(3, 115200)


def coordinate(x, y):
    for i in range (1, 10):
        for j in range (1, 10):
            if (((44 + 8 * i -2) < x < (42 + 8 * i +2)) and ((100 - 8 * i - 2) < y < (100 - 8 * i + 2))):
                print("coordinate: ",i, " ", j)


#used for automatic correction
#left = 50
#right = 50
#top = 50
#bottom = 50
#black = []
#for i in range(50):
    #clock.tick()
    #img = sensor.snapshot().lens_corr(1.8)
    #for c in img.find_circles(threshold = 3500, x_margin = 10, y_margin = 10, r_margin = 10,
            #r_min = 2, r_max = 10, r_step = 2):
        #img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
        #if(c.x() < left):
            #left = c[0]
            #print("left ", left)
        #if(c.x() > right):
            #right = c[0]
            #print("right ", right)
        #if(c.y() < bottom):
            #bottom = c[1]
            #print("bottom ", bottom)
        #if(c.y() > top):
            #top = c[1]
            #print("top ",top)

right = 128
bottom = 7
top = 105
left = 30
x_interval = (right - left) / 9;
y_interval = (top - bottom) / 9;


while(True):
    clock.tick()
    img = sensor.snapshot().lens_corr(1.8)

    for c in img.find_circles(threshold = 3200, x_margin = 10, y_margin = 10, r_margin = 10,
            r_min = 2, r_max = 10, r_step = 2):
        img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
        x_axis = math.ceil((c[0] - left) / x_interval)
        y_axis = math.ceil((c[1] - bottom) / y_interval)
        print("pixel ", c[0], " ", c[1])
        #coordinate(c[0],c[1])
        print("x ",x_axis, "y ",y_axis)
        print("\n")
        #if (x_axis, y_axis) not in black:
             #black.append((x_axis,y_axis))
        print("new: x ",x_axis, "y ",y_axis)
        print("\n")
        uart.write("%s"%x_axis)
        time.sleep(500)
        #uart.write(",")
        #time.sleep(500)
        #uart.write(" ")
        #time.sleep(500)
        uart.write("%s"%y_axis)
        time.sleep(500)


