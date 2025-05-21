class Movie:
    def __init__(self, title: str, year: int, genre: str, rating: float) -> None:
        """
        Initialize a Movie instance with title, year, genre, and rating.

        Args:
            title (str): The title of the movie
            year (int): The release year of the movie
            genre (str): The genre of the movie
            rating (float): The rating of the movie (typically 0.0-10.0)
        """
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

    def __repr__(self) -> str:
        """
        Official string representation of the Movie object.
        Used for debugging, development and presenting purposes.

        Returns:
            str: The movie title as the representation
        """
        return self.title

    def details(self) -> str:
        """
        Generate a detailed, formatted string representation of the movie.
        Includes emoji icons for better readability.

        Returns:
            str: Formatted string with title, year, genre and rating
            Example: "Inception (📅2010, 🎥Sci-Fi, ⭐8.8)"
        """
        return f'{self.title} (📅{self.year}, 🎥{self.genre}, ⭐{self.rating}).'
