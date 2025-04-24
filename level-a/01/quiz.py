# Classe responsável por iniciar o quiz
class Start:
    def __init__(self):
        print("Seja muito bem vindo ao quiz do Iury!")
        # Pergunta se o usuário deseja começar o quiz
        self.__answer_user = input("Quer começar? (S/N) ")
        # Se a resposta não for "S", o programa encerra
        if self.__answer_user.upper() != "S":
            quit()

# Classe responsável pela lógica do quiz
class Quiz:
    # Construtor que recebe a lista de respostas corretas e as perguntas
    def __init__(self, answer_quiz, question_quiz):
        self.__score = 0  # Inicializa a pontuação com zero
        self.__answer_quiz = answer_quiz  # Lista com as respostas corretas
        self.__question_quiz = question_quiz  # Lista com as perguntas
        print("Começando...")

    # Função que faz as perguntas ao usuário
    def question(self):
        # Loop para percorrer todas as perguntas
        for x in range(len(self.__answer_quiz)):
            print(self.__question_quiz[x])  # Exibe a pergunta atual
            self.__answer_user = input("Resposta: ")  # Recebe a resposta do usuário
            
            # Verifica se a resposta está correta
            if self.__answer_user != self.__answer_quiz[x]:
                print("Incorreto!")  # Mensagem de erro
                continue  # Pula para a próxima pergunta
                
            print("Correto!")  # Mensagem de acerto
            self.__score = self.__score + 1  # Incrementa a pontuação

        # Exibe a pontuação final
        print(f"Quiz acabou... Pontuação: {self.__score}/2")

# Função principal do programa
def main():
    start = Start()  # Instancia a classe Start para iniciar o quiz
    # Cria o objeto Quiz com as respostas e perguntas e chama o método 'question'
    quiz = Quiz(
        ["A", "B"],
        [
            "Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n",
            "Qual o nome do protagonista do jogo GTA San Andreas?\n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n"
        ]
    ).question()

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
