def voronoi_area(input_coordinates, number_of_iterations=50, number_of_trials_per_iteration=10000, error_plot_enabled=True, voronoi_plot_enabled=False, sizeOfMarker=0.5, NUM_COLORS=20):
  
    import matplotlib as mpl
    import matplotlib.cm as cm
    import matplotlib.pyplot as plt
    from sklearn.neighbors import KDTree
    import numpy as np
    import csv

    
    if type(input_coordinates) is np.ndarray:
        points = input_coordinates
        n_trials = number_of_trials_per_iteration
        if n_trials < input_coordinates.shape[0]:
            print ('Number of points per trial is less than the number of area centres/input points\nreverting to the number of areas')
            n_trials = input_coordinates.shape[0]

        
        np.random.seed(0)
        points = points
        tree = KDTree(points)
        percent_increase_x = 0
        percent_increase_y = 0



        minX = np.min(points[:,0]) - percent_increase_x * np.min(points[:,0])
        minY= np.min(points[:,1]) - percent_increase_y * np.min(points[:,1])
        maxX = np.max(points[:,0]) + percent_increase_x * np.max(points[:,0])
        maxY= np.max(points[:,1]) + percent_increase_x * np.max(points[:,1])

        areas = {}
        areas_at_trial_number = {}
        mean_areas_until_now = {}
        for j in range(number_of_iterations):
            areas_at_trial_number[j] = {}
            mean_areas_until_now[j] = {}

        error_record = []
        nearest_ind_history = []
        query_points_history = []
        unique_history = []
        for j in range(number_of_iterations):
            x = np.random.uniform(low=minX, high=maxX, size=(n_trials,))
            y = np.random.uniform(low=minY, high=maxY, size=(n_trials,))
            query_points = np.random.rand(n_trials,2)
            query_points[:,0] = x
            query_points[:,1] = y

            nearest_dist, nearest_ind = tree.query(query_points, k=1)
            if voronoi_plot_enabled:
                nearest_ind_history.append(nearest_ind)
                query_points_history.append(query_points)

            unique, counts = np.unique(nearest_ind, return_counts=True)

            for i in range(unique.shape[0]):
                areas_at_trial_number[j][unique[i]] = counts[i]
            


            if j>0 :
                alpha = 1/(j+1)
                for i in range(unique.shape[0]):
                    if unique[i] in areas_at_trial_number[j-1]: 
                        areas_at_trial_number[j][unique[i]] = alpha *  areas_at_trial_number[j][unique[i]] + (1-alpha)* areas_at_trial_number[j-1][unique[i]]
                    else:
                        ## the case when there was not point in some particular area in the previous iteration
                        ## in this case, we retain the current value as the mean until now
                        areas_at_trial_number[j][unique[i]] = areas_at_trial_number[j][unique[i]] 

                errors = [] 
                for key in areas_at_trial_number[j-1]:
                    if key in areas_at_trial_number[j]:
                        errors.append((areas_at_trial_number[j][key] - areas_at_trial_number[j-1][key])/areas_at_trial_number[j-1][key] * 100 )
                
                error_record.append(np.mean(errors))
            
            
        if error_plot_enabled:
            plt.plot(range(1,len(error_record)+1), error_record)
            plt.xlabel('Trial number', fontsize=14)
            plt.ylabel('% error', fontsize=14)
            plt.grid()
            plt.tight_layout()
            plt.savefig('voronoi_errors.png',dpi=200)
            plt.show()

        if voronoi_plot_enabled:
            cm = plt.get_cmap('gist_rainbow')
            colormap = [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]
            cmap = {}

            unique_ind = [] 
            for j in range(number_of_iterations):
                unique_ind = unique_ind + list(set(list(nearest_ind_history[j][:,0])))
            unique_ind = list(set(unique_ind))
            for key in unique_ind:
                cmap[key] = colormap[int(np.random.rand() * NUM_COLORS)]


            x_list = []
            y_list = []
            c_list = [] 
            for j in range(number_of_iterations):
                for i in range(query_points_history[j].shape[0]):
                    x_list.append(query_points_history[j][i,0])
                    y_list.append(query_points_history[j][i,1])
                    c_list.append(cmap[nearest_ind_history[j][i,0]])
            plt.scatter(x_list, y_list, color = c_list, s=sizeOfMarker)
            
            x_list = []
            y_list = []
            for j in range(input_coordinates.shape[0]):
                x_list.append(input_coordinates[j][0])
                y_list.append(input_coordinates[j][1])
            plt.scatter(x_list, y_list, marker='o',color='black', s=sizeOfMarker)                

            plt.tight_layout()
            plt.savefig('voronoi_colorful.png',dpi=200)
            plt.show()

        lat_lon_area = {}
        s = sum(areas_at_trial_number[number_of_iterations-1].values())
        for key in areas_at_trial_number[number_of_iterations-1]:
            lat_lon_area[(input_coordinates[key][0], input_coordinates[key][1])] = areas_at_trial_number[number_of_iterations-1][key]*100/s
        return lat_lon_area, error_record[-1]
