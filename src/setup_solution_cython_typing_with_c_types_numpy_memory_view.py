from distutils.core import setup

import numpy as np
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "solution_cython_typing_with_c_types_numpy_memory_view.pyx",
        compiler_directives={"language_level": "3"},
        annotate=True,
    ),
    include_dirs=[np.get_include()],
)
