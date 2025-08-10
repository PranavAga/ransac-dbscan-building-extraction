*S25: Spatial Data Science*

**Project**
# Extracting Building Footprints from LiDAR Data
This repository contains the work and findings of a project focused on extracting building footprints from airborne LiDAR data. The project involves an analytical comparison of two leading unsupervised methods from the 11th SIGSPATIAL Cup competition and proposes a novel alternative pipeline.

## Project Overview
Building extraction from remote sensing data is crucial for applications like urban planning, disaster response, and population estimation. This project delves into unsupervised methods for this task, avoiding deep learning-based approaches. I analyze two top-performing solutions from the SIGSPATIAL Cup and introduce a new method combining RANSAC for plane detection and DBSCAN for spatial clustering.

## Methodologies Analyzed
I conducted a comparative analysis of the top two solutions from the competition, highlighting their different strategies:

### Method 1: Joint Boundary and Planar Filtering
- Workflow: Generates a Digital Surface Model (DSM) and then a Digital Terrain Model (DTM).

- Process: It computes a Normalized Digital Height Model (NDHM) and applies a series of filters (water body masking, morphological, planarity-based) to isolate and refine building structures.

- Key Feature: Treats the detection of planar surfaces and the delineation of boundaries as an integrated process.

### Method 2: Unsupervised Delineation via Ruggedness Metrics
- Workflow: Generates a DTM first and uses data voids to identify potential building locations.

- Process: Creates a DSM and uses the Terrain Ruggedness Index (TRI) and Vector Ruggedness Measure (VRM) to find flat rooftop areas. Footprints are validated based on rectangularity and Intersection over Union (IoU) with the roof areas.

- Key Feature: Handles boundary and plane detection sequentially and emphasizes the rectangularity of buildings.

### Proposed Solution: RANSAC + DBSCAN Pipeline
Building on insights from the analyzed methods, I developed a new pipeline:

1. Point Filtering: Non-ground points are selected from the LiDAR point cloud based on their classification.

2. Height Normalization: The height of each point is normalized by subtracting the ground elevation. A height threshold of 2.5 meters is applied to remove low-lying features.

3. Spatial Clustering (DBSCAN): The filtered high points are clustered using the DBSCAN algorithm to segment individual building structures.

4. Planar Detection (RANSAC): For each cluster, the RANSAC algorithm is used to robustly fit a plane, identifying points that belong to flat or sloped roof surfaces.

5. Footprint Generation (Alpha Shape): The identified planar points are projected onto a 2D plane, and the alpha-shape algorithm is used to generate the final polygonal building footprints.

## Results
The proposed RANSAC and DBSCAN-based method was implemented and tested on the available dataset.

- **Performance**: The pipeline achieved an average Intersection over Union (IoU) score of 0.06.

- **Analysis**: This result is significantly lower than the scores reported by the competition-winning methods. The primary challenges identified were sparse point coverage over buildings and the difficulty in handling irregular building shapes and structures with multiple planes.

## Scope for Improvement
Future work could focus on enhancing the accuracy and robustness of the proposed method by:

- Developing techniques to handle sparse point clouds more effectively.

- Incorporating multi-plane detection to model complex roof structures.

- Exploring hybrid approaches that combine geometric methods with machine learning techniques.

## Acknowledgments
I would like to thank Dr. K S Rajan and Dr. Kuldeep Kurte for their valuable guidance and reviews for the project.

## References
[1] Song, H., & Jung, J. (2022). Challenges in building extraction from airborne LiDAR data: ground-truth, building boundaries, and evaluation metrics. SIGSPATIAL '22.

[2] Xu, X. (2022). An unsupervised building footprints delineation approach for large-scale LiDAR point clouds. SIGSPATIAL '22.

[3] Tarsha-Kurdi, F., Landes, T., & Grussenmeyer, P. (2008). Extended RANSAC algorithm for automatic detection of building roof planes from LiDAR data. The photogrammetric journal of Finland.