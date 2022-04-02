from distutils.core import setup

from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "solution_cython_typing_with_c_types.pyx",
        compiler_directives={"language_level": "3"},
        annotate=True,
    ),
)
