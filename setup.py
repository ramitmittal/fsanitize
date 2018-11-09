
from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
        name='fsanitize',
        version='1.3',
        description='A python utility that sanitizes filenames',
        long_description=readme(),

        author='Ramit Mittal',
        author_email='ramitmittal.k@gmail.com',
        license='GPLv3+',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        entry_points={
            'console_scripts': ['fsanitize=fsanitize.app:main']
        },
        python_requires='>=3.6',
        extras_require={
            'dev': [
                'pytest',
                'pytest-pep8',
                'pytest-cov'
            ]
        }
    )
