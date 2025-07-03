from samgeo import tms_to_geotiff
from samgeo.text_sam import LangSAM

image = 'HALM1_75_20240418T153559_20240418T153632_T19TDK_VIS.tif'

sam = LangSAM()

text_prompt = "segment river in aerial view"

for i in range(3):
    title = "river_" + str(i)
    tif_title = title + ".tif"
    shp_title = title + "shp"
    sam.predict(images[i], text_prompt, box_threshold=0.36, text_threshold=0.36, automatic=False)

    sam.show_anns(
        cmap="Greens",
        add_boxes=False,
        title="Segmentation of water",
        blend=True,
        output= tif_title
    )

    sam.raster_to_vector(tif_title, shp_title)
