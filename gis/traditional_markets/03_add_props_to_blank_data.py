import geopandas as gpd
import os


def merge_csv_into_gdf():
    gdf = None
    for (dir,_,file) in os.walk("./data/"):
        print(file)
        for f in file:
            if gdf is None:
                gdf = gpd.read_file(dir+f,crs="epsg:4326")
            else:
                gdf.concat(gpd.read_file(dir+f,crs="epsg:4326"))
    return gdf
        



if __name__ == "__main__":
    merge_csv_into_gdf()
