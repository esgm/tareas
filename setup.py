from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tareas/__init__.py
from tareas import __version__ as version

setup(
	name="tareas",
	version=version,
	description="Plataforma de Gestion de Tareas",
	author="aei.gt",
	author_email="info@aei.gt",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
