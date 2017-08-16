def brute_force_solver(model,current_state,x_ind,search_space,target):
    """
    Args:
        model:          an instance with `predict` method
        current_state:  np.ndarray
        x_ind:          int
        search_space:   np.ndarray
        target:         float
    """
    
    scenarios = np.tile(current_state,(len(search_space),1))
    scenarios[:,x_ind] = search_space

    y_hats = model.predict(scenarios)
    optimal_x_ind = abs(y_hats - np.full((len(search_space),1),target)).argmin()
    optimal_x = scenarios[optimal_x_ind,x_ind]

    return optimal_x
