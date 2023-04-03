# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 01:40:31 2023

@author: Image903
"""

# import the necessary packages
import os
# initialize the path to the input directory containing our dataset
# of images
DATASET_PATH = "Cyclone_Wildfire_Flood_Earthquake_Database"
# initialize the class labels in the dataset
CLASSES = ["Cyclone", "Earthquake", "Flood", "Wildfire"]

# define the size of the training, validation (which comes from the
# train split), and testing splits, respectively
TRAIN_SPLIT = 0.75
VAL_SPLIT = 0.1
TEST_SPLIT = 0.25
# define the minimum learning rate, maximum learning rate, batch size,
# step size, CLR method, and number of epochs
MIN_LR = 1e-6
MAX_LR = 1e-4
BATCH_SIZE = 32
STEP_SIZE = 8
CLR_METHOD = "triangular"
NUM_EPOCHS = 100

# set the path to the serialized model after training
MODEL_PATH = "natural_disaster.model"
# define the path to the output learning rate finder plot, training
# history plot and cyclical learning rate plot
LRFIND_PLOT_PATH = "lrfind_plot.png"
TRAINING_PLOT_PATH = "training_plot.png"
CLR_PLOT_PATH = "clr_plot.png"