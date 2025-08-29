current_movies = {'The Batman': '2022-03-04', 'Avatar 2': '2022-12-16', 'Black Panther: Wakanda Forever': '2022-11-11'}
print("Current movies and their release dates:")
for key in current_movies:
    print(key)
movie = input("Enter the movie you want to see: ")

showtime = current_movies.get(movie)
if showtime == None:
    print("Movie not found")
else:
    print("The movie", movie, "is released on", showtime)