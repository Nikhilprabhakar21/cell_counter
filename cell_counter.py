import sys
import cv2
import csv

lower_thresh = 100
upper_thresh = 200
if len(sys.argv) == 3:
    lower_thresh = int(sys.argv[1])
    upper_thresh = int(sys.argv[2])


file_name_to_count = {}

for i in range(1,101):
    file_name = f"image({i}).png"
    gray = cv2.imread(f"cell_images/{file_name}", 0)

    threshed = cv2.inRange(gray, 120, 256)

    ## findcontours
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
    color = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    ## filter by area
    s1= 50
    s2 = 700
    xcnts = []
    i = 0
    for cnt in cnts:
        if s1<cv2.contourArea(cnt)<s2:
            xcnts.append(cnt)
            cv2.putText(color, str(i), (int(cnt[0][0][0]), int(cnt[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            i = i + 1

    print(f"Platelet number for {file_name}: {len(xcnts)}")

    file_name_to_count[file_name] = len(xcnts)

with open("all_cell_counts.csv", "w") as f:
    w = csv.writer(f)
    w.writerows(file_name_to_count.items())