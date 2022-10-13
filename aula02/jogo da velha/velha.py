import os


class Velha:
    matriz = None
    player01 = None
    player02 = None
    
    def __init__(self, player01, player02, matriz = [[None for i in range(3)] for x in range(3)]):
        self.matriz = matriz
        self.player01 = player01
        self.player02 = player02
        
    def f(self):
        for x in self.matriz:
            print(x)
   
    def displayer(self):
        cont = [0, 0]
        for x in self.matriz:
            cont[1] = 0
            texto = ""
            for i in x:
                if(cont[0] != 2):
                    if(i == None):
                        texto += "___"
                    elif(i == 1):
                        texto += "_X_"
                    elif(i == 0):
                        texto += "_O_"
                else:
                    if(i == None):
                        texto += "   "
                    elif(i == 1):
                        texto += ' X '
                    elif(i == 0):
                        texto += " O "
                        
                if(cont[1] == 0):
                    texto += "|"
                if(cont[1] == 1):
                    texto += "|"
                cont[1] += 1
            print(texto)
            cont[0] += 1
            
    def play(self):
        print("Essas são as opções de jogo:")
        print("_1_|_2_|_3_\n"
              "_4_|_5_|_6_\n"
              " 7 | 8 | 9 ")
        os.system("pause")
        os.system("cls")
        for x in range(9):
            os.system('cls')
            self.displayer()
            
            p1 = int(input('Digite a posição que %s quer jogar: '%(self.player01)))
            self.j(self.player01, p1)
            os.system("cls")
            self.displayer()
            p2 = int(input('Digite a posição que %s quer jogar: '%(self.player02)))
            self.j(self.player02, p2)
            os.system('cls')
            self.displayer()
            
            os.system("pause")
        
    def j(self, player, position):
        simbulo = None
        if(player == self.player01):
            simbulo = 1
        else:
            simbulo = 0
        if(position == 1):
            if(self.verify(self.matriz[0][0]) == True): 
                self.matriz[0][0] = simbulo
        elif(position == 2):
            if(self.verify(self.matriz[0][1]) == True): 
                self.matriz[0][1] = simbulo
        elif(position == 3):
            if(self.verify(self.matriz[0][2]) == True): 
                self.matriz[0][2] = simbulo
        elif(position == 4):
            if(self.verify(self.matriz[1][0]) == True): 
                self.matriz[1][0] = simbulo
        elif(position == 5):
            if(self.verify(self.matriz[1][1]) == True): 
                self.matriz[1][1] = simbulo
        elif(position == 6):
            if(self.verify(self.matriz[1][2]) == True): 
                self.matriz[1][2] = simbulo
        elif(position == 7):
            if(self.verify(self.matriz[2][0]) == True): 
                self.matriz[2][0] = simbulo
        elif(position == 8):
            if(self.verify(self.matriz[2][1]) == True): 
                self.matriz[2][1] = simbulo
        elif(position == 9):
            if(self.verify(self.matriz[2][2]) == True): 
                self.matriz[2][2] = simbulo
            
    def verify(self, matriz):
        return matriz == None
        
jogo = Velha('jose', 'carlos')
jogo.play()