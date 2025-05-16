import requests
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Download public SMACS 0723 image
url = "https://stsci-opo.org/STScI-01G7WATC7XWBVMDM7CSTW5R8TK.jpg"
response = requests.get(url, stream=True)
with open("smacs0723_nircam.jpg", "wb") as f:
    f.write(response.content)

# Open image
img = Image.open("smacs0723_nircam.jpg")
img_array = np.array(img)

# Create figure
plt.figure(figsize=(8, 8))
plt.imshow(img_array)

# Annotate Northeast Peripheral Arc
# Assume image center as cluster center, approximate scale: ~0.031''/pixel
# Position: +0.5' RA, +0.3' Dec = +30'' RA, +18'' Dec
pixel_scale = 0.031  # arcsec/pixel (NIRCam)
center_x, center_y = img_array.shape[1] / 2, img_array.shape[0] / 2
arc_x = center_x + (30 / pixel_scale)  # RA positive (left in astronomical images)
arc_y = center_y - (18 / pixel_scale)  # Dec positive (up)

# Draw arc (red circle for arc center)
plt.scatter(arc_x, arc_y, c='red', marker='o', s=200, facecolors='none', label='Northeast Peripheral Arc')
# Draw segments (approximated as points at ±0.5'' from center)
plt.scatter([arc_x - 0.5/pixel_scale, arc_x + 0.5/pixel_scale], [arc_y, arc_y], c='red', marker='x', s=100)

# Annotate lens galaxy (~5'' southwest)
lens_x = arc_x - (5 * np.cos(np.deg2rad(45)) / pixel_scale)
lens_y = arc_y + (5 * np.sin(np.deg2rad(45)) / pixel_scale)
plt.scatter(lens_x, lens_y, c='blue', marker='s', s=100, label='Lens Galaxy ($z \\approx 0.5$)')

plt.legend()
plt.axis('off')
plt.title('SMACS 0723 with Northeast Peripheral Arc Annotated')
plt.savefig('nircam_arc_annotated.pdf', format='pdf', bbox_inches='tight')
plt.close()
