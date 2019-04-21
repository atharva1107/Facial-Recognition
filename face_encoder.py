import face_recognition

image = face_recognition.load_image_file("person.jpeg")

face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    print("No faces found!")
else:
    first_face_encoding = face_encodings[0]
    print(first_face_encoding)
    print(len(face_encodings), "face found")