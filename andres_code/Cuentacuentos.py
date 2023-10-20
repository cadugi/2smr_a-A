import random 
  
Sentence_starter = ['Hace 100 años', ' Por el 20 AC', 'Hubo una vez'] 
character = [' vivía un rey.',' vivía un hombre llamado Aletheia.', 
             ' vivía un granjero.'] 
time = [' Un día', ' Una noche de luna llena'] 
story_plot = [' que paseaba por',' estaba en un picnic por '] 
place = [' las montañas', ' el jardín'] 
second_character = [' vió a un hombre a lo lejos', ' vió a una bella dama a la distancia'] 
age = [' quien se veía cerca de los 20s', ' quien se veía viejo and feeble'] 
work = [' buscando algo.', ' cavando un pozo en el camino.'] 

print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work)) 
input()