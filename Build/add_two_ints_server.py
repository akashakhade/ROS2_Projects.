#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts




class AddTwoIntsServerNode(Node): 
    #opertion = input("Enter the operation (+, -, *, /): ")
    def __init__(self):
        super().__init__("add_two_ints_server") 
        self.server_ = self.create_service(
            AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.get_logger().info("Add Two Ints server has been started.")
    
    def callback_add_two_ints(self, request: AddTwoInts.Request, response: AddTwoInts.Response): 
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + 
                               str(request.b) + " = " + str(response.sum))
        return response

        # a = request.a
        #opertion = request.operation
        #b = request.b
"""
        if opertion == "+":
            result = a + b
        elif opertion == "-":
            response = a - b
        elif opertion == "*":
            result = a * b
        elif opertion == "/":
            result = a / b

        
        self.get_logger().info(f"Recived: {a} {opertion} {b} = {result}")
        response.sum = result"""


        
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    