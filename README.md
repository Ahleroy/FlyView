# FlyView
FlyView: a bio-inspired optical flow truth dataset for visual navigation using panoramic stereo vision

This repository is an additional reference for the FlyView paper.

## Content of the repository

### Data generator

The script located in `datagenerator` allows to load a blender process in the background, load the trajectory from a CSV file, apply the static transform (X, Y, Z + Yaw rotation) and generate the data.

The command to run the `Data Generator` is located in the `datagenerator/command.txt` file.

### Data loader
The data loader is located in the `data_loader` folder.
It contains a minimal script example named  to load and visualize the EXR file containing the depth map, and the motion flow. This script is located in `data_loader/scripts/visualize_data.py`.

The data loader example requires `OpenEXR` and `Imath` to be installed.
OpenEXR can sometimes be difficult to install with `pip`. We suggest you have a look at the following links to download the wheel package.

https://excamera.com/sphinx/articles-openexr.html

https://www.lfd.uci.edu/~gohlke/pythonlibs/


## Paper

The pre-print paper is available here : Link not available yet
The published paper is available here : Link not available yet
The supplementary material is available here : Link not available yet

You can cite our paper using the following bibtex :

```
@article{Leroy2022,
	title = FlyView: a bio-inspired optical flow truth dataset for visual navigation using panoramic stereo vision,
	author = {Alix Leroy, Graham K. Taylor},
	year = {2022},
	keywords = {Optical flow, Ego-motion, Self-motion, Bioinspiration, optic flow,  visual navigation},
}
```

## Dataset

The dataset will be fully released on Zenodo and HuggingFace.

### Sample
A dataset sample can be downloaded here : https://doi.org/10.5281/zenodo.6653770

The dataset sample contains an example trajectory in a simple scene. 

## Code

The following scripts are included in the repository :
- Generate data with Blender using Python in `datagenerator`
- Load and visualize data in `data_loader`

## Licence
We do not own the right on the 3D assets we used. For each individual Blender scene, please refer to the source for more information.

## 3D Assets

### Barber shop
- Author : blender.org
- Original asset : https://svn.blender.org/svnroot/bf-blender/trunk/lib/benchmarks/cycles/barbershop_interior/
- License : CC-BY

### Bedroom
- Author : https://www.cgtrader.com/harshitverma1308
- Original asset : https://www.cgtrader.com/free-3d-models/interior/bedroom/bedroom-ca552be4-08d8-427b-8f5a-8391962983fe
- License : Royalty Free License

### Corridor
- Author : https://www.cgtrader.com/iamcyberalex
- Original asset : https://www.cgtrader.com/free-3d-models/space/spaceship/dead-space-sci-fi-corridor-by-cyberalex
- License : Royalty Free License

### Forest
- Author : https://www.cgtrader.com/ankitsarkar
- Original asset : https://www.cgtrader.com/free-3d-models/scanned/various/realistic-forest-model-for-blender
- License : Royalty Free License

### Kitchen
- Author : https://www.cgtrader.com/jpartsky
- Original asset : https://www.cgtrader.com/free-3d-models/interior/living-room/interior-b
- License : Royalty Free License

### Lakescape
- Author : https://www.cgtrader.com/mohdarbaaz3
- Original asset : https://www.cgtrader.com/3d-models/exterior/landscape/scene-lake
- License : Royalty Free License
- Price paid : $4.80

### Loft
- Author : https://www.cgtrader.com/jpartsky
- Original asset : https://www.cgtrader.com/free-3d-models/interior/living-room/project-b-54e79cb8-6763-471e-9d42-1e7e6cf01e14
- License : Royalty Free License

### Wine shop
- Author : https://www.cgtrader.com/harshitverma1308
- Original asset : https://www.cgtrader.com/free-3d-models/interior/other/old-wine-shop
- License : Royalty Free License

### Flat
- Author : Flavio Della Tommasa
- Original asset : https://download.blender.org/demo/cycles/flat-archiviz.blend
- License : CC-BY

### Sample
The example scene was homemade with basic Blender items. This scene is fully available online and allows future users to understand better the data generation and the setup of the camera system.
The sample scene is provided by the University of Oxford and released under the Creative Commons Attribution-NonCommercial-ShareAlike license (CC BY-NC-SA).
- Author : Alix Leroy
- Original asset : https://github.com/Ahleroy/FlyView
- License : CC BY-NC-SA