"""
picture.py
Author: Ed Dennison
Credit: 

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)

bodyShape = [
    (20,190), (10,180),(15,160),(60,150),(80,130),(140,135),(210,175),(200,190),(20,190)
    ]

print (bodyShape)
print (bodyShape * 2)

pcar = PolygonAsset(bodyShape, thinline, red)
mySprite = Sprite(pcar)
mySprite.position = (1000,400)


    
# add your code here /\  /\  /\


myapp = App()
myapp.run()
