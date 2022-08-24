import os
import json
from os import walk
import random
import shutil


def get_imagenet_index(index_file):
	with open(index_file) as json_data:
		index = json.load(json_data)
	return index


def get_validation_classes(validation_file):
	with open(validation_file) as file:
		lines = file.readlines()
		lines = [line.rstrip() for line in lines]
	return lines


def create_subfolders(sub_folder_names, main_folder):
	# create main folder first
	if not os.path.exists(main_folder):
		os.makedirs(main_folder)

	# create folders
	for i in range(len(sub_folder_names)):
		subfolder_name = main_folder + '/' + sub_folder_names[i]
		if not os.path.exists(subfolder_name):
			os.makedirs(subfolder_name)


def list_file_names(path):
	file_names = next(walk(path), (None, None, []))[2]
	return file_names


def select_subset():
	classes = random.sample(range(0, 999), 100)  # choose random classes
	classes.sort()
	imagenet_index = get_imagenet_index('imagenet_class_index.json')
	subset = []
	# get sysnet folder names
	for i in range(len(classes)):
		subset.append(imagenet_index[str(classes[i])][0])

	# copy folders
	for i in range(len(subset)):
		shutil.copytree('imagenet_val_cats' + '/' + subset[i], 'sprt-test-set' + '/' + subset[i])

	# create dict file
	keys = list(range(100))
	dictionary = dict(zip(keys, classes))
	with open('test_dict.txt', 'w') as filehandle:
		json.dump(dictionary, filehandle)

	return subset