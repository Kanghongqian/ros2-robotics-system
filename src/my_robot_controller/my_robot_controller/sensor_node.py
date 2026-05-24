import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class SensorNode(Node):

    def __init__(self):

        super().__init__('sensor_node')

        self.publisher_ = self.create_publisher(
            Float32,
            'distance_sensor',
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_distance
        )

    def publish_distance(self):

        msg = Float32()

        distance = random.uniform(10.0, 100.0)

        msg.data = distance

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Distance: {distance:.2f} cm'
        )

def main(args=None):

    rclpy.init(args=args)

    node = SensorNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()