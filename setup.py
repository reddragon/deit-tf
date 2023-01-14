import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='deit-tf',
    version='0.1',
    author='Gaurav',
    author_email='gaurav.menghani@gmail.com',
    description='DeIT-TF.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/reddragon/deit-tf',
    license='MIT',
    packages=['deit-tf'],
    # install_requires=['matplotlib'],
    package_data={
        # "deit-tf": ["fonts/*/*.*"]
    }
)
