from cx_Freeze import setup, Executable
import os
import shutil

cwd = os.getcwd().split("/")
if cwd[len(cwd)-1] != "buildscripts":
    os.chdir(os.path.abspath("./buildscripts"))
    

guiFile = os.path.join("..", "srxdbepinexinstallerui")
flag = os.path.exists(f'{guiFile}.pyw')

# Dependencies are automatically detected, but some modules need help.
buildOptions = dict(
    include_files = [f'../themes/'],
    packages = [],
    excludes = [],
    # We can list binary includes here if our target environment is missing them.
    bin_includes = [
    ]
)

if (flag):
    shutil.copy(f"{guiFile}.pyw", f"{guiFile}.py")

executables = [
    Executable(
        f"{guiFile}.py",
        base = None,
        targetName = 'sample-app',
    )
]

setup(
    name='Sample Flask App',
    version = '0.1',
    description = 'Sample Flask App',
    options = dict(build_exe = buildOptions),
    executables = executables
)

if (flag):
    os.remove(f"{guiFile}.py")

