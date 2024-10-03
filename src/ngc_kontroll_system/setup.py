from setuptools import find_packages, setup

package_name = 'ngc_kontroll_system'

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
    maintainer='nupix',
    maintainer_email='nupix@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "kontroller = ngc_kontroll_system.kontroller:main",
            "estimator = ngc_kontroll_system.estimator:main",
            "allokering = ngc_kontroll_system.allokering:main"
        ],
    },
)
