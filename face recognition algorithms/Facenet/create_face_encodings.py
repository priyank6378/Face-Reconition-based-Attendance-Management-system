import face_recognition as fr
import os
import pickle


base = r"E:\semester 5\mini project\face recognition algorithms\dataset"
names = os.listdir(base)                # names of people

person_face_encodings = dict()

for name in names:
    person_face_encodings[name] = []
    for file_name in os.listdir(base+'/'+name):
        img = fr.load_image_file(base+'/'+name+'/'+file_name)
        encodings = fr.face_encodings(img)
        if len(encodings):
            person_face_encodings[name].append(encodings[0])

try :
    file = open("./face_encodings.pickle", 'wb')
    pickle.dump(person_face_encodings, file)
    file.close()
except:
    print("Something went wrong!")
    os._exit(1)
