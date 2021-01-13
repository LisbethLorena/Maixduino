# Untitled - By: Lisbeth Nunez - lun. nov. 30 2020

import sensor, image, time, lcd
import KPU as kpu
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224,224))

sensor.set_hmirror(0)
lcd.clear()

labels = ['Alto', 'Bajo', 'Medio']
task = kpu.load('/sd/frijol.kmodel')

kpu.set_outputs(task, 0, 1, 1, 3)

while(True):
    ban1 = time.ticks_ms()
    kpu.memtest()
    img = sensor.snapshot()
    fmap = kpu.forward(task, img)
    plist = fmap[:]
    pmax = max(plist)
    max_index = plist.index(pmax)

    ban2 = time.ticks_ms()
    tim = time.ticks_diff(ban2, ban1)

    a = img.draw_string(0,0, str(labels[max_index].strip()), color= (255,0,0), scale=2)
    a = img.draw_string(0,20, str(pmax), color= (255,0,0),scale=2)
    a = img.draw_string(0,40, str('Time_ms'), color= (255,0,0), scale=2)
    a = img.draw_string(0,60, str(tim), color= (255,0,0), scale=2)
    print((pmax, labels[max_index].strip()))
    a = lcd.display(img)
a = kpu.deinit(task)
