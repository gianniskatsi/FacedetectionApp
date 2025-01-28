import pycuda.driver as cuda
import pycuda.autoinit
print("CUDA device count:", cuda.Device.count())
print("Device name:", cuda.Device(0).name())
