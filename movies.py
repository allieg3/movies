movieTitles = ["Braveheart", "Little Mermaid", "The Room", "Fargo", "Contact"]
parentRating = ["R","G","R","R","R"]
imdbRating = ["8.4","7.6","3.4","8.2","7.4"]
bechdelRating = ["2","2","3","3","3"]
genre = ["Drama", "Cartoon", "Drama", "Crime drama", "Science Fiction"]

n = 0

for movie in movieTitles:
	print movieTitles[n] + ", " + parentRating[n] + ", " + imdbRating[n] + ", " + bechdelRating[n] + ", " + genre[n] + "\n"
	n = n + 1
