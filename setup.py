import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = ['requests >= 2.7.0']

if sys.version_info < (2, 7):
    warnings.warn(
        'Python 2.6 is not supported by Synapsepay. '
        'If you have any questions, please file an issue on Github or '
        'contact us at hello@synapsepay.com.',
        DeprecationWarning)
    install_requires.append('ssl')

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        import json
    except ImportError:
        install_requires.append('simplejson')

setup(
    name='synapsepay',
    cmdclass={'build_py': build_py},
    version='0.0.6',
    description='SynapsePay allows you to integrate bank payments into your applications',
    author='SynapsePay',
    author_email='hello@synapsepay.com',
    url='http://api.synapsepay.com/v2.0',
    packages=['synapsepay', 'synapsepay.apibits', 'synapsepay.resources', 'synapsepay.endpoints', 'synapsepay.test'],
    package_data={'synapsepay': ['data/ca-certificates.crt', '../VERSION']},
    install_requires=install_requires,
    test_suite='synapsepay.test',
    use_2to3=True)
