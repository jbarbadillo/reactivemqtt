from setuptools import setup, find_packages
setup(
    name = 'reactivemqtt',
    version='1.0',
    packages = find_packages(),
    license = 'MIT',
    description = 'Examples for reactive mqtt',
    author = "Javier Barbadillo",
    author_email = "javier.barbadillo@gmail.com",
    url = 'https://github.com/jbarbadillo/reactivemqtt',
    download_url = 'https://github.com/jbarbadillo/reactivemqtt/archive/1.0.tar.gz',
    keywords = ['rx', 'mqtt'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)