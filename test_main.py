import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_uniform_discrete(self):
        for a in range(1,4) :
            for b in range(6,8) : 
                mean = 0
                for i in range(10) : 
                    var = uniform_discrete(a,b)
                    self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your uniform_discrete function returns a number that is not an integer" )
                    self.assertTrue( var>=a and var<=b, "your uniform_discrete function returns a number that falls outside of the range of allowed values")
                    mean = mean + var
                mean = mean / 10
                var = ( (b-a+1)*(b-a+1) - 1 ) / 12 
                bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                self.assertTrue( np.fabs( mean - 0.5*(b+a) )<bar, "your uniform_discrete function appears to be sampling the wrong distribution" )
    
    def test_n_uniform_discrete(self) : 
        for n in range(2,4) : 
            for a in range(1,3) :
                for b in range(6,7) : 
                    mean = 0
                    for i in range(10) : 
                        var = n_uniform_discrete(n,a,b)
                        self.assertTrue( np.fabs( np.floor(var) - var)<1e-7, "your n_uniform_discrete function returns a number that is not an integer" )
                        self.assertTrue( var>=n*a and var<=n*b, "your n_uniform_discrete function returns a number that falls outside of the range of allowed values" )
                        mean = mean + var
                    mean = mean / 10
                    var = n/12*( (b-a+1)*(b-a+1) - 1 )
                    bar = np.sqrt(var/10)*st.norm.ppf( (0.99 + 1) / 2 )
                    self.assertTrue( np.fabs( mean - n*0.5*(b+a) )<bar , "your n_uniform_discrete function appears to be sampling the wrong distribution" )
      
      def test_percentiles(self) : 
          psamples = np.zeros([4,100])
          for j in range(100) : 
              samples = np.zeros(100) 
              for i in range(100) : samples[i] = n_uniform_discrete(2,1,6)
              k=0
              for m in [20,40,60,80] : 
                  psamples[k,j] = np.percentile( samples, m )
                  k = k + 1 

          k=0
          for m in [20,40,60,80] : 
              ppp = percentile(m,100,2,1,6)
              self.assertTrue( np.percentile(psamples[k,:], 1)<=ppp and ppp<=np.percentile(psamples[k,:], 99), "your percentiles functions appears to be sampling the wrong distribution" )
              k=k+1
    
    
