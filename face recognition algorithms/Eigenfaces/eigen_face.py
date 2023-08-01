import numpy as np
import cv2
import os
import dlib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from data_preprocessing import preprocess_data

SIZE = (200,200)

base_dir = r"E:\semester 5\mini project\face recognition algorithms\dataset"
i = 0
names = {}
for p in os.listdir(base_dir):
    names[p] = i
    i+=1

###################################
def make_dataset():
    base_dir = r"E:\semester 5\mini project\face recognition algorithms\dataset"
    training_images_dir = [base_dir+'\\'+name for name in os.listdir(base_dir)]
    names = {}
    i = 0
    for p in os.listdir(base_dir):
        names[p] = i
        i+=1
    X = []
    y = []
    for person_dir in training_images_dir:
        for img in os.listdir(person_dir):
            image = cv2.imread(person_dir+'\\'+img)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image, SIZE)
            # image = image/255
            X.append(image)
            y.append(names[person_dir.split('\\')[-1]])
    data = np.array(X)
    labels = np.array(y)
    return data,labels

###################################
def get_faces_from_image_2(img):
    detector = dlib.get_frontal_face_detector()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_img)
    cropped_faces = []
    take = 0  # increase the size of the bounding box
    for face in faces:
        cropped_faces.append(img[ face.top()-take :face.bottom()+take, face.left()-take:face.right()+take , :].copy())
    return cropped_faces

##################################
x,y = make_dataset()
x_train ,x_test, y_train, y_test = train_test_split(x,y,test_size=0.10, random_state=60)
x_train = preprocess_data(x_train)
x_test = preprocess_data(x_test)

if 'EIGENFACE' not in os.listdir(r'E:\semester 5\mini project\face recognition algorithms'):
    x,y = make_dataset()
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.train(x,y)
    face_recognizer.write('EIGENFACE')

else :
    print("Loading...")
    face_recognizer = cv2.face.EigenFaceRecognizer_create()
    face_recognizer.read('EIGENFACE')

test_img = r"E:\semester 5\mini project\face recognition algorithms\dataset\Hrishi\1.jpg"
image = cv2.imread(test_img)
faces = get_faces_from_image_2(image)


if len(faces):
    index = 0
    plt.imshow(faces[index][:,:,::-1])
    face = cv2.cvtColor(faces[index], cv2.COLOR_BGR2GRAY)
    face = cv2.resize(face, SIZE)
    prediction, confidence = face_recognizer.predict(face)
    print([k for k,v in names.items() if v==prediction])
    print("confidence :", confidence)
    plt.show()

predictions = []
for i in x_test:
    predictions.append(face_recognizer.predict(i))

# predictions = np.array(predictions)
# y_test = np.array(y_test)
# accuracy = np.sum(np.sum(predictions[:,0]==y_test))/len(predictions)
# print(accuracy)
# print(predictions[:,0])