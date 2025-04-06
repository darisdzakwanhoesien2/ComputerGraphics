import glm
import math


class MVPController:
    def __init__(self, callback_update, width: int, height: int):
        self.callback_update = callback_update
        self.width = width
        self.height = height
        self.position = glm.vec3(1, 1, -2)
        self.pitch = -0.5
        self.yaw = -0.5
        self.roll = 0.0
        self.speed = 0.4
        self.mouse_speed = 0.01
        self.fov = 90
        self.calc_view_projection()

    def calc_mvp(self, model_matrix=glm.mat4(1.0)):
        return self.projection_matrix * self.view_matrix * model_matrix

    def calc_view_projection(self):
        # 3. Implement the direction, right and up vectors here.
        # Currently none of them are correct
        pitch_deg = glm.degrees(self.pitch)
        yaw_deg = glm.degrees(self.yaw)

        # Calculate direction vector
        direction = glm.vec3(
            glm.cos(self.pitch) * glm.sin(self.yaw),
            glm.sin(self.pitch),
            glm.cos(self.pitch) * glm.cos(self.yaw)
        )
        self.direction = glm.normalize(direction)

        # Calculate right and up vectors
        self.right = glm.normalize(glm.cross(self.direction, glm.vec3(0.0, 1.0, 0.0)))
        self.up = glm.normalize(glm.cross(self.right, self.direction))

        # Create view matrix
        self.view_matrix = glm.lookAt(
            self.position,
            self.position + self.direction,
            self.up
        )

        # Create projection matrix
        aspect_ratio = self.width / self.height
        self.projection_matrix = glm.perspective(glm.radians(self.fov), aspect_ratio, 0.1, 1000)

    def on_keyboard(self, key: bytes, x: int, y: int):
        # 4. Set the corresponding actions based on the key here
        self.calc_view_projection()
        self.callback_update()

    def on_mouse(self, key: int, up: int, x: int, y: int):
        if key == 0 and up == 0:
            self.last_x = x
            self.last_y = y

    def on_mousemove(self, x: int, y: int):
        x_diff = self.last_x - x
        y_diff = self.last_y - y
        self.last_x = x
        self.last_y = y
        self.yaw -= x_diff * self.mouse_speed
        self.pitch -= y_diff * self.mouse_speed
        self.calc_view_projection()
        self.callback_update()

    def on_special_key(self, *args):
        pass

