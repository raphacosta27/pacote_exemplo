from setuptools import setup

setup(name='dev_aberto_raphael',
      version='0.1',
      author='Raphael Costa',
      author_email='raphaelamc1@al.insper.edu.br',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      install_requires=[
          'requests'
      ],
      scripts=['scripts/hello.py'],
      packages=['dev_aberto']
      )