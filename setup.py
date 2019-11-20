from setuptools import setup, find_packages

setup(name='test',
      version='0.0.0.4',
      author='Vaishnavesh 2019',
     description='Python packages assignment Auto-scheduling based on User Timezone',
     long_description=open('README.md').read(),
     license='see LICENSE.txt',
     keywords="python module package template engine setuptools",
     scripts=['task/task.py'],
     install_requires = ["python_version<'3.3'"],
     packages= find_packages())
)