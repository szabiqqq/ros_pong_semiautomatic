import rclpy
from rclpy.node import Node

class GameManager(Node):
    def __init__(self):
        super().__init__('game_manager')
        self.get_logger().info('GameManager node elindult!')

def main(args=None):
    rclpy.init(args=args)
    node = GameManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
