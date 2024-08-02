---

# 🖼️ Image to ASCII Art Converter

## 📜 Description

A simple project covering the problem of transforming an image file into ASCII art. 🖼️➡️🔡

## ✍️ Author

Kacper Górski

## 🚀 Running

To run the program, follow these steps:

1. Make sure you have the Python interpreter installed on your computer. 🐍
2. Clone this project to your local machine:
   ```bash
   git clone https://github.com/your_username/image-to-ascii.git
   ```

3. Open a terminal or command prompt and navigate to the directory containing this project:
   ```bash
   cd image-to-ascii
   ```

4. Execute the following command:

   ```bash
   py ./mainApp.py --file-name <image_file_name> --output-file <output_file_name> [--dim-width <image_width>] [--dim-height <image_height>] [--erase-white]
   ```

   Where:
   - `<image_file_name>`: The path to the image file you want to convert to ASCII art. 🖼️
   - `<output_file_name>`: The name of the file where the generated ASCII art will be saved. 💾
   - `<image_width>` (optional): The optional width of the resulting image (in pixels). If not specified, the image will be scaled proportionally to the height. 📏
   - `<image_height>` (optional): The optional height of the resulting image (in pixels). If not specified, the image will be scaled proportionally to the width. 📐
   - `--erase-white` (optional): An option to remove white background from the generated ASCII art. ✂️

**Example:**

```bash
py ./mainApp.py --file-name image.jpg --output-file result.txt --dim-width 100 --dim-height 50 --erase-white
```

## 📝 Notes

- The `--dim-width` and `--dim-height` arguments are optional. If not provided, the image will be scaled proportionally. 📏
- The `--erase-white` option removes white background from the generated ASCII art. ✨
- Make sure to provide the correct path to the image file and the name of the output file. 📂

---

If you have any questions or suggestions, feel free to ask! 💬

---
