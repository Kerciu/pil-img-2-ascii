from converter import Converter

if __name__ == "__main__":
    """
    https://paulbourke.net/dataformats/asciiart/
    """
    image = "C:\\Users\\Kacper\\Desktop\\Folder\\Profilowe.png"
    asciiShades = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\\{\\}[]?-_+~<>i!lI;:,"^`\'."'
    convert = Converter(asciiShades)

    newWidth = 100
    newHeight = 100

    output_file = "KolosAndrzeja.txt"

    convert.scaleAndConvertToASCII(image, output_file, newWidth, newHeight)
