from samgeo import tms_to_geotiff
from samgeo.text_sam import LangSAM

image = 'HALM1_75_20240418T153559_20240418T153632_T19TDK_VIS.tif'

sam = LangSAM()

text_prompt = "rivers and lakes"

sam.predict(image, text_prompt, box_threshold=0.24, text_threshold=0.24)

sam.show_anns(
    cmap="Greys_r",
    add_boxes=False,
    title="Automatic Segmentation of Rivers",
    blend=False,
    automatic=False,
    output='water.tif'
)

sam.raster_to_vector("water.tif", "water.shp")
