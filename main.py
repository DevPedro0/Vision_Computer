from data.img_path import Img
from models.identification import Identification
from abc import ABC, abstractmethod

# Implementar ABC para Class Based -> Run()
class PipelineRunner():
    def __init__(self):
        pass

    def preparation(self):
        '''
        Preparação dos Dados, Obtenção de Imagens e Distribuição para o Run Class
        '''
        img = Img().Path()

    def __call__(self, *args, **kwds):
        self.preparation()

class Run():
    pipeline_r = PipelineRunner()
    def __init__(self, id:Identification = None):
        ...

    def __call__(self, *args, **kwds):
        self.pipeline_r()

run = Run()
run()