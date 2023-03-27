class Menu():
    # vytvoří rozcestník
    
    def __init__(self, cislo_operace=None):
        self.cislo_operace = cislo_operace
                
    def rozcestnik(self):
        if self.cislo_operace == 1:
            self.cislo_operace = 1  
        elif self.cislo_operace == 2:
            self.cislo_operace = 2
        elif self.cislo_operace == 3:
            self.cislo_operace = 3
        elif self.cislo_operace == 4:
            raise SystemExit
        else:
            print("Není ve výběru.")
                    
    def __str__(self): 
        return str(self.cislo_operace)