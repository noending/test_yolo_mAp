#!/bin/bash
./darknet detector valid cfg/voc.data cfg/yolov3-tiny-voc.cfg backup/yolov3-tiny-voc_480000.weights
rm annots.pkl
python compute-map.py
