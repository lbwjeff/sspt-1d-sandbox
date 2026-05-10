"""
modules/numericspy

Description:
--- ---
Numerical type conventions used to in the CimLib code.

CimLib type mapping:
    CIMdouble -> double -> np.float64
    CIMint -> int -> np.int32 / Python int
    CIMbool -> bool -> bool
"""

import numpy as np

REAL_DTYPE = np.float64
INT_DTYPE = np.int32
BOOL_DTYPE = np.bool_

# Terminal display precision
PRINT_PRECISION = 6

# Output file formats
CIMLIB_OUTPUT_FORMAT = "%.12e" # Similar to CimLib style
CIMLIB_DELIMITER = "\t"

DEBUG_OUTPUT_FORMAT = "%.17e" # Whole precision for debuging
