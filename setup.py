import sys
from cx_Freeze import setup, Executable

setup(
    name = "LibMan",
    version = "1.0",
    description = "library software",
    executables = [Executable("MainProg.py", base = "Win32GUI")])
