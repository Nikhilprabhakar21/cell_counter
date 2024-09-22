import sys
import cv2
from matplotlib import pyplot as plt

file_name = sys.argv[1]
print("File name:", file_name)

lower_thresh = 100
upper_thresh = 200
if len(sys.argv) == 4:
    lower_thresh = int(sys.argv[2])
    upper_thresh = int(sys.argv[3])

grey = cv2.imread(file_name, 0)
hist = cv2.calcHist([grey], [0], None, [256], [0, 256])
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(grey, cv2.COLOR_GRAY2RGB))

# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.axvline(x=lower_thresh, color="r")
plt.axvline(x=upper_thresh, color="r")
plt.xlim([0, 256])
plt.show()