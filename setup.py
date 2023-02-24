from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gms/__init__.py
from gms import __version__ as version

setup(
	name="gms",
	version=version,
	description="This is simple Gym Management System that enables tracking memberships, locker booking, group classes, professional trainer subscription",
	author="GKDevs",
	author_email="gkdevs50@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
