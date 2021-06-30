# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)
def calculate(list):

  if len(list) !=9:
    return "List must contain nine numbers."
  else:
    m1=np.array(list).reshape(3,3)
    calculations={
    'mean ': (np.mean(m1, axis=0).tolist(), np.mean(m1, axis=1).tolist(), np.mean(list)),
    'variance ': (np.var(m1, axis=0).tolist(), np.var(m1, axis=1).tolist(), np.var(list)),
    'standard deviation ': (np.std(m1, axis=0).tolist(), np.std(m1, axis=1).tolist(), np.std(list)),
    'max ': (np.max(m1, axis=0).tolist(), np.max(m1, axis=1).tolist(), np.max(list)),
    'min ': (np.min(m1, axis=0).tolist(), np.min(m1, axis=1).tolist(), np.min(list)),
    'sum ': (np.sum(m1, axis=0).tolist(), np.sum(m1, axis=1).tolist(), np.sum(list))
        }
  return calculations
