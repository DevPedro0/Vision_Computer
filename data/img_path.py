from deepface import DeepFace
import cv2

class Img():
    class Path():
        def __init__(self, path):
            self.path = path

        def get_path(self,name:str, *args, **kwargs):
            import os # Os Import, para Listar Dir e Add File Aluno
            img_path = f"{name}.jpg"
            for i in os.listdir(os.path.abspath()):
                ...


    class Cam():
        def __init__(self):
            self.c = cv2.VideoCapture(0)
            self.r, self.f = None, None
            if not self.c.isOpened():
                raise Exception("Cam is not Found")
            
            self.r, self.c = self.c.read()

    def __init__(self):
        self.p = self.Path()
        self.c = self.Cam()

    def run_img(self, *args, **kwargs):
        self.c
        self.p