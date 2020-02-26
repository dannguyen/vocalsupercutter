from setuptools import setup, find_packages

setup(
    name='vocalsupercutter',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'boto',
        'click',
        'moviepy',
        'pytest',
        'youtube_dl',
    ],
    entry_points={
        'console_scripts': [
            'vocalcuts = vocalsupercutter.cli:main',
        ]
    },
)
