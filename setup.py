from setuptools import setup, find_packages

setup(
    name='my_tkinter_project',
    version='0.1',
    description='A simple Tkinter app',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'run_myapp=my_tkinter_package.gui:run_app',
        ],
    },
)
