class Corcho(object):
    """Abstraccion de clase corcho"""
    def __init__ (self,bodega=""):
        """Constructor de la clase Corcho"""
        if bodega:
            self.bodega=bodega
        else:
            raise AttributeError("El nombre de la bodega no debe ser una cadena vacia")

    def __str__(self):
        """Muestra Corcho"""
        return "La Bodega del corcho es:"+str(self.bodega)


class Botella(object):
    """Abstraccion de la clase Botella"""
    def __init__(self,Corcho=""):
        """Constructor de la clase Botella"""
        if Corcho:
            self.corchotapado=Corcho
        else :
            self.corchotapado=None
    def __str__(self):
        if not self.corchotapado:
            return "La botella esta destapada"
        else :
            return "La botella esta tapada y tiene el corcho :"+str(self.corchotapado)

""" Sacacorchos ...."""
class Sacacorchos(object):
    """Abstraccion de la clase Sacacorchos"""
    def __init__(self,botella="",corcho=""):
        """Constructor de la clase Botella"""
        self.botella=botella
        self.corchotapado=corcho
        self.corchodestapado=None # el estado del destapador es sin corcho
    def __str__(self):
        return "Tengo la botella : "+str(self.botella)+" y el corcho : "+str(self.corchotapado)
    def destapar(self):
        """Saca el corcho de la botella"""
        if self.corchotapado!=None:
            self.corchodestapado=self.corchotapado #colocar el self a corcho destapado para poder visualizar
            self.corchotapado=None
            return corchodestapado
        else :
            raise AttributeError("La botella ya esta destapada")
    def limpiar(self,destapar):
        """Saca el corcho del sacacorchos,o levanta una excepcion en el caso de que no tenga corcho el mismo"""
        if destapar!=None:
            self.corchotapado=None
            self.corchodestapado=None
        else:
            raise AttributeError("El sacacorchos no tiene corcho")



c=Corcho("FLOR\n") # c es un objeto de tipo corcho con nombre de bodega flor print(c)
a=Botella(c ) #aqui sale tapada y el nombre de la bodega del corcho .. xq le paso el valor de c= corcho.print(a)
#a=Botella(None) # no le paso el objeto corcho a la botella ( va a estar destapada)print(a)
b=Sacacorchos(a,c)
b.destapar()#sale resultado None si ahora se encuenta destapado print(b) resultado NOne...
#b.destapar()# si vuelvo a destapa de nuevo me sale el error que cree! print(B)
s=limpiar(b)


print( s)


