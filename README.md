# (revision) Percentiles for dice rolls

In the previous exercise, you generated multiple identical random variables and then computed a __statistic__ - the mean.  If we have multiple random variables, however, the mean is not the only statistic we can compute.  A __statistic__ is any function of the set of random variables that have been generated.  One other statistic we have learned to compute, for instance, is percentiles.  In this exercise, I would thus like you to do something akin to what you just did.  __Instead of writing a function to calculate the mean from the m uniform discrete random variables that are greater than or equal to a and less than or equal to b that you generate I want you to write a function to calculate the pth percentile of this set of m random variables.__

To complete this task you will need to write three functions:

1. `uniform_discrete` - takes two arguments `a` and `b` in input.  It should return a uniform discrete random variable that is greater than or equal to `a` and less than or equal to `b`.
2. `n_uniform_discrete` - takes three arguments `n`, `a` and `b`.  It should return the sum of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  Notice that you can call `uniform_discrete` in this function.
3. `percentile` - takes five arguments in input `p`, `m`, `n`, `a` and `b`.  It should generate `m` sums of `n` uniform discrete random variables that are greater than or equal to `a` and less than or equal to `b`.  You will need to store these `m` random variables in an array so that you can then calculate the pth percentile of the distribution of values.  Please note that you may want to include calls to `n_uniform_discrete` in this function.

Once you have completed these three functions and run the code four values for the 10th percentile value obtained when you roll 2 dice 100 times are output in the black square.  Notice that these values are all different because the statistic we are sampling is still a random variable. 
