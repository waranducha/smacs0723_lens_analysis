import numpy as np
import matplotlib.pyplot as plt

# Simulate apparent magnitudes (NIRCam: F150W, F200W, F277W)
filters = ['F150W', 'F200W', 'F277W']
wavelengths = [1.5, 2.0, 2.77]  # Central wavelengths (microns)
source_mags = [27.5, 26.8, 26.5]  # Red, rising in F200W/F277W
lens_mags = [22.0, 21.8, 22.2]    # Flat, typical for elliptical galaxy

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(wavelengths, source_mags, 'ro-', label='Source ($z \\approx 7.6$)')
plt.plot(wavelengths, lens_mags, 'bs-', label='Lens ($z \\approx 0.5$)')
plt.scatter(wavelengths, source_mags, c='red', s=100)
plt.scatter(wavelengths, lens_mags, c='blue', s=100)

# Settings
plt.xlabel('Wavelength ($\mu$m)')
plt.ylabel('Apparent Magnitude (AB)')
plt.title('NIRCam Photometry of Northeast Peripheral Arc')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()  # Magnitudes: brighter upward
plt.savefig('photometric_redshift.pdf', format='pdf', bbox_inches='tight')
plt.close()
