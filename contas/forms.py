from operator import mod
from django.forms import ModelForm
from .models import DadosPessoais

class DadosPessoaisform(ModelForm):
    class Meta:
        model = DadosPessoais
        fields = ['nome','idade','musica_favorita','cor_favorita','jogo_favorito']