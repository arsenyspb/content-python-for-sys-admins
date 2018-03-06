from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
        name='hrtool',
        version='0.1.0',
        description='HR tool exercise',
        long_description=readme,
        author='Arseny Chernov',
        author_email='arseny.chernov@gmail.com',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=[],
)


