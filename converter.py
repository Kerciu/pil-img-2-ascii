from PIL import Image
import numpy as np
from dataclasses import dataclass
from typing import List
import copy


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
            image = copy.deepcopy(image)
            if newWidth <= 0:
                newWidth = image.width
            if newHeight <= 0:
                newHeight = image.height

            scaled = image.resize((newWidth, newHeight))

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
        return np.average(np.array(greyImage))

    def convertToASCII(self, image: Image, scale: float) -> str:
        """
        Will take in prescaled image
        """
        # proportionFactor = 0.55
        W, H = image.size
        # tileHeight = int(H / scale)

        artTxt = []
        for y in range(0, H):
            for x in range(0, W):
                x_2 = x + 1
                y_2 = y + 1

                croppedImage = image.crop((x, y, x_2, y_2))
                average = self.getAverage(self.transformToGrey(croppedImage))

                pivot = int(average * (len(self.asciiShades) - 1) / 255)
                artTxt.append(self.asciiShades[pivot])

            artTxt.append('\n')
        return ''.join(artTxt)

    @staticmethod
    def renderTextFile(stringToCompute: str, fileHandle: str) -> None:
        try:
            with open(fileHandle, 'w') as f:
                f.write(stringToCompute)
        except IOError as e:
            print("Error writing to file:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            f.close()
