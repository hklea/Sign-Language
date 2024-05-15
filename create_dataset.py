import os
import cv2

DATA_DIR='./mydataset'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
#num of folders ,how many each , jpg
num_folders=26
dataset_size=100
img_ext='.jpg'

capture=cv2.VideoCapture(0);
for i in range (num_folders):
    class_dir = os.path.join(DATA_DIR, str(i))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    if i > 0:
        # Display message indicating when to change the sign
        for _ in range(5):  # Display for 5 seconds
            ret, frame = capture.read()
            cv2.putText(frame, "Change sign now", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('SHOOT', frame)
            cv2.waitKey(1000)  
        cv2.destroyAllWindows()   
    print(f'Collecting data for class {i}')
    # Start capturing frames from the camera
    for j in range (dataset_size):
        ret,frame = capture.read();
        cv2.imshow('SHOOT',frame)
        img_path = os.path.join(class_dir, f'image_{j}{img_ext}')
        cv2.imwrite(img_path, frame)
        cv2.waitKey(100);
 

capture.release()
cv2.destroyAllWindows()
