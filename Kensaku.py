import numpy as np
import pandas as pd

from sklearn import neighbors
from sklearn import preprocessing

class Kensaku:
    """
    This class performs k-nearest neighbor search with user-defined distance metric.
    """

    def __init__(self,query,history,colnames=None,normalize=True):
        """
        Args:
            query:      pd.core.frame.DataFrame / np.ndarray
            history:    pd.core.frame.DataFrame / np.ndarray
            colnames:   list
            normalize:  bool
        """

        if type(query) != type(history):
            raise TypeError("Type of query and history are different!")

        if query.shape[1] != history.shape[1]:
        	raise ValueError("Query vector and history array have different number of features!")

        if not(colnames is None) and len(colnames) != query.shape[1]:
        	raise ValueError("Query vector has " + str(query.shape[1]) + " features, but " + str(len(colnames)) + " names were provided!")

        self.query = query
        self.history = history
        self.input_type = type(history)

        if self.input_type == pd.core.frame.DataFrame:
            self.colnames = list(self.history.columns.values)
            self.query_array = query.values
            self.history_array = history.values
        elif self.input_type == np.ndarray:
            self.colnames = colnames
            self.query_array = query
            self.history_array = history
        else:
            self.colnames = []
            self.query_array = query
            self.history_array = history

        self.normalize = normalize

        if self.normalize == True:
            self.combined = np.vstack([self.history_array, self.query_array])
            self.normalized_combined = preprocessing.normalize(self.combined)
            self.normalized_history = self.normalized_combined[0:-1,:]
            self.normalized_current = self.normalized_combined[-1,:].reshape(1,-1)


    def fit_history(self,udf_metric,n_cases):
        """
        Args:
            udf_metric: user-defined metric object
            n_cases:    int
        """

        self.neigh = neighbors.NearestNeighbors(n_neighbors=n_cases, metric=udf_metric)
        self.neigh.fit(self.normalized_history)
        self.indices = self.neigh.kneighbors(self.normalized_current,return_distance=False)[0]

    def get_indices(self):
        return self.indices

    def get_records(self,var=None):
        """
        Args:
            vars:   list of str. name of features

        Returns:
            .           pd.core.frame.DataFrame
        """

        if len(self.colnames) == 0:
            raise ValueError("No column names provided during initialization!")

        if var is None:
            var = self.colnames

        y_pos = [self.colnames.index(i) for i in var]
        record = self.history_array[np.ix_(self.indices,y_pos)]
        record = pd.DataFrame(record,columns=var,index=self.indices)
        return record
