user_text=input("Ingresa un texto: ".lower())
phirst_letter=input("Ingresa 1 lestras a tu elección: ")
secund_letter=input("Ingresa otra letra de su eleccion: ")
letter_3=input("Ingresa otra letra de tu eleción: ")
phirst_letter=phirst_letter.lower()
secund_letter=secund_letter.lower()
letter_3=letter_3.lower()
user_text=user_text.lower()
text_list=[phirst_letter,secund_letter,letter_3]

print("\n")
print("REPETICIÓN DE LETRAS")
#1.- Analisis cuantas veces aparece cada letra
count_letter_1=user_text.count(phirst_letter)
count_letter_2=user_text.count(secund_letter)
count_letter_3=user_text.count(letter_3)
print(f"tu letra '{phirst_letter}' se repite {count_letter_1} veces")
print(f"tu letra '{secund_letter}' se repite {count_letter_2} veces")
print(f"tu letra '{letter_3}' se repite {count_letter_3} veces")

print("\n")
print("NUMERO DE PALABRAS EN EL TEXTO")
#2- revisar el numero de palabras en un texto
number_words=user_text.split()
count_number_words=len(number_words)
print(f"Tu texto {user_text} tiene un total de {count_number_words} palabras")

print("\n")
print("PRIMERA Y ULTIMA LETRA DEL TEXTO")
#3.-Informar cual es la primera letra del texto y cual es la ultima
initial_letter=user_text[0]
final_letter=user_text[-1]
print(f"la primera letra del texto es {initial_letter}")
print(f"La ultima letra de tu texto es {final_letter}")

print("\n")
print("TEXTO INVERTIDO")
#4.-Texto invertida
number_words.reverse()
inverted_text=" ".join(number_words)
print(f"Tu texto al reves se vería así: '{inverted_text}'")
print("\n")
print("Buscando la palabra Python")
#La palabra Python se encuentra en el texto
word_validation="python"in user_text
data={True:"si",False:"no"}
answer=data[word_validation]
print(f"Su texto {answer} tiene la palabra 'Python'")