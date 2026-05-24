import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MotorControllerNode(Node):

    def __init__(self):

        super().__init__('motor_controller_node')

        self.subscription = self.create_subscription(
            String,
            'robot_command',
            self.command_callback,
            10
        )

    def command_callback(self, msg):

        command = msg.data

        if command == 'STOP':

            self.get_logger().warning(
                'Motor STOPPED'
            )

        elif command == 'FORWARD':

            self.get_logger().info(
                'Motor MOVING FORWARD'
            )

def main(args=None):

    rclpy.init(args=args)

    node = MotorControllerNode()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()