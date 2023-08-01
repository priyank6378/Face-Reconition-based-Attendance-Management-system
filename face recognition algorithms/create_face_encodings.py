import face_recognition as fr
import os
import pickle
import sys
import cv2

base =  r"E:\semester 5\mini project 1\dataset"
names = os.listdir(base)                # names of people
person_face_encodings = dict()

print(sys.version)
try :
    for name in names:
        person_face_encodings[name] = []
        for file_name in os.listdir(base+'/'+name):
            img = cv2.cvtColor(cv2.imread(base+'/'+name+'/'+file_name), cv2.COLOR_BGR2RGB)
            encodings = fr.face_encodings(img)
            if len(encodings):
                person_face_encodings[name].append(encodings[0])
    file = open("./face_encodings.pickle", 'wb')
    pickle.dump(person_face_encodings, file)
    file.close()
except Exception as e:
    print(e)
    print("Something went wrong!")
    os._exit(1)



# try:
#     file = open("./face_encodings", 'rb')
#     person_face_encodings = pickle.load(file)
#     file.close()
# except:
#     print("Something went wrong!")


# INPUT_SHAPE = (200,200)

# def get_faces_from_image(img, input_shape = INPUT_SHAPE):
#     """Extract the faces from the image:
#         returns : list of faces , image with bounding box on faces
#         list of faces : are ready for input to the learning model just adjust the INPUT_SHAPE
#     """
#     detector = dlib.cnn_face_detection_model_v1('./mmod_human_face_detector.dat')
# #     detector = dlib.get_frontal_face_detector()
#     gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = detector(gray_img)
#     cropped_faces = []
#     take = 7  # increase the size of the bounding box
#     for face in faces:
#         cropped_faces.append(img[ face.rect.top()-take :face.rect.bottom()+take, face.rect.left()-take:face.rect.right()+take , :].copy())
#     cropped_faces = [cv2.resize(face, dsize=INPUT_SHAPE) for face in cropped_faces]
#     for face in faces:
#         cv2.rectangle(img,(face.rect.left()-5, face.rect.top()-5), (face.rect.right()+5, face.rect.bottom()+5) ,(0,255,0), 1)
#     return cropped_faces , img


# img = load_img('./images/test1.jpg')
# img = img_to_array(img)
# img = np.uint8(img)
# cropped_faces, img = get_faces_from_image(img)
# print(len(cropped_faces), cropped_faces[0].shape)
# plt.imshow(img)


# ans = dict()
# face_vs_name = []
# for i,face in enumerate(cropped_faces):
#     unknown_encoding = fr.face_encodings(face)
#     if len(unknown_encoding):
#         for k,v in person_face_encodings.items():
#             result = fr.compare_faces(v, unknown_encoding[0])
#             ans[k] = np.sum(np.array(result))

#         face_name = (max(ans.items(), key=lambda i: i[1]))
#         if face_name[1] > 10:
#             face_vs_name.append(face_name)
#         else :
#             face_vs_name.append("UNKNOWN")
        
#     else :
#         face_vs_name.append("~ENCODING")

# fig, axes = plt.subplots( math.ceil(len(face_vs_name)/2) , 2 )
# for i,face in enumerate(cropped_faces):
#     axes.ravel()[i].imshow(face)
#     axes.ravel()[i].set_title(face_vs_name[i])
#     axes.ravel()[i].axis('off')
# fig.tight_layout()
