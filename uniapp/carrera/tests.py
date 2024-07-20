from django.test import TestCase
from .models import Maestro
from django.core.exceptions import ValidationError


class TestMaestro(TestCase):

    def test_grabacion(self):
        with self.assertRaises(ValidationError) as qv:
            q = Maestro.objects.create(nombre='No permitido')
            q.full_clean()

        mensaje_error = dict(qv.exception)
        self.assertEqual(mensaje_error["nombre"][0], "No es una opcion permitida")
