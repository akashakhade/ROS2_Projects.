from setuptools import find_packages, setup

package_name = 'ak_py_pkg'

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
    maintainer='akash-s-akhade',
    maintainer_email='akash-s-akhade@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot1_news_station = ak_py_pkg.robot1_news_station:main',
            'smartphone = ak_py_pkg.smartphone:main',
            'number_publisher = ak_py_pkg.number_publisher:main',
            'number_counter = ak_py_pkg.number_counter:main',
            'add_two_ints_server = ak_py_pkg.add_two_ints_server:main',
            'add_two_ints_client_no_oop = ak_py_pkg.add_two_ints_client_no_oop:main',
            'add_two_ints_client = ak_py_pkg.add_two_ints_client:main',
            "hw_status_publisher = ak_py_pkg.hardware_status_publisher:main",
            "led_panel = ak_py_pkg.LED_Panel_node:main",
            "battery = ak_py_pkg.Battery:main"
        ],
    },
)
