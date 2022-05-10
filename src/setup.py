"""
Use that module to create package!
"""


from rss_reader_folder.rss_reader import __rss_version__
from setuptools import find_packages
from setuptools import setup


setup(
    name='rssReader',
    version=__rss_version__,
    packages=find_packages(include=['rssReader']),  # include all packages in this package
    include_package_data=True,
    entry_points={
        'console_scripts':
            ['rss_reader = rss_reader_folder.rss_reader:main']
    }
)
