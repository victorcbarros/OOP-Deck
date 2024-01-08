#Programa que simula um baralho do livro Pense em Python para programação orientada a Objetos


#importando o metodo random
import random

#Criando a classe Carta



class Carta:
    """
    Representa uma carta do baralho 

    Os naipes estão relacionados a numeros:
    Espadas --> 3
    Copas --> 2
    Ouros --> 1 
    Paus --> 0 
    """


    nome_dos_naipes = ['Paus','Ouros','Copas','Espadas']
    nome_do_valor = [None,'Ás','2','3','4','5','6','7','8','9','10','Valete','Rainha','Rei']

    #Chamando a função construtora
    def __init__(self,naipe,valor):
        self.naipe = naipe
        self.valor = valor
    
    
    #Representação string da carta 
    def __str__(self):
        return '%s de %s' %(Carta.nome_do_valor[self.valor],Carta.nome_dos_naipes[self.naipe])
    
    #função para conferir os Naipes
    def __lt__(self,other):
        t1 = self.naipe, self.valor
        t2 = other.naipe, other.valor
        return t1 < t2 
    
#criação do baralho
class Baralho:

    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for valor in range(1,14):
                carta = Carta(naipe,valor)
                self.cartas.append(carta)


    #Representação string do Baralho
    def __str__(self):
        res = []
        for carta in self.cartas:
            res.append(str(carta))
        return '\n'.join(res)
    
    def retira_carta(self):
        return self.cartas.pop()
    
    def adiciona_carta(self,carta):
        self.cartas.append(carta)


    def embaralha_cartas(self):
        random.shuffle(self.cartas)

    def organiza_cartas(self):
        self.cartas.sort()

    #emcapsulando o codigo no metodo que distribui a mao para o jogador do baralho 
    def move_mao(self,mao,numero):
        for i in range(numero):
            mao.adiciona_carta(self.retira_carta())



#Criando uma subclasse do Baralho para representar uma mão de poker
class Mao_Poker(Baralho):
    """
    Representa uma mão de poker 
    """

    #Como a mão de poker tem propriedades de construção diferente do Baralho
    def __init__(self,label):
        self.cartas = []
        self.label = label



baralho1 = Baralho()
print(baralho1)


