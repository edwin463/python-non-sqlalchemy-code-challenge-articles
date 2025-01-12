class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title is immutable.")  # Ensure no changes to title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable.")  # Ensure no changes to name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None  # Match test expectation for no articles
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._validate_string(name, 2, 16)
        self._validate_string(category, 1, float('inf'))
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    def _validate_string(self, value, min_len, max_len):
        if not isinstance(value, str) or not (min_len <= len(value) <= max_len):
            return False  # Ignore invalid changes instead of raising an exception
        return True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if self._validate_string(value, 2, 16):
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if self._validate_string(value, 1, float('inf')):
            self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None  # Match test expectation for no articles
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
