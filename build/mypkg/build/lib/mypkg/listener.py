import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cd(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
sub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
