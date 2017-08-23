def bf_optimizer(f, X, target, ind_vars, ind_vars_ranges):
    """
    X should be a pandas.DataFrame of shape (1,-1)
    """

    search_space_size = np.product([len(i) for i in ind_vars_ranges])
    print("search space size: " + str(search_space_size))

    ind_vars_inds = [list(X.columns.values).index(ind_var) for ind_var in ind_vars]
    current_state = X.values

    # set up the matrix
    scenarios = np.tile(current_state,(search_space_size,1))

    # fill in all the combinations. room for improvement
    for i, comb in enumerate(itertools.product(*ind_vars_ranges)):
        scenarios[i,ind_vars_inds] = comb
    
    # find optimal value
    y_hats = model.predict(scenarios)
    optimal_x_ind = abs(y_hats - np.full((search_space_size,1),target)).argmin()
    optimal_x = scenarios[optimal_x_ind,ind_vars_inds]
    optimal_y = model.predict(scenarios[optimal_x_ind].reshape(1,-1))[0]

    return optimal_x, optimal_y
