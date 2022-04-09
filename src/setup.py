from setuptools import setup, find_packages
from rss_reader_folder.rss_reader import __rs_version__


setup(
    name='rssReader',
    version=__rs_version__,
    packages=find_packages(include=['rssReader']),
    include_package_data=True,
    entry_points={
        'console_scripts':
            ['rss_reader = rss_reader_folder.rss_reader:main']
        }
)
