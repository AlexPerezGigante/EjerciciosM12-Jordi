from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Habitant():
    def __init__(self, nom, cognom, any, ciutat):
        self.nom=nom
        self.cognom=cognom
        self.any=any
        self.ciutat=ciutat

        

def saludo(request):

    h1=Habitant("Ferran","Torres","1999","Barcelona")

    alumno=["Lamine","Yamal", "2007", "Barcelona"]

    ahora=datetime.datetime.now()

    modulo=["m8 - Desplegamiento", "m12 - Proyecto" , "m2 - BBDD" , "m9 - Diseño" , "m7 - Servidor" , "m6 - Programación web"]

    doc_externo=open("C:/Users/Administrator/Desktop/Objectiu3-Plantilles/Proyecto3/Plantillas/plantilla.html")
    
    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_habitante":h1.nom , "apellido_habitante":h1.cognom , "anyo_habitante":h1.any , "ciudad_habitante":h1.ciutat , "info_alumno":alumno , "ahora_mismo":ahora , "lista_modulos":modulo})

    documento=plt.render(ctx)

    return HttpResponse(documento)


