from django.core.exceptions import ValidationError

def validar_cedula(value):
    if len(value) != 10:
        raise ValidationError("%(valor)s la cedula de identidad tiene que ser de 10 digitos", params={'valor': value})

def validation_maestro(value):
    if value == "ninguno":
        raise ValidationError("No es una dato permitido")
