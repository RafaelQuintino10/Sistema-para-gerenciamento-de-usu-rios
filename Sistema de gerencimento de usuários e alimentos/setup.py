from cx_Freeze import setup, Executable
import sys

arquivos = 'gerenciamentoicon.ico'

# Target executable
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    
configuracao = Executable(
    script='prototipo.py',
    icon='gerenciamentoicon.ico',
    base=base
)


# Dependencies
build_exe_options = {
    "packages": ["tkinter","customtkinter", "csv", "os"],  # Add your package dependencies here
    "includes": [],
    "include_msvcr": True
}


setup(
    name="Gerenciamento de usuários e alimentos",
    version="1.0",
    description = 'Este programa agiliza o gerenciamentos de usuários, alimentos, e faz a divisão igualitária dos mesmos',
    author = '',
    options={"build_exe": build_exe_options},
    executables=[configuracao]  # Replace with your script name
)
