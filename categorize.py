import os
import utils

index_file = 'imagenet_class_index.json'
val_classes_dir = 'ILSVRC2012_validation_ground_truth.txt'
target_folder = 'imgnet'
val_dir = 'test'

# get imagenet index
index = utils.get_imagenet_index(index_file)
print(index)

# create folders
folders = []
for i in range(len(index)):
	folders.append(index[str(i)][0])
utils.create_subfolders(folders, target_folder)

# get validation set classes
val_classes = utils.get_validation_classes(val_classes_dir)
print(len(val_classes))

# move val images to corresponding folders
val_files = utils.list_file_names(val_dir)

for i in range(len(val_classes)):
	val_class = val_classes[i]
	subfolder_name = index[str(val_class)]
	pic_file_location = val_dir + '/' + val_files[i]
	target_subfolder = target_folder + '/' + subfolder_name
	print(pic_file_location + " " + target_subfolder)
	#os.replace(pic_file_location, target_subfolder)