import math

def unbiasedVariance(obs):
	'''
	compute unbiased estimator of population variance
	obs: list of numbers
	'''
	num_of_obs = len(obs)
	average = sum(obs)/num_of_obs
	return sum([(i-average)**2 for i in obs])/(num_of_obs-1)


def pooledVariance(obs):
	'''
	computes pooled variance. returns S_p^2,the one WITHOUT the square root
  	obs: list of list of numbers
	'''
	num_of_groups = len(obs)
	num_of_obs = sum([len(i) for i in obs])
	return sum([unbiasedVariance(group)*(len(group)-1) for group in obs])/(num_of_obs-num_of_groups)

obs = [[2.5,5.5,8.5,3.5],[3,5,6,4],[5,7,4,8],[7,6,8,10],[10,12,7,8]]
print(pooledVariance(obs))
print(math.sqrt(pooledVariance(obs)))
