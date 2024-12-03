from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio1 = Laboratorio.objects.create(nombre="Laboratorio1", pais="País1", ciudad="Ciudad1")
        cls.laboratorio2 = Laboratorio.objects.create(nombre="Laboratorio2", pais="País2", ciudad="Ciudad2")
        cls.laboratorio3 = Laboratorio.objects.create(nombre="Laboratorio3", pais="País3", ciudad="Ciudad3")

    def test_laboratorio_data(self):
        """Verifica que los datos en la base de datos coinciden con los creados"""
        laboratorio1 = Laboratorio.objects.get(nombre="Laboratorio1")
        laboratorio2 = Laboratorio.objects.get(nombre="Laboratorio2")
        laboratorio3 = Laboratorio.objects.get(nombre="Laboratorio3")
        
        self.assertEqual(laboratorio1.nombre, "Laboratorio1")
        self.assertEqual(laboratorio1.pais, "País1")
        self.assertEqual(laboratorio1.ciudad, "Ciudad1")

        self.assertEqual(laboratorio2.nombre, "Laboratorio2")
        self.assertEqual(laboratorio2.pais, "País2")
        self.assertEqual(laboratorio2.ciudad, "Ciudad2")

        self.assertEqual(laboratorio3.nombre, "Laboratorio3")
        self.assertEqual(laboratorio3.pais, "País3")
        self.assertEqual(laboratorio3.ciudad, "Ciudad3")

    def test_laboratorio_url(self):
        """Verifica que la URL devuelve una respuesta HTTP 200"""
        url = reverse('mostrar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_template(self):
        """Verifica que la plantilla usada sea la correcta y contiene el contenido esperado"""
        url = reverse('mostrar')  
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'laboratorio/mostrar.html') 
        self.assertContains(response, "Laboratorio1")
        self.assertContains(response, "Laboratorio2")
        self.assertContains(response, "Laboratorio3")
        self.assertContains(response, "País1")
        self.assertContains(response, "País2")
        self.assertContains(response, "País3")
        self.assertContains(response, "Ciudad1")
        self.assertContains(response, "Ciudad2")
        self.assertContains(response, "Ciudad3")
