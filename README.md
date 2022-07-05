# Python ctypes example project

This is an example Python package that builds ctypes-based cross-Python wheels
using cibuildwheel.

These wheels have the wheel tag `py3-none-PLATFORM`, meaning that one wheel
will work for any version of Python 3, including PyPy. So you'll end up with
one wheel per OS/architecture, which is considerably fewer than building one
for each Python.

Thanks to @himbeles for some of the code from their [sample ctypes
project](https://github.com/himbeles/ctypes-example)