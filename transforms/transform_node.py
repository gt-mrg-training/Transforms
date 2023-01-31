import rclpy
from rclpy.node import Node
from rclpy.time import Time
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from geometry_msgs.msg import TransformStamped, PoseStamped
from .geometry import do_transform_pose_stamped

class TransformNode(Node):

    def __init__(self):
        super().__init__('my_transform_node')

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.sub = self.create_subscription(PoseStamped, 
            'raw_poses', self.callback, 10)

        self.pub = self.create_publisher(PoseStamped,
            'transformed_poses', 10)
    
    def callback(self, msg):

        try:
            transform:TransformStamped = self.tf_buffer.lookup_transform(
                'wamv/base_link',
                'wamv/lidar_wamv_link',
                Time()                
            )
        except Exception as e:
            self.get_logger().info('Failed to lookup transform')
            return
        
        self.get_logger().info(str(transform))
        
        transformed_pose:PoseStamped = do_transform_pose_stamped(msg, transform)

        transformed_pose.header.frame_id = 'wamv/base_link'

        self.pub.publish(transformed_pose)


def main(args=None):
    rclpy.init(args=args)

    node = TransformNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()