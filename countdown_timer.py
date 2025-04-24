import time

tempo_em_segundos = int(input("Digite o tempo em segundos: "))
# messagebox.showerror("Erro", "Por favor, insira números válidos.")
# Definindo a função contagem_regressiva

def contagem_regressiva(segundos):
    while segundos:
        min, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(min, secs)
        print(timer, end="\r")  # Atualiza o timer na mesma linha
        time.sleep(1)  # Pausa de 1 segundo entre os números
        segundos -= 1
    print("Acabou o tempo 00:00!")

# Chamando a função
contagem_regressiva(tempo_em_segundos)