# TODO SCALE THE IMAGE
# TODO TRANSFORM TO THE SHADES OF GREY
# TODO MAP PIXELS TO ASCII
# TODO RENDER TEXT FILE

from PIL import Image
import numpy as np
from dataclasses import dataclass
from typing import List


@dataclass
class Converter:
    asciiShades: List[str]

    @staticmethod
    def openImage(fileHandle: str) -> Image:
        im = None
        try:
            im = Image.open(fileHandle)
            return im

        except FileNotFoundError:
            raise FileNotFoundError("File was not found")
        except Exception as e:
            raise Exception("There was an error while processing your image: ", e)

    @staticmethod
    def scaleImage(image: Image, newWidth: int, newHeight: int) -> Image:
        try:
            if newWidth <= 0:
                newWidth = 1
            if newHeight <= 0:
                newHeight = 1

            scaled = image.resize((newWidth, newHeight))
            return scaled
        except Exception as e:
            raise Exception("There was an error while processing your image: ", e)

    @staticmethod
    def transformToGrey(image: Image) -> Image:
        try:
            return image.convert('L')
        except Exception as e:
            raise Exception("There was an error while processing your image: ", e)

    @staticmethod
    def getAverage(greyImage: Image) -> np.array:
        image = np.array(greyImage)
        width, height = image.shape

        return np.average(image.reshape(width * height))

    def convertToASCII(self, image: Image) -> str:
        """
        Will take in prescaled image
        """
        rows, cols = image.size[0], image.size[1]

        artTxt = []
        for i in range(rows):
            # Generate list of dimensions
            rowText = ""
            for j in range(cols):
                # Convert to ASCII
                # Collect average
                average = self.getAverage(image)
                pivot = int(average * (len(self.asciiShades) - 1))
                rowText += (self.asciiShades[int(pivot / 255)])

            artTxt.append(rowText)

        return '\n'.join(artTxt)

    @staticmethod
    def renderTextFile(stringToCompute: str, fileHandle: str = None) -> None:
        with open(fileHandle, 'w') as f:
            f.write(stringToCompute)

    def scaleAndConvertToASCII(self, image_path: str, output_file: str, newWidth: int, newHeight: int) -> None:
        imgObject = self.openImage(image_path)
        scaled_image = self.scaleImage(imgObject, newWidth, newHeight)
        grey_image = self.transformToGrey(scaled_image)
        ascii_text = self.convertToASCII(grey_image)
        self.renderTextFile(ascii_text, output_file)
        imgObject.close()
