def cross_section(vec, model, *, x_pos, x_range):
    scenarios = np.tile(vec,(len(x_range),1))
    scenarios[:,x_pos] = x_range

    y_hats = model.predict(scenarios)
    plt.plot(x_range,y_hats)
    plt.show()
    return x_range,y_hats

def cross_section_analysis(data, *, y, x, model, i):
    temp_data = data.drop([y], axis=1, inplace=False)
    x_pos = list(temp_data.columns.values).index(x)
    
    cross_section(vec=temp_data.loc[i,:].values.reshape(1,-1)[0], model=model, x_pos=x_pos, x_range=np.arange(
        data[x].min(), data[x].max(), 0.01))
    
    return data.iloc[i, x_pos], data.loc[i,[y]].values[0], model.predict(temp_data.loc[i,:].values.reshape(1,-1))[0]
