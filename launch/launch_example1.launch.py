#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Turtlesim ablak
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
            output='screen'
        ),

        # Labda (turtle1)
        Node(
            package='ros_pong_semiautomatic',
            executable='ball_node',
            name='ball_node',
            output='screen'
        ),

        # Bal oldali ütő (turtle2)
        Node(
            package='ros_pong_semiautomatic',
            executable='paddle_node',
            name='paddle_node',
            output='screen'
        ),

        # Jobb oldali automata ütő (turtle3)
        Node(
            package='ros_pong_semiautomatic',
            executable='right_paddle_node',
            name='right_paddle_node',
            output='screen'
        ),
    ])
