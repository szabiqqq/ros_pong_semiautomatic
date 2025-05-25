#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

import sys
import termios
import tty
import select
import time  


def get_key():
    """Billentyű lenyomás azonnali érzékelése (ENTER nélkül)"""
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


class PaddleNode(Node):
    def __init__(self):
        super().__init__('paddle_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.spawn_client = self.create_client(Spawn, '/spawn')

        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Várakozás /spawn szolgáltatásra...')

        request = Spawn.Request()
        request.x = 1.0
        request.y = 5.5
        request.name = 'turtle2'
        self.spawn_client.call_async(request)

        self.timer = self.create_timer(0.1, self.check_keys)

    def check_keys(self):
        key = get_key()
        msg = Twist()

        if key == 'w':
            msg.linear.y = 2.0
        elif key == 's':
            msg.linear.y = -2.0

        if key in ['w', 's']:
            self.publisher_.publish(msg)
            self.get_logger().info(f'Billentyű: {key} → mozgatás {msg.linear.y}')


def main(args=None):
    global settings
    settings = termios.tcgetattr(sys.stdin)  # billentyű állapot mentése

    print("⏳ Várakozás 10 másodpercig a játék többi komponensére...")
    time.sleep(10)  # ✅ Várakozás, hogy a többi node elinduljon
    print("✅ Indul a paddle vezérlés!")


    rclpy.init(args=args)
    node = PaddleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)  # visszaállítás


if __name__ == '__main__':
    main()
