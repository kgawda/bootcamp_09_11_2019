import bmp
import argparse
import numpy as np
import scipy.ndimage

COLOR_VECTORS = {
    'r': [0, 0, 1],
    'g': [0, 1, 0],
    'b': [1, 0, 0],
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="input BMP file name")
    parser.add_argument('output', help="output BMP file name")
    parser.add_argument('--crop', help="crop to specified area: X1,Y1,X2,Y2")
    parser.add_argument('--select-color', help="select one color: red, green or blue")
    parser.add_argument('--black-and-white', action='store_true')
    parser.add_argument('--rotate', type=int, help="rotate by given number of degrees")
    parser.add_argument('--blur', action="store_true")

    args = parser.parse_args()

    data = bmp.read_bmp(args.input)

    if args.blur:
        data = scipy.ndimage.gaussian_filter(data, (3, 3, 0))

    if args.select_color:
        color = args.select_color.lower()[0]  # r, g or b
        data = data * np.array(COLOR_VECTORS[color])

    if args.black_and_white:
        data = data.sum(axis=2, keepdims=True) / 3
        data = data * np.ones(3)

    if args.crop:
        x1, y1, x2, y2 = args.crop.split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        data = data[y1:y2+1, x1:x2+1]

    if args.rotate:
        data = scipy.ndimage.rotate(data, args.rotate, prefilter=False)

    bmp.write_bmp(args.output, data)


if __name__ == '__main__':
    main()
