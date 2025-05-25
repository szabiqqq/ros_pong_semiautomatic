#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class BallNode(Node):
    def __init__(self):
        super().__init__('ball_node')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.create_subscription(Pose, '/turtle1/pose', self.update_ball_pose, 10)
        self.create_subscription(Pose, '/turtle2/pose', self.update_paddle1_pose, 10)
        self.create_subscription(Pose, '/turtle3/pose', self.update_paddle2_pose, 10)

        self.timer = self.create_timer(0.1, self.move_ball)

        # 💨 Gyorsabb induló sebesség
        self.velocity_x = -3.5
        self.velocity_y = 0.0

        self.ball_pose = None
        self.paddle1_pose = None
        self.paddle2_pose = None
        self.game_over = False

    def update_ball_pose(self, msg):
        self.ball_pose = msg

    def update_paddle1_pose(self, msg):
        self.paddle1_pose = msg

    def update_paddle2_pose(self, msg):
        self.paddle2_pose = msg

    def move_ball(self):
        if self.game_over:
            return

        if self.ball_pose is None or self.paddle1_pose is None or self.paddle2_pose is None:
            return

        # 💥 Ütközés bal ütővel (turtle2)
        if self.distance(self.ball_pose, self.paddle1_pose) < 1.0 and self.velocity_x < 0:
            impact = self.ball_pose.y - self.paddle1_pose.y
            self.velocity_x = abs(self.velocity_x)
            self.velocity_y = impact * 0.7
            self.get_logger().info(f'💥 BAL ütés → vx={self.velocity_x}, vy={self.velocity_y:.2f}')

        # 💥 Ütközés jobb ütővel (turtle3)
        elif self.distance(self.ball_pose, self.paddle2_pose) < 1.0 and self.velocity_x > 0:
            impact = self.ball_pose.y - self.paddle2_pose.y
            self.velocity_x = -abs(self.velocity_x)
            self.velocity_y = impact * 0.7
            self.get_logger().info(f'💥 JOBB ütés → vx={self.velocity_x}, vy={self.velocity_y:.2f}')

        # ❌ VESZTÉS – kilép bal oldalon vagy alul/felül
        elif self.ball_pose.x <= 1.0 or self.ball_pose.y <= 1.0 or self.ball_pose.y >= 11.0:
            self.game_over = True
            self.get_logger().warn('❌ VESZTETTÉL! A labda elhagyta a pályát.')

        # ✅ GYŐZELEM – kilép jobb oldalon
        elif self.ball_pose.x >= 11.0:
            self.game_over = True
            self.get_logger().warn('✅ NYERTÉL! A labda elment jobbra.')

        # 🚀 Küldjük a sebességet
        msg = Twist()
        if not self.game_over:
            msg.linear.x = self.velocity_x
            msg.linear.y = self.velocity_y
        self.publisher_.publish(msg)

    def distance(self, a, b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def main(args=None):
    rclpy.init(args=args)
    node = BallNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
