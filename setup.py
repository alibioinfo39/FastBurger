from setuptools import setup, find_packages

setup(
    name='data-analysis-program',
    version='0.1',
    author='Licul Aragones',
    author_email='lic.aragones@gmail.com',
    description='A package for data analysis in bioinformatics',
    packages=find_packages(),
    install_requires=[
        'biopython',
        'numpy',
        'pandas',
        'pysam'
    ],
)
