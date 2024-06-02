import scipy.io as sio
from pprint import pprint
import numpy as np

if __name__ == '__main__':
    array = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.ones((5, 5))
    dictinory = {"array1": array, "array2": array2}
    # save mat lab file
    # sio.savemat("example",dictinory)

    # read mat lab file.
    print(sio.loadmat("example"))


