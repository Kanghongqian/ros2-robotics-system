import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class ObstacleAvoidanceNode(Node):

    def __init__(self):

        super().__init__('obstacle_avoidance_node')

        self.subscription = self.create_subscription(
            Float32,
            'distance_sensor',
            self.distance_callback,
            10
        )

        self.command_publisher = self.create_publisher(
            String,
            'robot_command',
            10
        )

    def distance_callback(self, msg):

        distance = msg.data

        command_msg = String()

        if distance < 30.0:

            command_msg.data = 'STOP'

            self.command_publisher.publish(command_msg)

            self.get_logger().warning(
                f'Obstacle detected! STOP'
            )

        else:

            command_msg.data = 'FORWARD'

            self.command_publisher.publish(command_msg)

            self.get_logger().info(
                f'Path clear. FORWARD'
            )

def main(args=None):

    rclpy.init(args=args)

    node = ObstacleAvoidanceNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()