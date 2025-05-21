import operator
from typing import Iterator, Optional, Iterable

from .movie import Movie


class MovieCollection:
    def __init__(self, collection: Optional[Iterable[Movie]] = None) -> None:
        """Initialize a MovieCollection with optional initial movies.

        Args:
            collection: An optional iterable object of Movie objects to initialize the collection.
                       If provided, movies will be stored with their titles as keys.
                       If None (default), creates an empty collection.
        """
        if collection:
            self._dict = {movie.title: movie for movie in collection}
        else:
            self._dict = dict()

    def __iter__(self) -> Iterator:
        """Return an iterator over all movies in the collection.
        Allows the collection to be iterated directly (e.g., 'for movie in collection').
        """
        return iter(self._dict.values())

    def __repr__(self) -> str:
        """Return the official string representation of the movie collection.
        Shows the internal dictionary structure for debugging/showing purposes.
        """
        return repr(self._dict)

    def add_movie(self, movie: Movie) -> None:
        """Add a movie to the collection.

        Args:
            movie (Movie): The movie object to add to the collection.

        Note:
            Uses the movie's title as the dictionary key.
            Will overwrite existing movie with same title.
        """
        self._dict[movie.title] = movie

    def remove_movie(self, key: Movie | str) -> Movie:
        """Remove and return a movie from the collection.

        Args:
            key (Movie | str): Either a Movie object or string title of movie to remove.

        Returns:
            The removed Movie object.

        Raises:
            KeyError: If the movie doesn't exist in the collection.
        """
        return self._dict.pop(key.title if isinstance(key, Movie) else key)

    def details(self, key: Movie | str) -> str:
        """Get detailed information about a specific movie.

        Args:
            key (Movie | str): Either a Movie object or string title of movie.

        Returns:
            The detailed string representation of the movie.

        Raises:
            KeyError: If the movie doesn't exist in the collection.
        """
        return key.details() if isinstance(key, Movie) else self._dict[key].details()

    def filter(self, **kwargs):
        """Filter movies based on specified criteria.

        Supports Django-style field lookups with double-underscore syntax:
        - field__operator=value
        - Available operators: lt, lte, gt, gte, eq, ne, contains

        Examples:
            filter(year__lt=2010) - Movies released before 2010
            filter(rating__gte=8.5) - Movies with rating >= 8.5
            filter(genre='Action') - Movies in Action genre

        Returns:
            List of Movie objects matching all criteria.

        Raises:
            ValueError: If invalid operator is specified.
            AttributeError: If invalid movie field is specified.
        """
        result = self._dict.values()

        for key, value in kwargs.items():
            field, op = key.split('__') if '__' in key else (key, 'eq')

            op_func = {
                'lt': operator.lt,
                'lte': operator.le,
                'gt': operator.gt,
                'gte': operator.ge,
                'eq': operator.eq,
                'ne': operator.ne,
                'contains': operator.contains,
            }.get(op)

            if not op_func:
                raise ValueError(f"Unknown operator '{op}'")

            result = [movie for movie in result if op_func(getattr(movie, field), value)]

        return MovieCollection(result)
