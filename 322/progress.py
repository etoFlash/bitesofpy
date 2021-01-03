from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    day_of_year = day_of_year or int(datetime.now().strftime('%j'))

    return books_read / day_of_year * 365 >= books_goal
