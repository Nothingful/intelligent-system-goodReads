from pandas import read_csv
from models import Book
from gui import *

from decision_tree_model import predict_totalratings

dataframe = read_csv("GoodReadsData.csv", delimiter=",")

# Remove all rows that contain NULL values
dataframe.dropna(inplace=True)

books = []

for index, row in dataframe.iterrows():
    author = row["author"]
    book_format = row["bookformat"]
    description = row["desc"]
    genres = row["genre"].split(",")
    isbn = row["isbn"]
    link = row["link"]
    pages = row["pages"]
    rating = row["rating"]
    reviews = row["reviews"]
    title = row["title"]
    total_ratings = row["totalratings"]

    new_book = Book(
        author,
        book_format,
        description,
        genres,
        isbn,
        link,
        pages,
        rating,
        reviews,
        title,
        total_ratings,
    )

    books.append(new_book)

if __name__ == "__main__":
    total_rating = predict_totalratings() 

    #above_total_rating = dataframe[(dataframe['totalratings'] > total_rating) & (dataframe['reviews'] == 1214)]                      

    gui = set_gui(
        books, 
        dataframe
    )
    gui.geometry('550x400')
    gui.configure(bg='#7878ab')
    gui.mainloop()
    


