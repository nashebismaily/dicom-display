import os
import pydicom
import matplotlib.pyplot as plt
from pydicom.data import get_testdata_file

directory = "dicoms"

entries = os.listdir(directory)
for entry in entries:
  print(entry)
  ds = pydicom.dcmread(os.path.join(directory, entry))
  plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
  plt.show()
