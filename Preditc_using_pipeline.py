import pickle
import numpy as np
from numpy.conftest import dtype

pipe = pickle.load(open('pipe.pkl','rb'))

#Assume user input
test_data = np.array([2,'male',31.0,0,0,10.5,'S'],dtype = object).reshape(1,7)

print(pipe.predict(test_data))