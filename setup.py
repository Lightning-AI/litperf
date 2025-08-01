from setuptools import setup, find_packages

setup(
    name="litperf",
    version="0.0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A performance benchmarking tool for Lightning AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "isort",
        ],
    },
    entry_points={
        "console_scripts": [
            "litperf=litperf.cli:main",
        ],
    },
)
