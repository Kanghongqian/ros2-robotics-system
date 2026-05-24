from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kk',
    maintainer_email='kk@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sensor_node = my_robot_controller.sensor_node:main',
            'subscriber_node = my_robot_controller.subscriber_node:main',
            'publisher_node = my_robot_controller.publisher_node:main',
            'robot_node = my_robot_controller.robot_node:main',
            'obstacle_avoidance_node = my_robot_controller.obstacle_avoidance_node:main',
            'motor_controller_node = my_robot_controller.motor_controller_node:main',
        ],
    },
)
