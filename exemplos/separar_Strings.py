texto = "John Lennon,john@example.com,Liverpool,England,1940,1980"
(nome, email, *__) = texto.split(",")
print (nome, email, *__)
