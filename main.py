from data.img_path import Img
from models.identification import Idenfitication

class PipelineRunner():
    def __init__(self):
        pass

    def preparation(self):
        '''
        Preparação dos Dados, Obtenção de Imagens e Distribuição para o Run Class
        '''
        ...

    def __call__(self, *args, **kwds):
        self.preparation()

class Run():
    pipeline_r = PipelineRunner()
    def __init__(self, id:Idenfitication = None):
        ...

    def __call__(self, *args, **kwds):
        self.pipeline_r()

run = Run()
run()