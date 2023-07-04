# TerminalCanvas
A class that allow you to draw some primitives shape using coordinate geometry.
![image](https://github.com/Eczemuth/TerminalCanvas/assets/61462393/ecd4cea0-a4c8-4766-8c54-ab21c5c04433)

How to use
1. create canvas instance
```python
canvas = Canvas(w=50, h=50, bg='.')
```
w : width of canvas
h : height of canvas
bg : common element in your canvas

2. Use .draw_(primitive shape) to draw on canvas (these metohd won't show you any thing yet).
  - Draw circle will take in center and radius.
  ```python
  canvas.draw_circle((25, 25), 12, opacity=0.4)
  ```
  - Draw triangle will take in 3 points of triangle corner in any order.
  ```python
  canvas.draw_triangle((25, 10), (42, 32), (12, 25), opacity=0.8)
  ```
  - Draw rectangle will take in top-left corner positions, width and height of rectangle.
  ```python
  canvas.draw_rectangle((42, 15), 7, 10, opacity=1)
  ```
  Each draw function will take in 2 more optional arguments
  1. brush : The charactor you want to use to fill the shape.
  2. opacity : The opacity of the shape in uniform (0 - 1)
     The charactor that is used when working with opacity is from here -> http://paulbourke.net/dataformats/asciiart/

3. Use draw() to print the canvas
  ```python
  canvas.draw()
  ```
