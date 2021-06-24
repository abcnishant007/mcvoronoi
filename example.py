import numpy as np
import mcvoronoi 


points = np.random.rand(10, 2)  # a numpy array of 10 input co-ordinates
lat_lon_area, mean_percentage_error = mcvoronoi.voronoi_area(points,voronoi_plot_enabled=True, NUM_COLORS=5, metric='manhattan')
