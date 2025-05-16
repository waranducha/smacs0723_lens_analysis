from astropy.io import fits
from astropy.wcs import WCS
import matplotlib.pyplot as plt
import numpy as np

# Open hypothetical FITS file (replace with real file from MAST)
fits_file = 'smacs0723_nircam_f200w.fits'  # Download from MAST
hdul = fits.open(fits_file)
img_data = hdul[1].data  # Assume data in extension 1
wcs = WCS(hdul[1].header)  # World Coordinate System for RA/Dec
hdul.close()

# Create figure
plt.figure(figsize=(8, 8))
plt.imshow(img_data, origin='lower', cmap='viridis', norm='log')

# Annotate Northeast Peripheral Arc
# Position: +0.5' RA, +0.3' Dec = +30'' RA, +18'' Dec from cluster center
pixel_scale = 0.031  # arcsec/pixel (NIRCam approximate)
center_x, center_y = img_data.shape[1] / 2, img_data.shape[0] / 2
arc_x = center_x + (30 / pixel_scale)
arc_y = center_y + (18 / pixel_scale)  # Dec positive (up with origin='lower')

# Draw arc and segments
plt.scatter(arc_x, arc_y, c='red', marker='o', s=200, facecolors='none', label='Northeast Peripheral Arc')
plt.scatter([arc_x - 0.5/pixel_scale, arc_x + 0.5/pixel_scale], [arc_y, arc_y], c='red', marker='x', s=100)

# Annotate lens galaxy (~5'' southwest)
lens_x = arc_x - (5 * np.cos(np.deg2rad(45)) / pixel_scale)
lens_y = arc_y - (5 * np.sin(np.deg2rad(45)) / pixel_scale)
plt.scatter(lens_x, lens_y, c='blue', marker='s', s=100, label='Lens Galaxy ($z \\approx 0.5$)')

plt.legend()
plt.colorbar(label='Flux (MJy/sr)')
plt.xlabel('Pixels (RA)')
plt.ylabel('Pixels (Dec)')
plt.title('SMACS 0723 NIRCam F200W with Arc Annotated')
plt.savefig('nircam_fits_annotated.pdf', format='pdf', bbox_inches='tight')
plt.close()
