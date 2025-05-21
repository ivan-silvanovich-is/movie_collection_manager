# Movie Collection Manager 🎬
A Python package for managing and organizing your personal movie collection with powerful filtering capabilities.

## Features
- 📌 Add and remove movies
- 🎥 Store movie information including title, year, genre, and rating
- 🔍 Filter movies using Django-style lookups (year__lt, rating__gte, etc.)
- 📊 Get detailed movie information with emoji formatting
- 🔄 Iterate over the collection using a custom iterator
- 📂 Store data in memory (no DB)
- 🛠 Fully typed code (type hints)

## References
Check the reference requirements in ```task_description.png```

## Installation and Run
1. Clone the repository:
```commandline
git clone https://github.com/ivan-silvanovich-is/movie_collection_manager.git
cd movie_collection_manager
```
2. Run (requires Python 3.10+):
```commandline
python main.py
```

## Quick Start
```python
from cinema.movie import Movie
from cinema.collection import MovieCollection


# Create a collection
favorites = MovieCollection()

# Add movies
favorites.add_movie(Movie('Inception', 2010, 'Sci-Fi', 8.5))
favorites.add_movie(Movie('The Shawshank Redemption', 1994, 'Drama', 10))

# Remove a movie
favorites.remove_movie('Inception')

# Filter movies
for movie in favorites.filter(year__lt=2000, rating__gte=9.0):
    print(movie.details())
```

## API Reference
### Movie Class
```
Movie(title: str, year: int, genre: str, rating: float)
```
- ```title```: Movie title
- ```year```: Release year
- ```genre```: Movie genre
- ```rating```: Rating (0.0-10.0 scale)

#### Methods:

- ```details()```: Returns formatted string with movie details
- ```__repr__()```: Returns movie title

### MovieCollection Class
#### Methods:

- ```add_movie(movie: Movie)```: Adds a movie to collection
- ```remove_movie(key: Movie | str)```: Removes a movie by title or Movie object
- ```details(key: Movie | str)```: Returns detailed info about specific movie
- ```filter(**kwargs)```: Filters movies based on criteria (see below)

#### Filter Operators:

- ```field__lt```: Less than
- ```field__lte```: Less than or equal
- ```field__gt```: Greater than
- ```field__gte```: Greater than or equal
- ```field__eq```: Equal (default)
- ```field__ne```: Not equal
- ```field__contains```: Contains substring (for strings)

## Examples
```python
# Get all Sci-Fi movies
sci_fi = favorites.filter(genre='Sci-Fi')

# Get movies released before 2010 with rating >= 9.0
classics = favorites.filter(year__lt=2010, rating__gte=9.0)

# Get movie details
print(favorites.details('Inception'))
# Output: "Inception (📅2010, 🎥Sci-Fi, ⭐8.5)"
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
MIT
