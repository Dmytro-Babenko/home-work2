from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='organize files in the folder',
    url='https://github.com/Dmytro-Babenko/home-work2/clean_folder',
    author='Dmytro Babenko',
    author_email='dmytro.babenko87@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']}
)