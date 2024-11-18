# forms.py
from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome do Produto')
    preco = forms.DecimalField(max_digits=10, decimal_places=2, label='Preço')

class ContatoForm(forms.Form):
    
    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )
    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4})
    )

class ProdutoForm(forms.Form):
    
    nome = forms.CharField(
        max_length=100, 
        label='Nome do Produto',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do produto'})
    )
    
    preco = forms.DecimalField(
        max_digits=10,
        label='Preço',
        decimal_places=2,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o preço do produto',
            'data-mask': '#.##0,00',
            'data-mask-reverse': 'true'
        })
    )
    