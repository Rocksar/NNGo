# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:27:38 2018

@author: Roland
"""

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import glob

# Helper libraries
import math
import numpy as np
import matplotlib.pyplot as plt

# The parser Function

def parser(file_to_parse,number_of_matrix,type_of_data):
    file = open(file_to_parse,'r')
    ligne=0
    matrix=0
    data=0
    for line in file:
        words=line.split(",")
        column=0
        ligne=0
        for i in words:
                type_of_data[data][matrix][ligne][column]=int(i)
                column+=1
                if column>=number_of_column:
                    column=0
                    ligne+=1
        if matrix<number_of_matrix-1 :
            matrix+=1
                
        else :
            matrix=0
            data+=1
            print(data)
            if data==number_of_data:
                file.close()
                return 0
    
    
def parse_output(file_to_parse,type_of_data):
    file = open(file_to_parse,'r')
    data=0
    for line in file:
        words=list(map(int, line.split(",")))
        type_of_data[data]=np.argmax(words)
        data+=1
        if data==number_of_data:
            return 0
               
        
        
           
    
# Data Information    
number_of_data=700000
number_of_matrix=3
number_of_test=50000
number_of_line=19
number_of_column=19   

#train_test=np.zeros(shape=(number_of_data,1,number_of_line,number_of_column), order='F')

#test_input=np.zeros(shape=(number_of_test,number_of_matrix,number_of_line,number_of_column), order='F')
#test_output=np.zeros(shape=(number_of_test), dtype=int, order='F')
 
#Load data from npy 

#def loadnpy(adress):
#    train_input=np.empty((0,3,361))
#    train_output=np.array([])
#    tmp=0
#    for i in adress:
#        if 'out' in i:
#            a=np.load(i)
#            train_output=np.concatenate((train_output,a),axis=0)
#            b=np.load(i[:-7]+'.npy')
#            train_input=np.concatenate((train_input,b),axis=0)
#        tmp+=1
#        if tmp%100==1:
#            print(tmp)
#    print (train_input.shape)
#    print (train_output.shape)
#    train_input=train_input.reshape((len(train_input),3,19,19))
#    return (train_input, train_output)

def loadnpy(adress):
    train_input=[]
    train_output=[]
    tmp=0
    for i in adress:
        if 'out' in i:
            a=list(np.load(i))
#            print(a)
            train_output.extend(a)
#            print(len(train_output))
            b=list(np.load(i[:-7]+'.npy'))
            train_input.extend(b)
        tmp+=1
        if tmp%100==1:
            print(tmp)
    train_input=np.array(train_input)
    train_output=np.array(train_output)
    print (train_input.shape)
    print (train_output.shape)
    train_input=train_input.reshape((len(train_input),3,19,19))
    return (train_input, train_output)
# Structure of the neural network

nombre_de_kernel=64

model = tf.keras.models.Sequential([
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first',input_shape=(3,19,19)),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(nombre_de_kernel,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9),
  tf.keras.layers.Activation(tf.nn.relu),
  tf.keras.layers.Convolution2D(1,(3, 3),padding='same',data_format='channels_first'),
  tf.keras.layers.BatchNormalization(axis=1,momentum=0.9,scale=True),
  tf.keras.layers.Flatten(data_format='channels_first'),
  tf.keras.layers.Activation(tf.nn.softmax)
  
])
    
model=keras.models.load_model("C:/PythonWorkSpace/Neural_Network_Go/NN07092018/49_50game_model_07092018.h5")    
    
    

checkpoint_path = "C:/PythonWorkSpace/Neural_Network_Go/training_1/cp.ckpt"


# Create checkpoint callback
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
                                                 save_weights_only=True,
                                                 verbose=1,
                                                 period=30)





#parser("C:/PythonWorkSpace/Neural Network Go/input3.txt",number_of_matrix,train_input)
##parser("C:/PythonWorkSpace/Neural Network Go/output3.txt",0,train_test)
#parse_output("C:/PythonWorkSpace/Neural Network Go/output3.txt",train_output)
#parser("C:/PythonWorkSpace/Neural Network Go/input2.txt",number_of_matrix,test_input)
#parse_output("C:/PythonWorkSpace/Neural Network Go/output2.txt",test_output)


adress_list=glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train/*")
print(len(adress_list))
adress_list+=glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train2012/*")
adress_list+=(glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train2012/*"))
adress_list+=(glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train2013/*"))
adress_list+=(glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train2014/*"))
adress_list+=(glob.glob("C:/PythonWorkSpace/Neural_Network_Go/train2015/*"))
print(len(adress_list))
temp=50
number_of_training=50
for i in range(0,number_of_training):
    
    model.compile(optimizer=tf.train.AdamOptimizer(learning_rate=math.exp(-0.1*i) ,epsilon=0.1),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    
    train_input,train_output=loadnpy(adress_list[int(len(adress_list)*(i/number_of_training)):int(len(adress_list)*((i+1)/number_of_training))])
    history=model.fit(train_input,train_output,validation_split=0.05, epochs=2,callbacks = [cp_callback])
    model.save('C:/PythonWorkSpace/Neural_Network_Go/NN07092018/%s_%sgame_model_07092018.h5'%(i,number_of_training))

predictions = model.predict(train_input)
print(model.summary())
# list all data in history

print(history.history.keys())

# summarize history for accuracy

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='best')
plt.show()

# summarize history for loss

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#

#test_input,test_output=loadnpy("C:/PythonWorkSpace/Neural_Network_Go/test1/*")

def debug_predict(n):
    plt.show(plt.matshow(train_input[n][0]))
    plt.show(plt.matshow(train_input[n][1]))
    plt.show(plt.matshow(train_input[n][2]))
    print(train_output[n])
    plt.show(plt.matshow(np.reshape(predictions[n],(19,19))))
    print(np.argmax(predictions[n]))
    


#test_loss, test_acc = model.evaluate(test_input, test_output)
#print('Test accuracy:', test_acc)




# accuracy on the test set of data
#
#test_loss, test_acc = model.evaluate(test_input, test_output)
#    
#print('Test accuracy:', test_acc)


