import face_recognition as fr
import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np
import math
import os


try:
    file = open("./face_encodings.pickle", 'rb')
    person_face_encodings = pickle.load(file)
    file.close()
except:
    print("Something went wrong!")
    os._exit(1)



def recognize_faces(img_path):
    img = fr.load_image_file(img_path)
    img = np.uint8(img)
    cropped_faces, img = face_detection_1(img)
    # print(len(cropped_faces), cropped_faces[0].shape)
    # plt.imshow(img)
    # plt.show()

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

    # fig, axes = plt.subplots( math.ceil(len(face_vs_name)/2) , 2 )
    # for i,face in enumerate(cropped_faces):
    #     axes.ravel()[i].imshow(face)
    #     axes.ravel()[i].set_title(face_vs_name[i])
    #     axes.ravel()[i].axis('off')
    # fig.tight_layout()
    # plt.show()

    return face_vs_name

if __name__ == '__main__':
    recognize_faces('./images/test6.jpg')
