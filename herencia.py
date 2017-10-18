class Corcho(object):
    def __init__(self,bodega=""):
        
        if bodega:
            self.bodega=bodega
        else:
            raise AttributeError("El nombre de la bodega no debe ser una cadena vacia")

    def __str__(self):
        return "La Bodega del corcho es:"+str(self.bodega)
    
class Botella(object):
    def __init__(self,Corcho=""):
        
        if Corcho:
            self.corchotapado=Corcho
        else:
            self.corchotapado=None          
    def __str__(self):
        if not self.corchotapado:
            return "La botella esta destapada"
        else:
            return "La botella esta tapada y tiene corcho"+str(self.corchotapado)

class Sacacorchos(object):
    def __init__(self,botella="",corcho=""):
        self.botella=botella
        self.corchotapado=corcho

    def __str__(self):
        return "Tengo la botella : "+str(self.botella)+" y el corcho : "+str(self.corchotapado)


    def destapar(self):
        if self.corchosacado!=None:
            corchodestapado=self.corchotapado
            self.corchotapado=None
            return corchodestapado
        else:
            raise AttributeError("La botella ya se encuentra destapada")

    def limpiar(self,destapar):
        if destapar!=None:
            self.corchotapado=None
        else:
            raise AttributeError("El sacacorchos no tiene corcho")
            

d=Corcho('lalo')
b=Botella(d)


