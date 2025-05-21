from cinema.movie import Movie
from cinema.collection import MovieCollection


if __name__ == '__main__':
    # I wanna create my favorites movies collection
    favorites = MovieCollection()
    favorites.add_movie(Movie('Inception', 2010, 'Sci-Fi', 8.5))
    favorites.add_movie(Movie('Annihilation', 2018, 'Sci-Fi', 9.5))
    favorites.add_movie(Movie('The Shawshank Redemption', 1994, 'Drama', 10))
    favorites.add_movie(Movie('The Dark Knight', 2008, 'Action', 9.0))
    favorites.add_movie(Movie('Ideocracy', 2006, 'Comedy', 6.5))

    # After second thought, I don't really like Ideocracy...
    favorites.remove_movie('Ideocracy')

    # Let's see my collection now
    print('🗂️ My collection:')
    for movie in favorites:
        print(movie.details())

    # Okay, how many Sci-Fi movies are in my collection?
    print('\n🛸 All my Sci-Fi:')
    for i, movie in enumerate(favorites.filter(genre='Sci-Fi')):
        print(f'{i+1}. {movie}')

    # At the second thought, I don't really remember this Annihilation movie
    print("\n🤔 What's Annihilation?", favorites.details('Annihilation'), sep='\n', end='\n\n')

    # Do I really like old movies?
    for i, movie in enumerate(favorites.filter(year__lt=2010, rating__gte=9.0)):
        print(f'{i+1}. {movie}')
