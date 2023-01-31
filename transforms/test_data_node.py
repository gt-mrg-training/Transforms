import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class TestDataNode(Node):

    def __init__(self):
        super().__init__('test_data')

        self.pub = self.create_publisher(PoseStamped, 'raw_poses', 10)
    
        self.create_timer(1.0, self.callback)
    
    def callback(self):
        msg = PoseStamped()
        msg.pose.position.x = 1.0

        msg.header.frame_id = 'wamv/lidar_wamv_link'

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = TestDataNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()