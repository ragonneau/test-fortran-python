project(
    'my_project',
    'c',
    version: '1.0.0',
    meson_version: '>= 0.64.0',
)

# https://mesonbuild.com/Python-module.html
py_mod = import('python')
py3 = py_mod.find_installation(pure: false)
py3_dep = py3.dependency()

# Compilers
add_languages('fortran', native: false)

subdir('my_project')

