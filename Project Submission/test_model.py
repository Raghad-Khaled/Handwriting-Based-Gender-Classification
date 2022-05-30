import time 
import cv2
import os

# input files directories
print("please input full test file directory")
TEST_DIRECTORY = input()

print("please input full output file directory")
OUTPUT_DIRECTORY = input()

predicted_class = []
time_list = []

# read images 
for filename in os.listdir(TEST_DIRECTORY):
    image = cv2.imread(os.path.join(TEST_DIRECTORY,filename), 0)
    if image is not None:
        start_time = time.time()

        k=10
        wshape=(100*k,142*k)

        image=cv2.resize(image,wshape)
        image = cv2.GaussianBlur(image,(3,3),cv2.BORDER_DEFAULT)

        image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2) # making the image binary
        image = cv2.medianBlur(image, 5)
        image = cv2.medianBlur(image, 5)
        image = cv2.erode(image, None, iterations = 1)

        # predicted_class.append() # here call preprocessing function and the model
        end_time = time.time() - start_time
        if(end_time < .001):
            time_list.append(.001)
        else:
            time_list.append(end_time)


result_file = open(OUTPUT_DIRECTORY + '/results.txt', 'w')
time_file = open(OUTPUT_DIRECTORY + '/times.txt', 'w')
for i in range(len(time_list)):
    result_file.write(predicted_class[i] + '\n')
    time_file.write(time[i] + '\n')