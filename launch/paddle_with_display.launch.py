#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # pygame vizualizáció
        Node(
            package='ros_pong_semiautomatic',
            executable='pong_display_node',
            name='pong_display_node',
            output='screen'
        ),
    ])
