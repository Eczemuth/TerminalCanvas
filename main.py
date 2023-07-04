from Canvas import Canvas

canvas = Canvas(50, 50, bg='.')

canvas.draw_circle((25, 25), 12, opacity=0.4)
canvas.draw_circle((15, 15), 15, opacity=0.6)
canvas.draw_triangle((25, 10), (42, 32), (12, 25), opacity=0.8)
canvas.draw_rectangle((42, 15), 7, 10, opacity=1)

canvas.draw()
