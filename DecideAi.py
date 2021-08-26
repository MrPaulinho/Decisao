#Faça uma pergunta para o programa e ele terá que te dar uma resposta

#decideAi

import random
import pefile

pe = pefile.PE('DecideAi.exe')
pe.print_info() # Imprimir de formato legivel


class DecideAi:
    def __init__(self):
        self.respostas = [
            'Sim! mas faça julgamentos realísticos',
            'Talvez. Você possui algumas fraquezas que pode acabar afetando mas, no geral, consegue compensá-las',
            'Cuidado! Às vezes você pode criar certas necessidade de ser querido e admirado por outros. Análise os pontos fortes e fracos.',
            'Quer uma mundaça? Faça. Mas se estiver bom, deixa prá lá.'
        ]
    def Iniciar(self):
        input('Respire fundo e faça sua pergunta: ')
        print(random.choice(self.respostas))

    
decide = DecideAi()
decide.Iniciar()

input('Pressione enter para sair')

with open('DecideAi.txt','w', newline='') as file:
    for line in DecideAi:
        file.write(line) 