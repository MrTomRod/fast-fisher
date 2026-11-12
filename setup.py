# All metadata lives in pyproject.toml; this file only declares the Cython extension.
from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize('fast_fisher/fast_fisher_cython.pyx', language_level=3),
)
