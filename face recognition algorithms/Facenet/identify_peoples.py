import face_recognition as fr
import os
import pickle
import dlib
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math


try:
    file = open("./face_encodings.pickle", 'rb')
    person_face_encodings = pickle.load(file)
    file.close()
except:
    print("Something went wrong!")
    os._exit(1)


# This function is computationally expensive:
def get_faces_from_image_1(img):
    """Extract the faces from the image:
        returns : list of faces , image with bounding box on faces
        list of faces : are ready for input to the learning model just adjust the INPUT_SHAPE
    """
    detector = dlib.cnn_face_detection_model_v1('./mmod_human_face_detector.dat')
#     detector = dlib.get_frontal_face_detector()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_img)
    cropped_faces = []
    take = 2  # increase the size of the bounding box
    for face in faces:
        cropped_faces.append(img[ face.rect.top()-take :face.rect.bottom()+take, face.rect.left()-take:face.rect.right()+take , :].copy())
    for face in faces:
        cv2.rectangle(img,(face.rect.left()-5, face.rect.top()-5), (face.rect.right()+5, face.rect.bottom()+5) ,(0,255,0), 1)
    return cropped_faces , img


# This function is computationally less expensive and faster:
def get_faces_from_image_2(img):
    detector = dlib.get_frontal_face_detector()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_img,1)
    cropped_faces = []
    take = 7  # increase the size of the bounding box
    for face in faces:
        cropped_faces.append(img[ face.top()-take :face.bottom()+take, face.left()-take:face.right()+take , :].copy())
    for face in faces:
        cv2.rectangle(img,(face.left()-5, face.top()-5), (face.right()+5, face.bottom()+5) ,(0,255,0), 1)
    return cropped_faces , img


def recognize_faces(img_path):
    img = fr.load_image_file(img_path)
    # img = np.uint8(img)
    cropped_faces, img = get_faces_from_image_2(img)
    # plt.imshow(img)
    # plt.show()
    # print("found faces:", len(cropped_faces))
    ans = dict()
    face_vs_name = []
    for i,face in enumerate(cropped_faces):
        unknown_encoding = fr.face_encodings(face)
        if len(unknown_encoding):
            for k,v in person_face_encodings.items():
                result = fr.compare_faces(v, unknown_encoding[0])
                ans[k] = np.sum(np.array(result))

            face_name = (max(ans.items(), key=lambda i: i[1]))
            if face_name[1] > 10:
                face_vs_name.append(face_name[0])
            else :
                face_vs_name.append("UNKNOWN")

        else :
            face_vs_name.append("~ENCODING")

    fig, axes = plt.subplots( len(face_vs_name) , 1 , figsize=(100,100))
    for i,face in enumerate(cropped_faces):
        axes.ravel()[i].imshow(face)
        axes.ravel()[i].set_title(face_vs_name[i])
        axes.ravel()[i].axis('off')
    fig.tight_layout()
    plt.show()
    return face_vs_name

def make_dataset():
    base_dir = r"E:\semester 5\mini project\face recognition algorithms\data"
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
            X.append(person_dir+'\\'+img)
            y.append(person_dir.split('\\')[-1])
    return X,y

if __name__ == '__main__':
    ans = recognize_faces(r"E:\semester 5\mini project\face recognition algorithms\Facenet\test.jpg")
    print(ans)
    ans = recognize_faces(r"E:\semester 5\mini project\face recognition algorithms\Facenet\test1.jpg")
    print(ans)
    
    # img_paths, labels = make_dataset()
    # print(len(img_paths), len(labels))
    # predictions = []
    # for img in img_paths:
    #     ans = recognize_faces(img)
    #     if len(ans)==0:
    #         continue
    #     print(ans)
    #     if ans[0] == labels[img_paths.index(img)]:
    #         predictions.append(1)
    #     else :
    #         predictions.append(0)

    # print("accuracy :", sum(predictions)/len(predictions))