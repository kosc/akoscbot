import setuptools

setuptools.setup(
    name="akoscbot",
    version="0.0.1",
    author="Kosenko Artem",
    author_email="hotkosc@gmail.com",
    description="Yet another telegram bot",
    url="https://github.com/kosc/akoscbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': [
            'akoscbot = koscbot:main'
        ],
    },
)
