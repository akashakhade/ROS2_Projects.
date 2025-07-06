#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from ak_robot_interfaces.msg import LedPanelState
from ak_robot_interfaces.srv import SetLed

class LedPanelNode(Node): 
    def __init__(self):
        super().__init__("led_panel")
        self.led_states_ = [0, 0, 0]
        self.LED_publisher_ = self.create_publisher(
            LedPanelState, "led_panel_state", 10)
        self.led_states_timer_ = self.create_timer(
            5.0, self.publisher_led_states)
        self.set_led_service_ = self.create_service(
            SetLed, "set_led", self.callback_set_led)
        self.get_logger().info("LED panel node has been started.")
        
    def publisher_led_states(self):
        msg = LedPanelState()
        msg.led_states = self.led_states_
        self.LED_publisher_.publish(msg)

    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        led_number = request.led_number
        state = request.state

        if led_number >= len(self.led_states_) or led_number < 0:
            response.success = False
            return response
        if state not in [0, 1]:
            response.success = False
            return response
        
        self.led_states_[led_number] = state
        self.publisher_led_states()
        response.success = True
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    
