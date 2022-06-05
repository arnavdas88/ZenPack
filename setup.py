import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ZenPack',
    version='0.0.1',
    author='Zeron Zensor Pack for Enterprise',
    author_email='arnav@zeron.one',
    # scripts=['bin/script1','bin/script2'],
    url='http://pypi.python.org/pypi/zenpack/',
    project_urls={
        "GitHub": "https://github.com/arnavdas88/zenpack",
    },
    license='LICENSE',
    description='Zeron zensor package manager.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests==2.26.0",
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Topic :: Utilities"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)