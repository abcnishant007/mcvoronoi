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
import mcvoronoi 


points = np.random.rand(10, 2)  # a numpy array of 10 input co-ordinates
lat_lon_area, mean_percentage_error = mcvoronoi.voronoi_area(points, voronoi_plot_enabled=True, NUM_COLORS=5)
```

### Parameters to the function 

| 	  Input Type	| 						Input					| 	Default_Value	|
| ------------------| ----------------------------------------------|-------------------|
| numpy array		| input_coordinates		|	No default value|
| integer 			| number_of_iterations 							|	50				|
| integer			| number_of_trials_per_iteration 				|	10000			|
| boolean			| error_plot_enabled 							|	True			|
| boolean			| voronoi_plot_enabled 							|	False			|
| float				| sizeOfMarker 									|	0.5				|
| integer			| NUM_COLORS									|	20				|


### Returned values

|	  Return Type	| 						Output														|
| ------------------| ----------------------------------------------------------------------------------|
| python dict		| key = (x,y), value = % of area of the smallest rectangle enclosing all input_coordinates, len(lat_lon_area) is same as number of input_coordinates  			|
| plot  			| line graph of % error vs trial number (saved as .png)							|
| plot				| voronoi Diagram with pts & random pts closest to points marked in NUM_COLORS(saved as .png)		|
| float				| mean % error at the last trial									 						|


### Credits

|	  Author	    | 		Contribution                                    														|        Email					|
| ------------------| --------------------------------------------------------------------------------------------------------------|-------------------------------|
| Kusum Kumari      | code standardization; code extension to include useful functionalities; creation and maintenance of mcvoronoi python library | kusum.kumarisjce@gmail.com    |
| Nishant Kumar 	| initial working solution using [MC](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation for voronoi areas | abc.nishant007@gmail.com     			|


### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to add/change.


### License

[MIT](https://choosealicense.com/licenses/mit/)


### Output plots
![mean_errors_plot](https://user-images.githubusercontent.com/9101260/84084935-0e5a7380-aa17-11ea-9519-7887a4a35cc0.png)
![vornoi_colored_areas](https://user-images.githubusercontent.com/9101260/84084884-ed921e00-aa16-11ea-97b6-edfb4c98c397.png)
