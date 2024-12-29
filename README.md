Here's an optimized version of your `README.md`:

---

# Multi-Picture-in-One-Page

This project allows you to create a composite image from multiple smaller images. It is built with **HTML**, **CSS**, and **JavaScript**. While this approach may not be the most advanced, it is one of the simplest.

### Preview:
![Preview](https://github.com/user-attachments/assets/d7279d99-99e6-44bc-9898-222158bd9dc0)

## How to Use

### Step 1: Image Compression
Since this project involves multiple images, it's important to compress them to reduce load times, especially if they are large. We recommend using *ImageMagick*. 

#### Installation
First, you need to install ImageMagick on your system.

#### Compression Command
Once installed, navigate to your image directory and run the following command:

```bash
magick mogrify -quality 85 -path ./output *.jpg
```

This command will compress all `.jpg` images in the current directory and save the compressed images in the `./output` directory.

### Step 2: Updating the HTML with Image Filenames
You will need to replace the image names in `index.html` with the new filenames from the output directory.

#### Filename Extraction
Run the Python script `python.py` located in the output directory. It will extract all filenames, including their file extensions, and save them into a file called `filenames.txt`.

Open `filenames.txt`, copy all the lines, and paste them into the appropriate sections of the `index.html` file.

### Important Reminder:
**Do not forget to delete `python.py` from the filenames list in `filenames.txt`** before using it in the final HTML file!

---
The website will load slowly, that's acceptable, just take your time...
