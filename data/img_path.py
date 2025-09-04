import cv2 # Cam()
from pathlib import Path # Lib para self.path
import os # Os Import, para Listar Dir e Add File Aluno
from PIL import Image
from threading import Thread as t
import base64 as b

class Img():
    class Path():
        def __init__(self):
            self.path = Path(__file__).parent.parent
            self.errors = (FileExistsError, FileNotFoundError, Exception)
            self.f_jpg = Image # Imagem Pillow

        def _(self, path:str, content = ""):
            try:
                f_path = self.f_jpg.open(path)
                f_path.show(content.join(f"Imagem Test"))
            except self.errors as e:
                for i in self.errors:
                    ...
                
        def get_path(self, name:str, *args, **kwargs):
            f_data = f"data"
            for i in os.listdir(self.path):
                if (os.path.isdir(i)) and i == "data":
                    f_f = r"\{f_data}\{name}.txt"
                    if not (os.path.exists(f_f)):
                        # Function Helpers para criar Arq
                        self._(f_f)
            
            self.path_f = None            
            return # No Caso, Retornar o Path (DIR)
        
        def run(self, *args, **kwargs):
            '''
            name (k) -> value (v)
            '''
            k_n = kwargs.get("name", None)
            self.get_path(k_n)
            
        @property
        def g_path(self):
            if self.path_f is not None:
                return self.path_f
            return []

        @g_path.setter
        def s_path_f(self, new_value:str):
            if isinstance(new_value, str):
                self.path_f = new_value
                return self.path_f
            return None
    class Cam():
        def __init__(self):
            # Connection Cam __init__
            self.c = cv2.VideoCapture(0)
            self.r, self.f = None, None
            self.threads = t # Adicionando Threads para Desenvolvimento em diferentes Ambientes
            if not self.c.isOpened():
                raise Exception("Cam is not Found")
            
            self.r, self.c = self.c.read()

        def open(self):
            ...
            
        def updated_frame(self):
            ...
            
        def threads_cam(self, *args, **kwargs)

    def __init__(self):
        self.p = self.Path()
        self.c = self.Cam()

    def run_img(self, *args, **kwargs):
        self.c
        self.p
        
# Test Instance and Methods
Test = Img.Path()
Test.get_path("pedro")
