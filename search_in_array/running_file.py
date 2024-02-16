import sys
import execution_time_algorithm
import algorithms
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
size = []
time_1 = []
time_2 = []
time_3 = []

if __name__ == "__main__":
    table = execution_time_algorithm.take_execution_time(10000,100000,10000,25)
    for row in table:
        size.append(row[0])
        time_1.append(row[1])
        time_2.append(row[2])
        time_3.append(row[3])
    
    bar_width = 10

    time_1_x = [x for x in size]
    time_2_x = [x - bar_width for x in size]
    time_3_x = [x + bar_width for x in size]

    plt.bar(time_1_x, time_1, bar_width, color = 'b', label = 'Linear search')
    plt.bar(time_2_x, time_2, bar_width, color = 'g', label = 'Binary search')
    plt.bar(time_3_x, time_3, bar_width, color = 'r', label = 'Ternary search')

    plt.xlabel = ('Array size')
    plt.ylabel = ('Execution time [ms]')

    plt.legend()

    plt.show()

"""     width = 600
    heigth = 600
    GREY = (230,230,230)
    BACKGROUND = (255,255,255)

    row_container_1 = pg.sprite.Group()
    row_container_2 = pg.sprite.Group()
    row_container_3 = pg.sprite.Group()

    screen = pg.display.set_mode([width,heigth])
    table = execution_time_algorithm.take_execution_time(10000,100000,10000,25)
    for row in table:
        row_container_1.add(row[1])
        row_container_2.add(row[2])
        row_container_3.add(row[3])
                

    pg.init()
    chart = pg.Surface((width//4, heigth//4))
    chart.fill(GREY)
    chart.set_alpha(230)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    screen.fill(BACKGROUND)

    chart_heigth = chart.get_height()
    chart_width = chart.get_width()



    pg.quit()
 """