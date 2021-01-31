import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='guadian-reader',
    version='0.1.0',
    author='Otto Hermann',
    author_email='ojhermann@gmail.com',
    description='Endpoints for using The Guardian API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ojhermann/guardian_reader',
    packages=setuptools.find_packages(exclude=('test',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
