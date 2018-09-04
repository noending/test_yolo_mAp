from voc_eval_py3 import voc_eval
print('car:') 
print(voc_eval('/home/magic/Desktop/CNN models/darknet/results/{}.txt', '/home/magic/Desktop/CNN models/darknet/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/magic/Desktop/CNN models/darknet/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'car', '.'))
print('\n###############################################################################')
print('person:')
print(voc_eval('/home/magic/Desktop/CNN models/darknet/results/{}.txt', '/home/magic/Desktop/CNN models/darknet/VOCdevkit/VOC2007/Annotations/{}.xml', '/home/magic/Desktop/CNN models/darknet/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'person', '.'))