# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:19:56 2018

@author: Roland
"""

import glob
import numpy as np
import tensorflow as tf
import sys

train_filename = 'train.tfrecords'
# open the TFRecords file
writer = tf.python_io.TFRecordWriter(train_filename)

def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
def _bytes_feature(value):
    
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))
        
for i in glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train1/0*"):
    if 'out' in i:
        out=np.load(i)
        inn=np.load(i[:-7]+'.npy')
        print (out.shape)
        print(inn.shape)
        inn=np.reshape(inn,[len(inn)*len(inn[0])*len(inn[0][0]),])
        
        for j in range (0,len(out)):
            
            feature = {'train/label': _int64_feature(out[j]),
                       'train/image': _int64_feature(inn[j])}

    # Create an example protocol buffer
            example = tf.train.Example(features=tf.train.Features(feature=feature))
        
    # Serialize to string and write on the file
        writer.write(example.SerializeToString())
        
writer.close()

