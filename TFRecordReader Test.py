# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 13:57:35 2018

@author: Roland
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Define a reader and read the next record
reader = tf.TFRecordReader()

filename = 'train.tfrecords'  # address to save the file

filename_queue = tf.train.string_input_producer(filename)

_, serialized_example = reader.read(filename_queue)

feature = {'train/label': tf.FixedLenFeature([], tf.int64),
           'train/image': tf.FixedLenFeature([], tf.int64)}


# Decode the record read by the reader
features = tf.parse_single_example(serialized_example, features=feature)
print (features)

# parse features
data = features['image']   
label = features['label']

# Reshape image data into the original shape
#print(data.shape)
#data=tf.reshape(data, [3, 19, 19])
# Any preprocessing here ...
    
    
with tf.Session() as sess: 
    print (sess.run([data,label]))
    
    
    
    
    
   