import os
import uuid
import face_recognition
import cv2

class Bag:
    
    def __init__(self):
        self.data = []
        path = "../face_recognition/"
        input_movie = cv2.VideoCapture(path+"Lucifer1.mp4")
        length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

        # Create an output movie file (make sure resolution/frame rate matches input video!)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))
        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        frame_number = 0

        while True:
            # Grab a single frame of video

            ret, frame = input_movie.read()
            frame_number += 1
            rgb_frame = frame[:, :, ::-1]
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            if ret == False:
                break

            # Loop through each face in this frame of video

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

                img = frame
                print(str(top)+" "+str(right)+" "+str(bottom)+" "+str(left))
                crop_img = img[top:bottom, left:right]
                print(crop_img)
                cv2.imshow("cropped", crop_img)
                # cv2.waitKey(0)

                name = "Person"
                directory = os.fsencode(
                    "C:\\Repositories\\opensource\\face\\has\\VideoNewLuci")
                # bu for dongusu methodun icerisinde olacak 
                # eger metod klasorde yuzu bulabilirse true donecek bulamazsa false donecek
                #metod false donerse yuz klasore kaydedilecek
                # results[0] donen degeri veriri if(results[0] seklinde kullanilabilir)
                result = self.checkIfFaceExists(face_encoding)
                print(result)
                if(result is False):
                    cv2.imwrite('VideoNewLuci\\'+ str(uuid.uuid1()) + '.jpg', crop_img)

                

            if (frame_number == 3000):
                break

                input_movie.release()
                cv2.destroyAllWindows()


        # Label the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                continue

            # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 25),
                            (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6),
                            font, 0.5, (255, 255, 255), 1)

        # Write the resulting image to the output video file
                print("Writing frame {} / {}".format(frame_number, length))
                output_movie.write(frame)




    def add(self, x):
        self.data.append(x)

    def checkIfFaceExists(self, unknown_encoding):
        directory = os.fsencode(
            "C:\\Repositories\\opensource\\face\\has\\VideoNewLuci")
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            print(file)
            print(filename)
            imagePathInFolder = os.fsdecode(os.path.join(directory, file))
            print(imagePathInFolder)
            image = cv2.imread(imagePathInFolder)
            cv2.imshow('filename', image)
            known_image = face_recognition.load_image_file(imagePathInFolder)
            knownImage_encoding = face_recognition.face_encodings(known_image)[0]

            results = face_recognition.compare_faces([knownImage_encoding], unknown_encoding)
            print(results)
            if(results[0]):
                return True
        return False

test_instance = Bag()
test_instance.__init__()