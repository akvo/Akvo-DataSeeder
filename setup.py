import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AkvoDataSeeder",
    author="Akvo",
    author_email="tech.consultancy@akvo.org",
    description="Fast-API Datapoint seeder",
    keywords="akvo, data, helper, pypi, package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akvo/Akvo-DataSeeder",
    project_urls={
        "Documentation": "https://github.com/akvo/Akvo-DataSeeder",
        "Bug Reports": "https://github.com/akvo/Akvo-DataSeeder/issues",
        "Source Code": "https://github.com/akvo/Akvo-DataSeeder",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Database :: Database Engines/Servers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: FastAPI",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.5",
    install_requires=["fastapi", "pydantic", "sqlalchemy"],
    extras_require={
        "dev": ["check-manifest"],
        "test": ["httpx"],
    },
    entry_points={
        "console_scripts": [
            "akvo-dataseeder=AkvoDataSeeder.cli.migrate:main"
        ]
    },
)
