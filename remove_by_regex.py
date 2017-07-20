def remove_by_regex(df,colname,pattern_string,removed_ind=False):
	"""
	Given a pd.DataFrame, return rows such that the colname does NOT
	satisfy the given regex expression.

	If removed_ind is True, then will return the index of the rows that
	were removed from the original dataframe.
	"""

	ind_filter = df[colname].str.contains(pattern_string, na=False)
	ind_removed = [i for i,x in enumerate(ind_filter) if x == True]

	if removed_ind == False:
		return df.loc[-ind_filter]
	else:
		return df.loc[-ind_filter], ind_removed
