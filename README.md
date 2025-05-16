# smacs0723_lens_analysis
Arco Periférico Noreste en SMACS J0723.3-7327
SMACS 0723 Gravitational Lens Analysis
This repository contains Python scripts for the analysis of a gravitational lens candidate, the Northeast Peripheral Arc, in SMACS J0723.3-7327, as described in the paper "Discovery of a New Gravitational Lens Candidate in the SMACS 0723 Cluster with JWST" (Gutierrez Peñuñuri, 2025, submitted to ApJ).
Scripts

annotate_image.py: Annotates the public JWST NIRCam image to highlight the arc.
lens_model.py: Generates the gravitational lens model diagram.
photometric_redshift.py: Creates the photometric redshift plot.
fits_processing.py: Processes hypothetical FITS data (requires real data from MAST).

Requirements
Install dependencies:
pip install -r requirements.txt

Usage
Run each script to generate figures:
python annotate_image.py
python lens_model.py
python photometric_redshift.py
python fits_processing.py

Data

Public image: https://webbtelescope.org/contents/media/images/2022-032/01G7WATC7XWBVMDM7CSTW5R8TK
FITS data: Download from MAST (Proposal 2736).

Citation
Please cite: Gutierrez Peñuñuri, C., 2025, ApJ (arXiv:XXXX.XXXXX, pending).
Contact
Carlos Cristobal Gutierrez Peñuñuri (carlos.cristobal.gutierrez@pemex.com)
