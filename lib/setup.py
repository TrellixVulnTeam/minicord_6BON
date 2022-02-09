from setuptools import find_packages, setup
setup(
    name='minicord',
    packages=find_packages(include=['minicord']),
    version='0.1.0',
    description='Custom Discord API library for Python',
    author='MiiDev',
    license='MIT',
		install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)