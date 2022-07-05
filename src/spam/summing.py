import ctypes
import pathlib

# path of the shared library
libfile = pathlib.Path(__file__).parent / "csumlib.so"
csumlib = ctypes.CDLL(str(libfile))

type_vec3 = ctypes.POINTER(ctypes.c_double * 3)

csumlib.add_vec3.restype = type_vec3
csumlib.add_vec3.argtypes = [type_vec3, type_vec3]


def add(a: list, b: list) -> list:
    a_p = (ctypes.c_double * 3)(*a)
    b_p = (ctypes.c_double * 3)(*b)
    r_p = csumlib.add_vec3(a_p, b_p)

    return [l for l in r_p.contents]
