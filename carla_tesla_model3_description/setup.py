from glob import glob
import os

from setuptools import setup

package_name = 'carla_tesla_model3_description'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name) + '/config', glob('config/*.yaml')),
        (os.path.join('share', package_name) + '/urdf', glob('urdf/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robo',
    maintainer_email='kirill.mitkovskii@gmail.com',
    description='tesla.model3 CARLA vehicle model description',
    license='MIT',
    entry_points={
        'console_scripts': [
        ],
    },
)
