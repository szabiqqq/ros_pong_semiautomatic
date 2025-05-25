from setuptools import setup
import os
from glob import glob

package_name = 'ros_pong_semiautomatic'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),  # Launch fájlok
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='szaboaron2003@gmail.com',
    description='ROS 2 turtlesim pong játék',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'ball_node = ros_pong_semiautomatic.ball_node:main',
        'paddle_node = ros_pong_semiautomatic.paddle_node:main',
        'right_paddle_node = ros_pong_semiautomatic.right_paddle_node:main',
        'pong_display_node = ros_pong_semiautomatic.pong_display_node:main',
    ],
}

)
