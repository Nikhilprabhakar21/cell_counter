# Cell Counter
 Scripts for finding color thresholds and counting cells for biological applications. Video demo: https://www.loom.com/share/cf338891272f4e9386f1e04e51b2808c


### Instalation:
1. clone this repository
2. create virtual enviornment
3. pip instal matplotlib and opencv-python

### Running the program:
The histogram file must be run on the command line prompt with the following command.
The first parameter is the image file, the second is the lower bound for the threshold
and, the third is the upperbound for the threshold. 
```commandline
 python3 histogram.py "cell_images/image(1).png" 100 200
```

The cell_counter file is also run on  the command line prompt with the following command.
The first parameter is the lower bound for the threshold
and the second is the upperbound for the threshold. 
```commandline
python3 cell_counter.py 100 200
```

