import numpy as np
import geopandas as gpd
from tqdm import tqdm

def calc_iou(gdf_groundtruth, gdf_predict):
    """Calculates intersection over union (iou) score.

    Args:
      gdf_groundtruth: Groundtruth GeoDataFrame of polygons.
      gdf_predict: Predicted GeoDataFrame of polygons.

    Returns:
      Intersection Over Union (IOU) Score.

    """
    
    intersect = gdf_groundtruth.dissolve().intersection(gdf_predict.dissolve()).area
    union = gdf_groundtruth.dissolve().union(gdf_predict.dissolve()).area
    iou = intersect / union
    
    return iou[0]

def calc_metrics(groundtruth_file, predict_file):
    """Reads geojson files, and calculates IOU.

    Args:
      groundtruth_file: Geojson file for groundtruth.
      predict_file: Geojson file for predictions

    Returns:
      Intersection over union (IOU) score with punishment.
    """
    
    gdf_groundtruth = gpd.read_file(groundtruth_file)
    gdf_predict = gpd.read_file(predict_file).to_crs(3857)
    
    # Validate the CRS
    assert gdf_predict.crs==3857, (
        f'All geometries must be in EPSG:3857 Coordinate Reference System.')
    assert gdf_groundtruth.crs==3857, (
        f'All geometries must be in EPSG:3857 Coordinate Reference System.')
    
    # Validate the geometry column
    assert "geometry" in gdf_predict.columns, (
        f'Missing geometry column.')
    assert "geometry" in gdf_groundtruth.columns, (
        f'Missing geometry column.')
    
    iou = calc_iou(gdf_groundtruth, gdf_predict)
    # Punish if more polygon provided 
    if len(gdf_groundtruth)<len(gdf_predict):
        iou = iou * (len(gdf_groundtruth)/len(gdf_predict))
    
    return iou
    
def evaluate(groundtruth_files, predict_files):
    """Calculates metrics for multiple files.

    Args:
      groundtruth_files: List of groundtruth files.
      predict_files: List of prediction files. One file for each groundtruth.

    Returns:
      Intersection Over Union (IOU) Score.
    """
    
    # Check the number of files provided
    assert len(groundtruth_files) == len(predict_files), (
        f'Number of files are not matching.')
    
    results = []
    
    for i in tqdm(range(len(groundtruth_files))):
      try:
        iou = calc_metrics(groundtruth_files[i], predict_files[i])
        print(predict_files[i],iou)
        if iou:
          results.append(iou)
      except:
        continue
    
    print(np.min(results),np.max(results),np.mean(results))
    return np.mean(results)
    