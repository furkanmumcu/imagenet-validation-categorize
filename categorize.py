import utils
import shutil

index_file = 'imagenet_class_index.json'
val_classes_dir = 'val_truth_caffe.txt'
target_folder = 'imagenet_val_cats'
val_dir = 'imagenet_val'

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


for i in range(len(val_classes)):
	val_class = val_classes[i]
	val_class = val_class.split()
	val_class_file_name = val_class[0]
	val_class_index = val_class[1]

	pic_file_location = val_dir + '/' + val_class_file_name

	subfolder_name = index[str(val_class_index)][0]
	target_subfolder = target_folder + '/' + subfolder_name

	print(pic_file_location + " " + target_subfolder)
	shutil.move(pic_file_location, target_subfolder)