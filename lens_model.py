import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Define lens and source parameters
theta_E = 1.5  # Einstein radius in arcseconds
e = 0.3  # Ellipticity
gamma = 0.1  # External shear
source_pos = np.array([0.5, 0.0])  # Source position (arcsec)
lens_pos = np.array([0.0, 0.0])  # Lens position

# Simplified lens equation for eSIS + shear
def lens_equation(beta, theta_E, e, gamma):
    phi = np.arctan2(beta[1], beta[0])
    beta_r = np.sqrt(beta[0]**2 + beta[1]**2)
    theta1 = beta + np.array([theta_E * (1 - e * np.cos(2 * phi)) - gamma * beta_r, 
                             -theta_E * e * np.sin(2 * phi) + gamma * beta_r])
    theta2 = beta - np.array([theta_E * (1 - e * np.cos(2 * phi)) - gamma * beta_r, 
                             -theta_E * e * np.sin(2 * phi) + gamma * beta_r])
    return theta1, theta2

# Compute image positions
image1, image2 = lens_equation(source_pos, theta_E, e, gamma)

# Critical curve (approximate for eSIS)
theta = np.linspace(0, 2 * np.pi, 100)
crit_x = theta_E * np.sqrt(1 - e) * np.cos(theta)
crit_y = theta_E * np.sqrt(1 + e) * np.sin(theta)

# Caustic (approximate mapping to source plane)
caustic_x = crit_x * (1 - gamma) - crit_y * gamma
caustic_y = crit_y * (1 + gamma) - crit_x * gamma

# Create plot
plt.figure(figsize=(8, 8))
ax = plt.gca()

# Plot lens (elliptical galaxy)
lens = Ellipse(lens_pos, width=2 * theta_E * np.sqrt(1 - e), height=2 * theta_E * np.sqrt(1 + e),
               angle=0, fill=False, color='black', linestyle='--', label='Lens (eSIS)')
ax.add_patch(lens)

# Plot source
plt.scatter(source_pos[0], source_pos[1], c='green', marker='*', s=200, label='Source ($z \\approx 7.6$)')

# Plot images
plt.scatter([image1[0], image2[0]], [image1[1], image2[1]], c='red', marker='o', s=100, label='Images')

# Plot observed positions
obs_pos1 = image1 + np.random.normal(0, 0.1, 2)
obs_pos2 = image2 + np.random.normal(0, 0.1, 2)
plt.scatter([obs_pos1[0], obs_pos2[0]], [obs_pos1[1], obs_pos2[1]], c='black', marker='x', s=100, label='Observed Positions')

# Plot critical curve
plt.plot(crit_x, crit_y, 'b-', label='Critical Curve')

# Plot caustic
plt.plot(caustic_x, caustic_y, 'g-', label='Caustic')

# Settings
plt.xlabel('RA Offset (arcsec)')
plt.ylabel('Dec Offset (arcsec)')
plt.title('Gravitational Lens Model of Northeast Peripheral Arc')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Save plot
plt.savefig('lens_model.pdf', format='pdf', bbox_inches='tight')
plt.close()
