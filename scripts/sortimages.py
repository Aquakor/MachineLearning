from csv import reader
import os
import shutil

# Load a CSV file
def load_csv(filename):
	file = open(filename, "r")
	lines = reader(file)
	dataset = list(lines)
	return dataset

# Convert string column to integer
def str_column_to_int(dataset, column):
    for i in dataset:
        i[column] = int(i[column])
    
# Copy files to proper folders    
def sort_images(images, csvfile, name_column, label_column):
    for image in images:
        for i in csvfile:
            if i[name_column] == image:
                if i[label_column] == 0:
                    shutil.move(os.path.join(image_path, image), none_path)
                    print('Successfully copied image to none')
                elif i[label_column] == 1:
                    shutil.move(os.path.join(image_path, image), red_path)
                    print('Successfully copied image to red')
                elif i[label_column] == 2:
                    shutil.move(os.path.join(image_path, image), green_path)
                    print('Successfully copied image to green')
                    
                

# Load dataset
filename = '/home/kornel/version-control/trafficlights/labels.csv'
csvfile = load_csv(filename)
name_column = 0
label_column = 1

image_path = '/home/kornel/version-control/trafficlights/nexar_traffic_light_train'
root_path = '/home/kornel/version-control/trafficlights/'
images = os.listdir(image_path)
none_path = os.path.join(root_path, 'none')
red_path = os.path.join(root_path, 'red')
green_path = os.path.join(root_path, 'green')

# convert label column to int
str_column_to_int(csvfile, label_column)
# sort images to folders none, green, red
sort_images(images, csvfile, name_column, label_column)