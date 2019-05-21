from setuptools import setup, find_packages

setup(
    name='browserup-proxy',
    version='0.1.0',
    description='A library for interacting with the Browserup Proxy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python'
    ],
    packages=find_packages(include=['browserupproxy*']),
    install_requires=[
        'requests>=2.9.1'
    ],
)
