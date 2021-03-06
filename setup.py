#Setting up pi settings for our robot companion

from setuptools import setup

setup(name='stubby_eui',
	version='1.0',
	description='CompE Stub Library',
	author='Cassandra Chow',
	author_email='cc5718@nyu.edu',
	url='https://github.com/ca-chow/DesktopPet_Eui',
	py_modules=['stubby_eui', 'app'],
	install_requires=['Adafruit-SSD1306', 'PyYAML']
	)



