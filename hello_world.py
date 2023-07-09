"""
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro

Neste script vamos a reproduzir os resultados de teste do Jerry An,
você pode encontrar o artigo na Medium.

Teste de carga com Locust: um guia para iniciantes
==================================================
Link --> https://levelup.gitconnected.com/load-testing-with-locust-a-beginners-guide-5a6efa2898a5

O teste de carga é uma parte essencial do desenvolvimento 
de software, ajudando a garantir que os aplicativos possam 
lidar com o tráfego e o uso esperados.

Locust:
=======
Uma ferramenta de teste de carga de código aberto que usa Python 
para simular o comportamento do usuário e gerar carga. A instalação é:

$ pip install locust


Criando um “Olá, Mundo!” Teste de carga
=======================================
Vamos começar com um simples “Olá, Mundo!” exemplo para demonstrar 
como o Locust funciona. Crie um novo arquivo chamado hello_world.py
e adicione o seguinte código:
"""
from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(1, 2.5) # Intervalo de tempo que o usuário aguardará entre as tarefas.

    @task
    def hello_world(self):
        self.client.get("/")
        print("Olá, Mundo!")

"""
Este código define um usuário do Locust que simulará visitar o URL raiz 
de um site e imprimir “Olá, Mundo!” para o console.

Para executar este teste de carga, abra um terminal ou prompt de comando 
e navegue até o diretório que contém hello_world.py. Em seguida digite o 
seguinte comando 🤗: 
                    $ locust -f hello_world.py 
"""

