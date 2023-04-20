# NumPy include directories
incdir_numpy = run_command(py3, [
    '-c',
    '''import os, numpy as np
try:
    print(os.path.relpath(np.get_include()))
except:
    print(np.get_include())
    ''',
], check: true).stdout().strip()
inc_np = include_directories(incdir_numpy)
incdir_f2py = incdir_numpy / '..' / '..' / 'f2py' / 'src'
inc_f2py = include_directories(incdir_f2py)
fortranobject_c = incdir_f2py / 'fortranobject.c'

# Dependencies for Fortran
fortranobject_lib = static_library(
    '_fortranobject',
    fortranobject_c,
    dependencies: py3_dep,
    include_directories: [inc_np, inc_f2py],
)
fortranobject_dep = declare_dependency(
    link_with: fortranobject_lib,
    include_directories: [inc_np, inc_f2py],
)

# fib2 module
fib2_module = custom_target(
    'fib2module',
    output : 'fib2module.c',
    input : 'fib2.pyf',
    command: [py3, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)
fib2 = py3.extension_module(
    'fib2',
    [fib2_module, 'fib1.f'],
    dependencies: fortranobject_dep,
    install : true,
    link_language: 'fortran',
    subdir: 'my_project',
)

# Python files
py3.install_sources([
    '__init__.py',
], subdir: 'my_project')

