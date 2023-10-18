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

The official NeurIPS 2022 link is available here: 
https://proceedings.neurips.cc/paper_files/paper/2022/hash/b4005da5affc3ba527dcb992495ecd20-Abstract-Datasets_and_Benchmarks.html

The published paper is available here:
https://proceedings.neurips.cc/paper_files/paper/2022/file/b4005da5affc3ba527dcb992495ecd20-Paper-Datasets_and_Benchmarks.pdf

The supplementary material is available here: 
https://proceedings.neurips.cc/paper_files/paper/2022/file/b4005da5affc3ba527dcb992495ecd20-Supplemental-Datasets_and_Benchmarks.zip

You can cite our paper using the following bibtex :

```
@inproceedings{Leroy2022,
 author = {Leroy, Alix and Taylor, Graham W},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {S. Koyejo and S. Mohamed and A. Agarwal and D. Belgrave and K. Cho and A. Oh},
 pages = {28110--28124},
 publisher = {Curran Associates, Inc.},
 title = {FlyView: a bio-informed optical flow truth dataset for visual navigation using panoramic stereo vision},
 url = {https://proceedings.neurips.cc/paper_files/paper/2022/file/b4005da5affc3ba527dcb992495ecd20-Paper-Datasets_and_Benchmarks.pdf},
 volume = {35},
 year = {2022}
}

```

## Dataset

NEW: THE DATASET WILL BE PUBLICLY RELEASED ON Nov. 30 2023. BOTH FLYVIEW AND ITS NATURAL DATASETS CAPTURED IN THE FLIGHT ARENA WILL BE RELEASED ON THAT DATE.

The dataset will be fully released on HuggingFace. Due to storage limitations on Zenodo, we cannot upload the entire dataset on this platform.
We are also exploring the upload of the data on Kaggle.

### Sample
A dataset sample can be downloaded here : https://doi.org/10.5281/zenodo.6653770

The dataset sample contains an example trajectory in a simple scene. 

## Code

The following scripts are included in the repository :
- Generate data with Blender using Python in `datagenerator`
- Load and visualize data in `data_loader`

## Generation Pipeline

### Inputs-Outputs

The data generation pipeline requires the following :
 - A CSV file containing the position of the camera system for each frame. The CSV file must contain a header `(X, Y, Z, q_w, q_x, q_y, q_z)` and each line represents a keyframe position and attitude.
 - A blender file in which the camera system is attached to a parent frame named `CamerasFrame`.
 - Output directories created and specified in the `OutputFile` nodes located in the `Compositing` tab of the Blender file. This is a manual step to do once for each blender environment that was not automated.

 When launching the data generation, the pipeline will generate the data in the output directories described above. In the first directory, the PNG images will be saved in a 16bits format. In the second directory, the Depth and Motion Flow will be saved in a single EXR file for each frame. See the `EXRFile` class located in the `data_loader` folder to read the file. An example to use it is located in `data_loader/scripts/visualize_data.py`.

 ### Modifying the trajectory

To modify the trajectory, you must generate your own in a CSV file in the format presented above (Header + `(X, Y, Z, q_w, q_x, q_y, q_z)` coordinates for each keyframe). The example scene `S10` uploaded on Zenodo provides a sample of a trajectory file.

### Modify the Environment

You can use any environment/scene to generate data with the current pipeline following these steps :

1 - In the new scene, you will need to add the `CameraFrame` existing in our example scene. You can directly copy and paste the entire frame (and its cameras) to your new scene.

2 - Add the nodes that are located in the `Compositing` tab of the example scene to your own `Compositing` tab. Do not forget to tick the `Use Nodes` box.

3 - Define the output directories as defined above

4 - In the `Output Properties` tab, make sure that the box `Stereoscopy` is ticked and to use the `Multi-view` option. Create and select the camera you want to use for the data generation. Because Blender 2.93 LTS fails to correctly generate the motion flow with multiple cameras at once, do make sure to have a single camera selected in this tab. We gave the following suffix to our cameras; Left => `_FishEye_Left`; Right => `_FishEye_right`; Panoramic => `_FishEye_Center_EquiRect`

5 - In the `Output Properties` tab, give a temporary directory to the `Output` option. This will prevent Blender from generating undesired files in your output directories.

### Modifying the Camera system

You can change each camera model by selecting the camera in the `CameraFrame` parent object. Then, in the `Object Data Properties` tab (green camera symbol), you can change the type of camera and its field of view.

You can change the image resolution in the `Output properties` tab.

Finally, you can directly modify the position of the cameras within the camera system by modifying the `Transform` in the `Object Properties` tab (Orange square). In particular, the baseline between the stereo cameras is located on the Y axis.




## 3D Assets

### Licence
We do not own the right on the 3D assets we used. For each individual Blender scene, please refer to the source for more information.

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