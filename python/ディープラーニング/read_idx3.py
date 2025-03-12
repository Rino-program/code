import struct
import numpy as np

def read_idx(filename):
    with open(filename, 'rb') as f:
        zero, data_type, dims = struct.unpack('>HBB', f.read(4))
        shape = tuple(struct.unpack('>I', f.read(4))[0] for d in range(dims))
        return np.frombuffer(f.read(), dtype=np.uint8).reshape(shape)

# ファイルのパスを指定
file_path = r'C:\Users\user.DESKTOP-89OCUK7\Desktop\MNIST\train-images-idx3-ubyte'

# データを読み込む
data = read_idx(file_path)

# データの形状と最初の要素を表示
print(f'Data shape: {data.shape}')
print(f'First element: {data[0]}')