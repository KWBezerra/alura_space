from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label= 'Nome de login',
        required= True,
        max_length= 100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João Silva",
            }
        )

    )

    senha = forms.CharField(
        label= 'Senha',
        required= True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha",
            }
        )
    )

# Cada formulario é defindo por uma classe
# Criamos uma variavel para cada campo do formulário
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label= 'Nome de cadastro',
        required= True,
        max_length= 100,
        widget=forms.TextInput(  # o widget permite editar o input mudando suas caracteristicas EX: PasswordInput()
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: João Silva",
            }
        )
    )

    email = forms.EmailField(
        label= 'Email', # nome que fica em cima do input
        required= True, # torna obrigatorio o campo
        max_length= 100,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: joao@email.com",
            }
        )
    )

    senha_1 = forms.CharField(
        label= 'Senha',
        required= True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha",
            }
        )
    )

    senha_2 = forms.CharField(
        label= 'Senha',
        required= True,
        max_length= 70,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Digite sua senha novamente",
            }
        )
    )

