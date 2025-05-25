#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
import random

class RightPaddleNode(Node):
    def __init__(self):
        super().__init__('right_paddle_node')

        self.publisher_ = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)
        self.spawn_client = self.create_client(Spawn, '/spawn')

        self.ball_pose = None
        self.paddle_pose = None

        # ⚖️ Reagál 0.3 másodpercenként
        self.create_timer(0.3, self.track_ball)

        self.create_subscription(Pose, '/turtle1/pose', self.update_ball_pose, 10)
        self.create_subscription(Pose, '/turtle3/pose', self.update_paddle_pose, 10)

        # Spawn turtle3
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Várakozás a /spawn szolgáltatásra...')

        request = Spawn.Request()
        request.x = 10.0
        request.y = 5.5
        request.name = 'turtle3'
        self.spawn_client.call_async(request)

    def update_ball_pose(self, msg):
        self.ball_pose = msg

    def update_paddle_pose(self, msg):
        self.paddle_pose = msg

    def track_ball(self):
        if self.ball_pose is None or self.paddle_pose is None:
            return

        msg = Twist()

        # Csak akkor mozog, ha a labda már közeledik
        if self.ball_pose.x > 6.5:
            # 🎯 Labda követése kisebb hibával
            target_y = self.ball_pose.y + random.uniform(-1.0, 1.0)
            dy = target_y - self.paddle_pose.y

            # Ha a különbség elég nagy, mozdul
            if abs(dy) > 0.5:
                msg.linear.y = 1.8 if dy > 0 else -1.8
            else:
                msg.linear.y = 0.0
        else:
            msg.linear.y = 0.0

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RightPaddleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
