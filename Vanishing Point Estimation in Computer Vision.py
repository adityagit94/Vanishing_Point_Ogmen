import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load and convert image
image = cv2.imread("C:\\Users\\aayus\\Downloads\\Estimate_vanishing_points_data\\Estimate_vanishing_points_data\\pexels-photo-10622719.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create a copy for drawing lines
image_with_lines = image.copy()

# Get image dimensions
height, width, _ = image.shape

# Define vanishing point somewhere above the center
vanishing_point = (width // 2, int(height * 0.6))

# Draw perspective lines
num_lines = 6
for i in range(num_lines):
    x_start = (i * width) // (num_lines - 1)
    y_start = height
    x_end, y_end = vanishing_point
    cv2.line(image_with_lines, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)

# Mark vanishing point
cv2.circle(image_with_lines, vanishing_point, 12, (255, 0, 0), -1)

# Plotting
plt.figure(figsize=(12, 6))

# Original image (no axes)
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Image with perspective lines and custom axes
plt.subplot(1, 2, 2)
plt.imshow(image_with_lines)
plt.title('Image with Perspective Lines')

# Custom X-axis (0 to 500) and Y-axis (300 to 0)
plt.xlim(0, 500)
plt.ylim(300, 0)  # Invert y-axis for image-like orientation

plt.xticks(np.arange(0, 501, 50))  # Ticks from 0 to 500 in steps of 50
plt.yticks([300, 250, 200, 150, 100, 50, 0])  # As requested

plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X-axis (pixels)')
plt.ylabel('Y-axis (pixels)')

plt.tight_layout()
plt.show()
