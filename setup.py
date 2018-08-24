from setuptools import setup

setup(
    name='django-storage-swift-epfl',
    version='0.1',
    description='OpenStack Swift storage backend for Django without cache',
    long_description=open('README.rst').read(),
    url='https://github.com/epfl-cede/django-storage-swift-epfl',
    author='EPFL CEDE',
    author_email='demakov.oleg@epfl.ch',
    license='MIT',
    packages=['swift-epfl'],
    install_requires=[
        'django-storage-swift>=1.2.19',
    ],
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
