from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='lidar_to_base',
            arguments=['0.1', '0.0', '2.0', '0', '0', '0', 
                'wamv/base_link', 'wamv/lidar_wamv_link']
        ),
        Node(
            package='transforms',
            executable='test_data'
        ),
        Node(
            package='transforms',
            executable='transform'
        )
    ])
