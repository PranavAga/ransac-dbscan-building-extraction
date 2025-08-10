import eval

groundtruth_files = [
    # 'data/USGS_LPC_IL_8County_2020_A20_1035_8430_gt_buildings.geojson',
    'data/USGS_LPC_AL_AGIO_B1_2016_16S_EB_2340_LAS_2018_gt_buildings.geojson',
    'data/USGS_LPC_CT_Statewide_C16_250890_se_gt_buildings.geojson',
    'data/USGS_LPC_GA_SW_Georgia_22_County_Lidar_2017_B17_GAW_20750320_gt_buildings.geojson',
    'data/USGS_LPC_IA_NorthCentral_2020_D20_w4350n4631_gt_buildings.geojson',
    'data/USGS_LPC_IL_8County_2020_A20_1035_8430_gt_buildings.geojson',
    'data/USGS_LPC_IL_GrnMacMont_2017_2403_1011_LAS_2018_gt_buildings.geojson',
    'data/USGS_LPC_IL_HicksDome_FluorsparDistrict_2019_D19_2339_5650_gt_buildings.geojson',
    'data/USGS_LPC_KY_Eastern_2019_A19_e1174n1677_gt_buildings.geojson',
    # 'data/USGS_LPC_MI_FEMA_2019_C19_845492_gt_buildings.geojson'
    # 'eval/groundtruth_area1.geojson'
]

predict_files = [
    # 'output2.geojson',
    'USGS_LPC_AL_AGIO_B1_2016_16S_EB_2340_LAS_2018_pred.geojson',
    'USGS_LPC_CT_Statewide_C16_250890_se_pred.geojson',
    'USGS_LPC_GA_SW_Georgia_22_County_Lidar_2017_B17_GAW_20750320_pred.geojson',
    'USGS_LPC_IA_NorthCentral_2020_D20_w4350n4631_pred.geojson',
    'USGS_LPC_IL_8County_2020_A20_1035_8430_pred.geojson',
    'USGS_LPC_IL_GrnMacMont_2017_2403_1011_LAS_2018_pred.geojson',
    'USGS_LPC_IL_HicksDome_FluorsparDistrict_2019_D19_2339_5650_pred.geojson',
    'USGS_LPC_KY_Eastern_2019_A19_e1174n1677_pred.geojson',
    # 'USGS_LPC_MI_FEMA_2019_C19_845492_pred.geojson'
    # 'eval/prediction_area1.geojson',
]
# 4. 0.008669204184713104
# 6. 0.016138091981347573
print(eval.evaluate(groundtruth_files, predict_files))