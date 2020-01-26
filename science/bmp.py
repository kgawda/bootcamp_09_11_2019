import struct
import typing

import numpy as np

HEADER_STRUCT = struct.Struct('<2sihhiiiihhiiiiibbh')


class BMPHeader(typing.NamedTuple):
    id: bytes
    size: int
    reserved_1: int
    reserved_2: int
    offset: int
    header_size: int
    width: int
    height: int
    number_of_color_planes: int
    bits_per_pixel: int
    compression_method: int
    image_size: int
    horizontal_resolution: int
    vertical_resolution: int
    number_of_colors: int
    number_of_important_colors: int
    rotation: int
    reserved_3: int

    def row_size(self):
        return (self.bits_per_pixel * self.width + 31) // 32 * 4

    def padding_size(self):
        return self.row_size() - (self.width * 3)

    @staticmethod
    def make_from_data(data: np.array):
        width = data.shape[1]
        height = data.shape[0]
        image_size = ((24 * width + 31) // 32 * 4) * height
        return BMPHeader(
            id=b'BM',
            size=image_size + 54,
            reserved_1=0,
            reserved_2=0,
            offset=54,
            header_size=40,
            width=width,
            height=height,
            number_of_color_planes=1,
            bits_per_pixel=24,
            compression_method=0,
            image_size=image_size,
            horizontal_resolution=2835,
            vertical_resolution=2835,
            number_of_colors=0,
            number_of_important_colors=0,
            rotation=0,
            reserved_3=0,
        )


def pixels(data):
    while len(data) >= 3:
        (b, g, r), data = data[:3], data[3:]
        yield b, g, r


def read_bmp(file_name: str) -> np.array:
    with open(file_name, 'rb') as f:
        header_data = f.read(HEADER_STRUCT.size)
        header_raw = HEADER_STRUCT.unpack(header_data)
        header = BMPHeader._make(header_raw)
        return np.array([
            [pixel for pixel in pixels(f.read(header.row_size()))] for _ in range(header.height)],
            dtype='int64',
        )


def write_bmp(file_name: str, data: np.array):
    header = BMPHeader.make_from_data(data)
    padding = header.padding_size()
    with open(file_name, 'wb') as f:
        f.write(HEADER_STRUCT.pack(*header))
        for row in data.astype('b'):
            f.write(bytes(row) + b'\x00' * padding)
