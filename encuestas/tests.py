from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()
    
    def testHelloWrold(self):
        response = self.client.get("/users/")
        self.assertContains(response , "Hello world from Django for Codo a Codo 4.0")

    def testSatusCodeHelloWorld(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200 )