#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64  # Change this to the appropriate message type
from geometry_msgs.msg import Vector3  # Change this if needed

class TauPropulsionNode(Node):
    def __init__(self):
        super().__init__('tau_propulsion_node')

        # Subscriber to /eta_sim
        self.eta_subscriber = self.create_subscription(
            Float64,  # Change to the appropriate message type
            '/eta_sim',
            self.eta_callback,
            10
        )

        # Subscriber to /nu_sim
        self.nu_subscriber = self.create_subscription(
            Float64,  # Change to the appropriate message type
            '/nu_sim',
            self.nu_callback,
            10
        )

        # Publisher for /tau_propulsion
        self.tau_publisher = self.create_publisher(
            Float64,  # Change to the appropriate message type
            '/tau_propulsion',
            10
        )

        self.eta_data = None
        self.nu_data = None

        self.timer = self.create_timer(0.1, self.publish_tau_propulsion)
