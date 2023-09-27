from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: José Silva"}
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        )
    )

class RegisterForm(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: José Silva"}
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Ex.: josesilva@xpto.com"}
        )
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        )
    )

    confirmar_senha = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha mais uma vez"}
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo!")
            else:
                return nome


