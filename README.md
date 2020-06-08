# mcvoronoi 
Computing [voronoi](https://en.wikipedia.org/wiki/Voronoi_diagram) areas using monte carlo simulation


### Prerequisites (required modules)

- python_requires='>=3.6'
```sh
$ python3 --version 
```
If not installed, visit official site for python [here](https://www.python.org/downloads/) and download the latest version of Python.

- numpy
```sh
$ pip3 install numpy
```
- sklearn
```sh
$ pip3 install sklearn
```
- matplotlib
```sh
$ pip3 install matplotlib
```

### Installation

```sh
$ pip3 install mcvoronoi
```
- in main.py file *example code to use the module*:
```sh
import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import mcvoronoi
from sklearn.neighbors import KDTree

node_lat_lon = {}
node_dict = {}
points = []
node_id = []
with open('example_latlon.csv') as f:
    for row in f:
        listed = row.strip().split(',')
        if np.random.rand() < 0.1:
            if int(listed[0]) not in node_dict:
                points.append([float(listed[1]), float(listed[2])])
                node_id.append(int(listed[0]))

points = np.array(points) # np.random.uniform(size=[50, 2])
lat_lon_area, mean_percentage_error = voronoi_area(points) 
```

### Input

| 	  Input Type	| 						Input					| 	Default_Value	|
| ------------------| ----------------------------------------------|-------------------|
| numpy array		| input_coordinates: x, y 		|	No default value|
| integer 			| number_of_iterations 							|	50				|
| integer			| number_of_trials_per_iteration 				|	10000			|
| boolean			| error_plot_enabled 							|	True			|
| boolean			| voronoi_plot_enabled 							|	False			|
| float				| sizeOfMarker 									|	0.5				|
| integer			| NUM_COLORS									|	20				|


### Output

|	  Output Type	| 						Output														|
| ------------------| ----------------------------------------------------------------------------------|
| python dict		| key = (x,y), value = %age of area of the smallest rectangle enclosing all input_coordinates, len(lat_lon_area) is same as number of input_coordinates  			|
| plot  			| line graph of %age error vs trial number_of_iterations							|
| plot				| voronoi Diagram with pts & random pts closest to points marked in NUM_COLORS		|
| float				| mean % error_plot_enabled									 						|


### Credits

|	  Author	    | 		Contribution                                    														|        Email					|
| ------------------| --------------------------------------------------------------------------------------------------------------|-------------------------------|
| Kusum Kumari      | code standardization; code extension to include useful functionalities; creation and maintenance of mcvoronoi python library | kusum.kumarisjce@gmail.com    |
| Nishant Kumar 	| initial working solution using [MC](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation for voronoi areas | abc.nishant007@gmail.com     			|


### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to add/change.


### License

[MIT](https://choosealicense.com/licenses/mit/)

