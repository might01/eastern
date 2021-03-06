from setuptools import setup, find_packages

setup(
    name='eastern',
    description='Simple Kubernetes Deployment',
    version='2.1.0',
    packages=find_packages(),
    url='https://github.com/wongnai/eastern',
    install_requires=[
        'Click==6.7',
        'click-log==0.2.1',
        'PyYAML==3.12',
        'stevedore==1.28.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['eastern = eastern.cli:cli'],
        'eastern.command': [
            'load? = eastern.formatter.overrides:load',
            'load! = eastern.formatter.overrides:load_strict',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: System :: Systems Administration',
    ])
