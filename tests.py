from django.test import TestCase
from django.urls import reverse
from .models import Mystickynote

class mystickynote (TestCase):
    
   # @classmethod
   # def setUpTestData(cls):
       # Mystickynote.objects.create(title= "test mystickynote",
       # description = "This is a test mystickynote",
       # is_completed=False,
       # created_by ="Test User")
                                    
        def setUp(self) -> None:
            Mystickynote.objects.create (title= "test mystickynote", 
                                     description = "This is a test mystickynote",
                                     is_completed=False,
                                     created_by ="Test User")
        
        def test_Mystickynote_create_has_title(self):
            Mystickynote= Mystickynote.objects.get(id=1)
            
            self. assertedEqual(Mystickynote.description, "This is a test Mystickynote")
            class MystickynoteviewTest (TestCase):
                def setUp(self) -> None:
                    Mystickynote.objects.create (title= "test mystickynote", 
                                     description = "This is a test mystickynote",
                                     is_completed=False,
                                     created_by ="Test User")
                    
                    def test_get_all_returns_correct_values(self):
                        response  = self.client_get(reverse('Mystickynotes'))
                        
                        self.assertEqual(response.status_code,200)
                        self.assertContains(response, "Test Mystickynote" )
                        
                        def test_get_returns_correct_values(self):
                            Mystickynote= Mystickynote.objects.get(id=1)
                            response= self.client.get(reverse('mystickynote', args=[mystickynote.pk]))
                            
                            self.assertEqual(response.status_code,200)
                        self.assertContains(response, "Test Mystickynote" )
                        
                        def test_create_adds_Mystickynote_to_database(self):
                            start_counter = Mystickynote.objects.count()
                            
                        response  = self.client.post (reverse('Mystickynotes'),
                                                      title = "new mystickynote",
                                                       description = "This is a new mystickynote",
                                                       is_completed=False,
                                                       created_by ="Test User")
                        
                        final_count = mystickynote.objects.count()
                        
                        self.assertEqual(response.status_code,302)
                        self.assergtNotEqual(final_count)
                        
                        
                            
                        
                        
        
                

# Create your tests here.
