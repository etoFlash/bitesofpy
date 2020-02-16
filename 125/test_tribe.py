import pytest

from tribe import get_top_books, load_page


@pytest.fixture(scope='module')
def content():
    """Load content once for all test"""
    return load_page()


def test_return(content):
    books = get_top_books(content=content)
    assert len(books) == 15
    assert type(books) == list
    assert all(type(book) == tuple for book in books)


@pytest.mark.parametrize("title, count", [
  ('Man’s Search For Meaning', 6),
  ('Tao Te Ching', 5),
  (('The 4-Hour Workweek: Escape the 9-5, '
    'Live Anywhere and Join the New Rich'), 4),
  ('The Fountainhead', 4),
  ('Sapiens: A Brief History of Humankind', 4),
  ('The Better Angels of our Nature: Why Violence Has Declined', 3),
  ('The Beginning of Infinity: Explanations That Transform the World', 3),
  (('The War of Art: Break Through the Blocks and Win Your '
    'Inner Creative Battles'), 3),
  ('The Hero with a Thousand Faces ', 3),
  ('Poor Charlie’s Almanack', 3),
  ('The Chronicles of Narnia', 3),
  ('The Selfish Gene', 3),
  ('Tools of Titans', 3),
  ('Song of Solomon', 3),
  ('The Alchemist', 3),
])
def test_counts(content, title, count):
    books = get_top_books(content=content)
    assert (title, count) in books