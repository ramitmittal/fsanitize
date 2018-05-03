from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
        name='filename_sanitizer',
        version='0.9',
        description='A small python app that renames files for fun',
        long_description=readme(),
        url='https://github.com/ramitmittal/filename_sanitizer',
        author='Ramit Mittal',
        author_email='ramitmittal.k@gmail.com',
        license='GPLv3+',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        install_requires=['easyargs'],
        entry_points={
            'console_scripts': ['filename_sanitizer=filename_sanitizer.app:main']
        },
        python_requires='>=3.6',
    )
