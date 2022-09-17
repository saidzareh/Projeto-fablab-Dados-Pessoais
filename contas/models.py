from django.db import models


class DadosPessoais(models.Model):

    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    idade = models.DecimalField(max_digits=3, decimal_places=0)
    musica_favorita = models.CharField(max_length=25)
    cor_favorita = models.CharField(max_length=15)
    jogo_favorito = models.CharField(max_length=30)


    def __str__(self):
        return self.nome
    
    #crud django


    
