# TODO SCALE THE IMAGE
# TODO TRANSFORM TO THE SHADES OF GREY
# TODO MAP PIXELS TO ASCII
# TODO RENDER TEXT FILE

import os, sys
from PIL import Image
import numpy as np
from dataclasses import dataclass
from typing import List


@dataclass
class Converter:
    asciiShades: List[str]

    @staticmethod
    def openImage(fileHandle: str) -> Image:
        try:
            with Image.open(fileHandle) as im:  
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

        # Collect average
        average = self.getAverage(image)

        artTxt = []
        for i in range(0, rows):
            # Generate list of dimensions
            artTxt.append("")
            for j in range(0, cols):
                # Convert to ASCII
                pivot = int(average * len(self.asciiShades))
                artTxt.append(self.asciiShades[int(pivot / 255)])

        return "".join(artTxt)

    @staticmethod
    def renderTextFile(stringToCompute: str, fileHandle: str = None) -> None:
        with open(fileHandle, 'w') as f:
            f.write(stringToCompute)
    