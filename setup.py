#!/usr/bin/env python

from setuptools import setup



if __name__ == '__main__':

    try:
        with open('README.rst', 'r') as f:
            long_description = f.read()
    except:
        long_description = ''

    setup(name='remote_copy_and_execute',
            version='1.1.1',
            scripts=['remote_copy_and_execute'],
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            url='https://github.com/kata198/remote_copy_and_execute',
            maintainer_email='kata198@gmail.com',
            description='Tool to use SSH protocol to copy and execute arbitrary scripts/commands on a list of machines in parallel',
            long_description=long_description,
            license='GPLv3',
            install_requires=['python-subprocess2'],
            keywords=['ssh', 'scp', 'remote', 'copy', 'execute', 'shell', 'rcae', 'script', 'host'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                         'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.7',
                          'Programming Language :: Python :: 3',
                          'Programming Language :: Python :: 3.3',
                          'Programming Language :: Python :: 3.4',
                          'Topic :: Internet :: WWW/HTTP',
                          'Environment :: Console',
                          'Intended Audience :: System Administrators',
                          'Intended Audience :: Developers',
                          'Topic :: System :: Distributed Computing',
                          'Topic :: System :: Software Distribution',
                          'Topic :: Utilities',
            ]
    )

#vim: set ts=4 sw=4 expandtab
