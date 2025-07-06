# !/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStation(Node):
    def __init__(self): # MODIFY NAME
        super().__init__("robot1_news_station") # MODIFY NAME
        self.robot_name_ = "C3P0"
        self.publishers_ = self.create_publisher(String, "new_robot", 10)
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot News Station has been started.")

    def publish_news(self):
        msg = String()
        msg.data = "Hi this is " + self.robot_name_+ "as robot owner"
        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()