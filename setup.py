from setuptools import find_packages, setup

setup(
    name='ursina',
    version='3.0.0',
    url='https://github.com/pokepetter/ursina',
    author='Petter Amland',
    author_email='pokepetter@gmail.com',
    license='MIT',
    keywords='game development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'panda3d',
        'pillow',
        'screeninfo',
    ],

    extras_require={
        'extras':  ['psd-tools3', 'imageio', 'psutil', 'hurry.filesize'],
    }
)
