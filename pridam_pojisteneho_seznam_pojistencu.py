
class PridamVratimPojisteneho:
    # vytvořena třída pro seznam
    def __init__(self):
        self.seznam_pojistencu = []
        
    def pridej(self, pojisteny):
        # metoda přidá nového pojištěnce do seznamu
        self.seznam_pojistencu.append(pojisteny)

    def vrat(self):
        # vrátí se aktualizovaný seznam
        return self.seznam_pojistencu
    
    def __str__(self):
        return " "             
         
        
