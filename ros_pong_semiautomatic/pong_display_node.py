#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import pygame
import sys
import subprocess  # Linuxos always-on-top ablakhoz

class PongDisplayNode(Node):
    def __init__(self):
        super().__init__('pong_display_node')

        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = None

        self.ball = [400, 300]
        self.paddle_left = [50, 300]
        self.paddle_right = [750, 300]

        # ROS topicok
        self.create_subscription(Pose, '/turtle1/pose', self.update_ball, 10)
        self.create_subscription(Pose, '/turtle2/pose', self.update_paddle_left, 10)
        self.create_subscription(Pose, '/turtle3/pose', self.update_paddle_right, 10)

        # Pygame ablak
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Pong – Pygame Visualization")

        # 🐧 Linux: always on top (wmctrl)
        try:
            subprocess.Popen(['wmctrl', '-r', 'Pong – Pygame Visualization', '-b', 'add,above'])
        except Exception as e:
            print("⚠️ wmctrl nem érhető el vagy sikertelen:", e)

        # Frissítés 60 FPS
        self.create_timer(1/60, self.draw)

    def update_ball(self, msg):
        self.ball = [msg.x * 75, self.HEIGHT - msg.y * 50]

    def update_paddle_left(self, msg):
        self.paddle_left = [msg.x * 75, self.HEIGHT - msg.y * 50]

    def update_paddle_right(self, msg):
        self.paddle_right = [msg.x * 75, self.HEIGHT - msg.y * 50]

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.screen.fill((0, 0, 50))  # háttér

        # Labda
        pygame.draw.circle(self.screen, (255, 255, 0), (int(self.ball[0]), int(self.ball[1])), 10)

        # Bal ütő (zöld)
        pygame.draw.rect(self.screen, (0, 255, 0), (self.paddle_left[0]-5, self.paddle_left[1]-30, 10, 60))

        # Jobb ütő (piros)
        pygame.draw.rect(self.screen, (255, 0, 0), (self.paddle_right[0]-5, self.paddle_right[1]-30, 10, 60))

        pygame.display.flip()

def main(args=None):
    rclpy.init(args=args)
    node = PongDisplayNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        pygame.quit()

if __name__ == '__main__':
    main()
