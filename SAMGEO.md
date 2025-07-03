## Using the geospatial version of Meta's Segment Anything for geospatial imaging: segment-geospatial, AKA the samgeo module

### Introduction

Meta's Segment Anything Model is described as "a new AI model from Meta AI that can "cut out" any object, in any image, with a single click". The potential uses of this for identifying geographic features from satellite imaging is a promising step towards environmental and geographical modeling of changes to our planet. One potential application of this is to quantify flooding from timelapsed imaging.

### Requirements

Assuming that one already has necessary geospatial imaging, the modules necessary to run samgeo are as follows:

* install python 3.12 and (via pip or equivalent processes) the python modules segment-geospatial, opencv-python, supervision, groundingdino-py, osr, and gdal
* if using windows, you may potentially need to download and install "gdal-3.10.2-cp312-cp312-win_amd64.whl" or the equivalent wheel for your system from https://github.com/cgohlke/geospatial-wheels/releases before installing gdal.
