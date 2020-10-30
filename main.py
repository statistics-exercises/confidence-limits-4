import numpy as np

def uniform_discrete(a,b) :
  # Your code to generate the uniform discrete random variable goes here
  
  
def n_uniform_discrete( n, a, b ) : 
  # You code to generate the sum of n uniform discrete random variables goes here
  
  
def percentile( p, m, n, a, b ) : 
  # Your code to generate the pth percentile of a sample of size m of sums of
  # n uniform discrete random variables goes here.


# This outputs what you would get when you roll two fair dice four times.
print( percentile(10,100,2,1,6), percentile(10,100,2,1,6), percentile(10,100,2,1,6), percentile(10,100,2,1,6) )
