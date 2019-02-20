import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

with open('req.txt') as f:
    requirements = f.read().splitlines()

test_requirements = [
    "ipdb",
]

setup(
    name='spark_optimizer',
    version='0.1.2',
    description='Optimize AWS EMR spark settings (spark-config-cheatsheet)',
    long_description=README + '\n\n' + CHANGES,
    author='Josip Delic',
    author_email='delijati@gmx.net',
    url='https://github.com/delijati/spark-optimizer',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='spark emr aws cluster yarn',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='test',
    tests_require=test_requirements,
    entry_points={
        "console_scripts": [
            "spark-optimizer = spark_optimizer.cli:main",
        ],
    }
)
