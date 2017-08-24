def bf_optimizer(f, X, target, indp_vars, indp_vars_ranges):
    """
    X should be a pandas.DataFrame of shape (1,-1)
    When X is a n*p data frame, pass the i-th row as X.iloc[[i]]
    """

    search_space_size = np.product([len(i) for i in indp_vars_ranges])
    print("search space size: " + str(search_space_size))

    indp_vars_inds = [list(X.columns.values).index(ind_var) for ind_var in indp_vars]
    X_matrix = X.values

    # set up the matrix
    scenarios = np.tile(X_matrix,(search_space_size,1))

    # fill in all the combinations. room for improvement
    for i, comb in enumerate(itertools.product(*indp_vars_ranges)):
        scenarios[i,indp_vars_inds] = comb
    
    # find optimal value. without reshape will raise MemoryError
    y_hats = model.predict(scenarios).reshape(-1,1)

    if target == "min":
        optimal_comb_ind = y_hats.argmin()
        optimal_comb = scenarios[optimal_comb_ind,indp_vars_inds]
        optimal_y = model.predict(scenarios[optimal_comb_ind].reshape(1,-1))[0]

        return optimal_comb, optimal_y

    elif target == "max":
        optimal_comb_ind = y_hats.argmax()
        optimal_comb = scenarios[optimal_comb_ind,indp_vars_inds]
        optimal_y = model.predict(scenarios[optimal_comb_ind].reshape(1,-1))[0]

        return optimal_comb, optimal_y

    else:
        optimal_comb_ind = abs(y_hats - np.full((search_space_size,1),target)).argmin()
        optimal_comb = scenarios[optimal_comb_ind,indp_vars_inds]
        optimal_y = model.predict(scenarios[optimal_comb_ind].reshape(1,-1))[0]

        return optimal_comb, optimal_y


# optimal_comb, optimal_y = bf_optimizer(f=model, X=X, target="max", indp_vars=['air_pressure','oxygen_concentration',''], indp_vars_ranges=[
#     np.arange(0,0.9,0.01), np.arange(0,26,0.1), np.arange(0,37,0.1)])
