from cards.models import Card

c1 = Card(question="Hello", answer="Hola")
c2 = Card(question="Please", answer="Por favor")
c3 = Card(question="Sorry", answer="Lo siento", box=2)

c1.save()
c2.save()
c3.save()
