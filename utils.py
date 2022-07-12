import os
import json
from os import walk


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
