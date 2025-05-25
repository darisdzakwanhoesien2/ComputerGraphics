import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from OpenGL.GLUT import *

# Global variables
rotation_speed = 5.0  # Degrees per second
last_time = glfw.get_time()
translate_offset = 0.0  # For x-axis oscillation

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light_position = [5.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

def draw_cube(size):
    glPushMatrix()
    glScalef(size, size, size)
    glutSolidCube(1.0)
    glPopMatrix()

def display(window):
    global last_time, translate_offset
    current_time = glfw.get_time()
    elapsed = current_time - last_time

    # Update rotation based on time (5 degrees per second)
    angle1 = rotation_speed * current_time
    angle2 = rotation_speed * current_time * 0.5  # Slower forearm rotation

    # Update translation (oscillate along x-axis, amplitude 1.0, frequency 0.5 Hz)
    translate_offset = np.sin(current_time * 2.0 * 3.14159 * 0.5) * 1.0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # Original Arm
    glPushMatrix()
    glTranslatef(translate_offset, 0.0, 0.0)  # Oscillating translation
    glColor3f(0.8, 0.8, 0.8)  # Base
    draw_cube(1.0)

    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glRotatef(angle1, 0.0, 0.0, 1.0)  # Rotate upper arm
    glTranslatef(0.0, 0.5, 0.0)
    glColor3f(0.5, 0.5, 0.5)  # Upper arm
    draw_cube(0.5)

    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)
    glRotatef(angle2, 0.0, 0.0, 1.0)  # Rotate forearm
    glTranslatef(0.0, 0.5, 0.0)
    glColor3f(0.3, 0.3, 0.3)  # Forearm
    draw_cube(0.3)
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()

    # Reflected Arm
    glPushMatrix()
    glScalef(-1.0, 1.0, 1.0)  # Reflection
    glTranslatef(-1.0 + translate_offset, 0.0, 0.0)  # Shift and oscillate
    glColor3f(0.8, 0.8, 0.8)  # Base
    draw_cube(1.0)

    glPushMatrix()
    glTranslatef(0.0, 1.0, 0.0)
    glRotatef(angle1, 0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.5, 0.0)
    glColor3f(0.5, 0.5, 0.5)  # Upper arm
    draw_cube(0.5)

    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)
    glRotatef(angle2, 0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.5, 0.0)
    glColor3f(0.3, 0.3, 0.3)  # Forearm
    draw_cube(0.3)
    glPopMatrix()

    glPopMatrix()
    glPopMatrix()

    glfw.swap_buffers(window)
    last_time = current_time

def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS and key == glfw.KEY_ESCAPE:
        glfw.set_window_should_close(window, True)

def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width / height if height != 0 else 1, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    if not glfw.init():
        return

    window = glfw.create_window(500, 500, "Robot Arm", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()

    glfw.set_key_callback(window, key_callback)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    # Initial viewport setup
    width, height = glfw.get_framebuffer_size(window)
    framebuffer_size_callback(window, width, height)

    
    glutInit()

    while not glfw.window_should_close(window):
        display(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()