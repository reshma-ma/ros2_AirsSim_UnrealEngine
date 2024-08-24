from setuptools import setup

package_name = 'airsim_car_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiwi02',
    maintainer_email='hiwi02@todo.todo',
    description='A ROS 2 package for controlling a car in a simulated environment.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'keyboard_input_publisher = airsim_car_controller.keyboard_input_publisher:main',
            'command_converter = airsim_car_controller.command_converter:main',
            'car_controller = airsim_car_controller.car_controller:main',
        ],
    },
)
