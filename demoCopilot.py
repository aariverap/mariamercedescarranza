// importa spacy (un paquete popular para hacer Procesamiento de Lenguaje Natural o NLP)
import spacy

// crea un objeto nlp vacío para procesar español (el objeto que contiene el pipeline del procesamiento se guardará en la variable 'nlp')
nlp = spacy.blank("es")

// crea un string de texto con el objeto nlp (cuando se procesa
doc = nlp ("""Ahora en la hora del desamor
y sin la levedad irreal que da el deseo
flotan sus pasos y su gestos
Las sonrisas sonánmbulas, asi sin boca,
aquellas palabras necesarias que no fueron posibles
las preguntas que por miedo solo zumbaron como moscas
la poca fe en las ceremonias de la ternura
y sus ojos, frío pedazo de carne azul.
Días perdidos en oficios de la imaginación,
como las largas cartas mentales a la hora de la siesta
o el recuerdo preciso y casi cierto
de encuentros por ahí, que nunca fueron.
Los sueños, siempre los sueños.
             
        
¡Qué sucia es la luz de esta hora,
qué turbia es la memoria de lo poco que queda
y qué mezquino el inminente olvido!""")

// itera sobre los tokens en un documento
for token in doc:
    print(token.text)

// usa el índice del documento para acceder a un token
let token = doc[3]

// imprime el texto del token a través del atributo .text
print(token.text)



