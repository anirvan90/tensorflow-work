import numpy as np

scores = np.array([3.0, 1.0, 0.2])


def softmax(x):
    """
   Compute the softmax values for x
  """
    return np.exp(x) / np.sum(np.exp(x), axis=0)


print(softmax(scores))
print('\n')
print(softmax(scores / 10))

bill = 1e+9
for i in range(1000000):
    bill = bill + 1e-6
print(bill - 1e+9)
