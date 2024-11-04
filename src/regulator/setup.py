from setuptools import find_packages, setup

package_name = 'regulator'

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
    maintainer='gruppe5',
    maintainer_email='gruppe5@stud.ntnu.no',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kontroller = regulator.kontroller:main',
            'estimator = regulator.estimator:main',
            'allokering = regulator.allokering:main',
            'waypoint = regulator.waypoint:main',
            'signalbehandler = regulator.signalbehandler:main'
        ],
    },
)
