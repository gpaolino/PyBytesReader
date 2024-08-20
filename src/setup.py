from setuptools import setup, find_packages

setup(
      name='pybytesreader',
      version='0.0.2',
      description='PyBytesReader App',
      author='Paolo Guglielmino',
      author_email='gp.guglielminopaolo@gmail.com',
      url='https://github.com/gpaolino/pybytesreader',
      packages=find_packages(),
      entry_points={
          "console_scripts": ["pybytesreader=pybytesreader:main"],
      },
)