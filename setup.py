from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
        name='filename_sanitizer',
        version='1.2',
        description='A python app that sanitizes filenames',
        long_description=readme(),
        url='https://github.com/ramitmittal/filename_sanitizer',
        author='Ramit Mittal',
        author_email='ramitmittal.k@gmail.com',
        license='GPLv3+',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        entry_points={
            'console_scripts': ['filename_sanitizer=filename_sanitizer.app:main']
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
