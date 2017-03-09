from datetime import datetime
import time

class Marca:

    def __init__(self,nome):
        self.nome=nome
    def __repr__(self):
        return"<Marca %s>" % self.nome

class Automobile:
    def __init__(self,nome,anno,marca,consumo):
        anno=int(anno)
        self.nome = nome
        self.anno = anno
        self.carburante = 0
        self.marca = Marca(marca)
        self.eta = datetime.now().year - anno
        self.consumo = int(consumo)



    def __repr__(self):
        return "<Automobile %s>" % self.nome

    def rifornisci(self,litri):
        self.carburante += litri

    def consuma(self,litri):
        self.carburante -= litri

    def consuma(self,litri):
        self.carburante += self.consumo



if __name__== '__main__':
    nome = raw_input ("nome della macchina:  ")
    anno = raw_input ("anno di fabbricazione (aaaa): ")
    while len(anno) != 4:
        print "errore nel formato dell'anno!"
        anno = raw_input ("anno di fabbricazione (aaaa): ")     
    marca = raw_input ("marca: ")
    consumo = raw_input ("consumo. ")
    mia_auto = Automobile(nome,anno,marca,consumo)
    print "quindi possiedi una %s %s" % (mia_auto.marca.nome,mia_auto.nome)

    print mia_auto

    print "costruita nel %s" % mia_auto.anno

    print "la sua eta e %s" % mia_auto.eta

    print "Carburante %s litri" % mia_auto.carburante
    mia_auto.rifornisci(30)
    print "carburante: %s litri" % mia_auto.carburante 


    secondi = 20
    while secondi > 0:
        mia_auto.consuma()
        if mia_auto.carburante <= 0:
            print "Finita la benza!"
            break


        secondi -= 1
        time.sleep(1)
        print "Carburante %s litri" % mia_auto.carburante
   
    print "Carburante %s litri" % mia_auto.carburante

