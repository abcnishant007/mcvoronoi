import numpy as np

# this is just a quickfix so that we can run without the pip install
try:
    from mcvoronoi import voronoi_area  # if pip installed
except:
    from source import voronoi_area               # if not pip installed, and using the git version


points = np.random.rand(10, 2)  # a numpy array of 10 input co-ordinates
lat_lon_area, mean_percentage_error = voronoi_area(points,voronoi_plot_enabled=True, NUM_COLORS=5, metric='manhattan')
