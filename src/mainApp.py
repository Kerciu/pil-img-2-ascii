from converter import Converter
from argparse import ArgumentParser


def parseArgs():
    parser = ArgumentParser()
    parser.add_argument("--file-name", required=True)
    parser.add_argument("--output-file", required=True)
    parser.add_argument("--dim-width", type=int, default=-1, help="Determine width of ASCII art")
    parser.add_argument("--dim-height", type=int, default=-1, help="Determine height of ASCII art")
    parser.add_argument("--erase-white", action="store_true")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    """
    https://paulbourke.net/dataformats/asciiart/
    """

    args = parseArgs()
    asciiShades = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\\{\\}[]?-_+~<>i!lI;:,"^`\'."'
    convert = Converter(asciiShades)

    imageObj = convert.openImage(args.file_name)
    # Provide balance if one dim argument is not given

    args.dim_width = args.dim_height if args.dim_width < 0 else args.dim_width
    args.dim_height = args.dim_width if args.dim_height < 0 else args.dim_height

    imageObj = convert.scaleImage(imageObj, args.dim_width, args.dim_height)
    txt = convert.convertToASCII(imageObj, 0.42)
    if (args.erase_white):
        txt = txt.replace("\"", " ")
    convert.renderTextFile(txt, args.output_file)

    print(f"File rendered succesfully as {args.output_file}")
    if args.dim_width > 0 or args.dim_height > 0:
        print(f"Image scaled in following dimensions: {args.dim_width} x {args.dim_height}")
    print("White background removed") if args.erase_white else None
