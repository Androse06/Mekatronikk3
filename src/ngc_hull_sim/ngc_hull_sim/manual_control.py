#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from ngc_interfaces.msg import Tau, SetPoints
import numpy as np
from pynput.keyboard import Key, Listener


class Teleop(Node):
    def __init__(self):
        super().__init__('teleop')
        #self.publisher_ = self.create_publisher(Twist, 'cmd_force', 10)
        self.timer_period_ = 0.1  # seconds
        self.timer_ = self.create_timer(self.timer_period_, self.publish_commands)
        self.send_cmd = self.create_publisher(Tau, 'tau_prop', 10)
        self.x = 0
        self.y = 0
        self.th = 0
        self.force_scalar_x = 1.0 * 1000#TODO legge disse inn som parametere  
        self.force_scalar_y = 1.0 *1000
        self.moment_scalar_z = 1.0 *1000
        self.can_print = True
        self.status = 0

        ## Initialize key states
        #self.key_states = {key: False for key in self.key_mapping.keys()}

        self.get_logger().info("Manual Controller node has started.")
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        self.keys_bindings = ["q", "e"]
        self.special_keys_bindings = [Key.up, Key.down, Key.left, Key.right]

    def publish_commands(self):
        self.tau = Tau()
        self.tau.surge_x= self.x * self.force_scalar_x
        self.tau.sway_y = self.y * self.force_scalar_y
        self.tau.heave_z = 0.0
        self.tau.roll_k = 0.0
        self.tau.heave_z = 0.0
        self.tau.yaw_n = self.th * self.moment_scalar_z
        self.send_cmd.publish(self.tau)
        
        self.print_cmd()

    def on_press(self, key):
 
        if self._is_special_key(key) and key in self.special_keys_bindings: 
            if key == Key.up:
                self.x += 1
                    
            elif key == Key.down:
                self.x -= 1

            elif key == Key.left:
                self.y -= 1
            elif key == Key.right:
                self.y += 1
        elif not self._is_special_key(key) and key.char in self.keys_bindings:
            if key.char == 'q':
                self.th -= 1
            elif key.char == 'e':
                self.th += 1
        else:
            print("not a valid key")

    def _is_special_key(self, key):
        try:
            key.char
            return False
        except AttributeError:
            return True

    def print_cmd(self):
        if self.can_print:
            print(f" X:{self.x}, Y: {self.y}, N: {self.th}")


class SetPointsTeleop(Node):
    def __init__(self):
        super().__init__('set_points_teleop')
        self.timer_period_ = 0.1  # seconds
        self.timer_ = self.create_timer(self.timer_period_, self.publish_commands)
        self.send_cmd = self.create_publisher(SetPoints, 'set_points_thrusters', 10)
        self.set_points = []
        self.n = 0
        self.pitch = 0
        self.agle = 0
        self.rps_scalar = 100
        self.pitch_scalar = 0.01
        self.angle_scalar = 0.01
        self.can_print = True

        self.get_logger().info("Manual set points controller node has started.")
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        self.keys_bindings = ["q", "e", "s", "w", "a", "d", "z", "c"]
        self.special_keys_bindings = [Key.up, Key.down, Key.left, Key.right]

    def publish_commands(self):
        self.set_points = SetPoints()
        self.n= self.n * self.rps_scalar
        self.pitch = self.pitch * self.pitch_scalar
        self.angle = self.angle * self.angle_scalar
        print("NB!: Temporary, hard coded to send set points to a dual controlable pitch and rudder configuration.")
        #TODO: change this to construct the set points based on th eThrusterSystem configuration.
        self.set_points = [self.n, self.pitch, self.angle, self.n, self.pitch, self.angle] 
        self.send_cmd.publish(self.set_points)
        
        self.print_cmd()

    def on_press(self, key):
 
        if self._is_special_key(key) and key in self.special_keys_bindings: 
            if key == Key.up:
                self.n += 1
            elif key == Key.down:
                self.n -= 1
            elif key == Key.left:
                self.angle -= 1
            elif key == Key.right:
                self.angle += 1
        elif not self._is_special_key(key) and key.char in self.keys_bindings:
            if key.char == 'w':
                self.pitch -= 1
            elif key.char == 's':
                self.pitch += 1
        else:
            print("not a valid key")

    def _is_special_key(self, key):
        try:
            key.char
            return False
        except AttributeError:
            return True

    def print_cmd(self):
        if self.can_print:
            print(f" set points: {self.set_points}")        


def main(args=None):
    try:
        rclpy.init(args=args)
        controller = Teleop()

        rclpy.spin(controller)
        controller.destroy_node()

        rclpy.shutdown()
    except KeyboardInterrupt:
        print("Not a valid key")

if __name__ == '__main__':
    main()