from converter import Converter
from argparse import ArgumentParser


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("--file-name", required=True)
    parser.add_argument("--cols", type=int, default=80, help="Determine number of collumns in ASCII art")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    """
    https://paulbourke.net/dataformats/asciiart/
    """
    args = parseArgs()
    asciiShades = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\\{\\}[]?-_+~<>i!lI;:,"^`\'."'
    convert = Converter(asciiShades)

    newWidth = 100
    newHeight = 100

    output_file = "ptoszek.txt"

    imageObj = convert.openImage(args.file_name)
    txt = convert.convertToASCII(imageObj, 0.42, args.cols)
    convert.renderTextFile(txt)
