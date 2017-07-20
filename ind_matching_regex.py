def ind_matching_regex(df,colname,pattern):

	ind_filter = df[colname].str.contains(pattern, na=False)
	ind_matching = [i for i,x in enumerate(ind_filter) if x == True]
	return ind_matching
