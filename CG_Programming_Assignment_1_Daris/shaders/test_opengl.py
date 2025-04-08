import pyglet
from pyglet import gl

# Create a window (this creates the OpenGL context!)
window = pyglet.window.Window(width=400, height=300, caption='OpenGL Test')

@window.event
def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    print("OpenGL context is working!")

pyglet.app.run()
