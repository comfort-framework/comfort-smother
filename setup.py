import os

from setuptools import setup, find_packages, Command


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.egg-info')

setup(
    name='COMFORT-smother',
    version='0.2.2',
    description='An abundance of coverage data',
    long_description='Coverage data collector for the COMFORT framework',
    url='https://github.com/comfort-framework/comfort-smother/tree/master/comfort-smother',
    packages=find_packages(),
    author='Fabian Trautsch',
    author_email='trautsch@cs.uni-goettingen.de',
    license='Apache',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'coverage>=4',
        'portalocker>=0.4',
        'six',
        'nose',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'comfortsmother = comfortsmother.nose_plugin:SmotherNose',
        ],
        'pytest11': [
            'comfortsmother = comfortsmother.pytest_plugin',
        ]
    },
    package_data={
        '': ["*.comfortsmother*"],
    },
    cmdclass={
        'clean': CleanCommand,
    }
)
