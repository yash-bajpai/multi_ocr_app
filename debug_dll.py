import ctypes
import os
import sys

# Path to site-packages
site_packages = os.path.join(os.getcwd(), '.venv', 'Lib', 'site-packages')
torch_lib = os.path.join(site_packages, 'torch', 'lib')
shm_dll = os.path.join(torch_lib, 'shm.dll')

print(f"Testing load of: {shm_dll}")

# Add torch/lib to PATH for dependencies
os.environ['PATH'] = torch_lib + ';' + os.environ['PATH']

try:
    lib = ctypes.CDLL(shm_dll)
    print("Successfully loaded shm.dll")
except Exception as e:
    print(f"Failed to load shm.dll: {e}")
    # Try loading dependencies explicitly
    deps = ['libiomp5md.dll', 'c10.dll', 'torch_cpu.dll', 'torch_python.dll']
    for dep in deps:
        dep_path = os.path.join(torch_lib, dep)
        try:
            print(f"Trying to load dep: {dep}")
            ctypes.CDLL(dep_path)
            print(f"  Loaded {dep}")
        except Exception as dep_e:
            print(f"  Failed to load {dep}: {dep_e}")
