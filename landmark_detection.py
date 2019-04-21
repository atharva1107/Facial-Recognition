import PIL.Image
import PIL.ImageDraw
import face_recognition

image = face_recognition.load_image_file("people.jpg")

face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print("Found {} face(s) in this picture.".format(number_of_faces))

pil_image = PIL.Image.fromarray(image)

draw = PIL.ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:
    for name, list_of_points in face_landmarks.items():
        print("The {} in this face has the following points: {}".format(name, list_of_points))
        draw.line(list_of_points, fill="orange", width=2)
pil_image.show()