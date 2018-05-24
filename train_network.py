import numpy as np
import time
import tflearn
from tflearn.data_utils import shuffle
import pandas as pd
import tensorflow as tf
import sys
import numpy as np
import matplotlib as mpl
from shutil import copyfile
mpl.use('Agg')
import matplotlib.pyplot as plt

current_milli_time = lambda: int(round(time.time() * 1000))

def calc_distance(predictions, targets, inputs):
    return tf.nn.l2_loss(tf.subtract(predictions, targets), name='l2')

run_id = "run_" + str(np.random.randint(10000));
if len(sys.argv) >= 2:
    run_id = "run_" + str(sys.argv[1])

print "Reading data"

import h5py
h5f = h5py.File('data/data.h5', 'r')
x = h5f['X'][:, [0,1,2,3,4,6,9,10]] # no 
y = h5f['Y'][:]
print "Data read"
print np.min(y),np.max(y)
net = tflearn.input_data(shape=[None, 8])
net = tflearn.batch_normalization(net)
net = tflearn.fully_connected(net, 500, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 500, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 500, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 500, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 500, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 500, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 5000, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 5000, activation='relu', regularizer='L2')
net = tflearn.fully_connected(net, 5000, activation='tanh', regularizer='L2')
net = tflearn.fully_connected(net, 1, activation='linear', regularizer='L2')

net = tflearn.regression(net, metric=None, loss='mean_square')
model = tflearn.DNN(net, checkpoint_path='./model_checkpoints')

model.fit(x, y, n_epoch=50, batch_size=2048,run_id=run_id, show_metric=True,validation_set=0.1)
model.save('./models/' + run_id + '.tflearn')
