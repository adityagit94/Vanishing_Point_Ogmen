# Vanishing Point Estimation Visualizer

A Python script to visually explore the concept of vanishing points in digital images.

## Description

This project offers a straightforward way to see how parallel lines in a real-world scene appear to meet at a single "vanishing point" when viewed in a two-dimensional image. The script takes an image, allows for a vanishing point to be set, and then draws lines to demonstrate this effect, helping to illustrate the principles of perspective.

## Core Idea

- **Image Loading:** Works with standard image files.
- **Vanishing Point Focus:** Highlights a user-defined vanishing point.
- **Perspective Lines:** Draws lines that converge towards this point to visually represent perspective.
- **Comparison View:** Shows the original image next to the one with the visual aids.

## Setup

To run this script, you'll need:
- Python 3.x
- The following Python libraries: OpenCV, NumPy, and Matplotlib.

You can typically install these with pip:
```bash
pip install --quiet opencv-python-headless scikit-learn
```

## Getting Started

1.  **Get the script:**
    Download or clone this repository.
    ```bash
    # If using git:
    # git clone [https://github.com/yourusername/Vanishing_Point_Ogmen.git](https://github.com/yourusername/Vanishing_Point_Ogmen.git)
    # cd Vanishing_Point_Ogmen
    ```
2.  **Choose your image:**
    In the `Vanishing Point Estimation in Computer Vision.py` script, you'll need to tell it which image to use. Look for a line like this and change the path:
    ```python
    # image_path = "path/to/your/image.jpg" 
    ```
    *(Note: For more flexible use, this could be adapted to take the image path as a command when you run the script.)*

3.  **Run it:**
    Execute the script from your terminal:
    ```bash
    python "Ogmen Vanishing Points.py"
    ```
    A window should appear, displaying your original image and the version with the perspective lines.

## How It Works (Conceptually)

The script essentially:
1.  Opens and prepares your chosen image.
2.  Uses a pre-set coordinate (defined in the script) as the vanishing point.
3.  Draws several lines from the lower portion of the image, all aiming towards this vanishing point.
4.  Marks the vanishing point with a circle for clarity.
5.  Presents both images so you can see the effect.

## Example Output
Before : ![vanishing-point-4468780__340](https://github.com/user-attachments/assets/1e36cb4e-7076-42a5-a4ca-cb78deb4a861)

After : ![image](https://github.com/user-attachments/assets/75fa77c4-d816-4220-84bc-b83d2c991c0f)



