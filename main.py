import requests
import sqlite3

API_KEY = "261c1e2701a652fe4cb9e22b5668ab43"
BASE_URL = "https://api.themoviedb.org/3/search/movie"
DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS favorites(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       release_date TEXT,
                       rating REAL
                   )
                """)
    conn.commit()
    conn.close()
    
def add_to_favorites(title,release_date,rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
                   INSERT INTO favorites (title,release_date,rating)
                   VALUES(?,?,?)
                   """, (title,release_date,rating))
    
    conn.commit()
    conn.close()

def view_favorites():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT title, release_date, rating FROM favorites")
    rows = cursor.fetchall()
    
    conn.close()
    
    if not rows:
        print("\nNo favorite movies saved yet.")
        return
    
    print("\n=== Your Favorite Movies ===")
    for i, movie in enumerate(rows, start=1):
        print(f"{i}. {movie[0]} ({movie[1]}) - Rating: {movie[2]})")
    

def show_menu():
    print("\n=== Movie Recommendation CLI ===")
    print("1. Search Movies")
    print("2. View Favorite Movies")
    print("3. Exit")
    
def search_movie():
    title = input("Enter movie title to search: ")
    
    params = {
        "api_key": API_KEY,
        "query": title,
        "language": "en-US",
        "page": 1,
        "include_adult": False
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code!=200:
        print("Error fetching data from TMDb API")
        return
    
    data = response.json()
    results = data.get("results",[])
    
    if not results:
        print(f"No results found for '{title}'.")
        return
    
    for i, movie in enumerate(results[:5], start=1):
        movie_title = movie.get("title","N/A")
        release_date = movie.get("release_date","N/A")
        rating = movie.get("vote_average","N/A")
        print(f"{i}. {movie_title} ({release_date}) - Rating: {rating}")
        
    choice = input("\nEnter a number (1-5) to save to favorites, or press Enter to skip: ")
    
    if choice.isdigit():
        choice = int(choice)
        if 1<=choice <=5:
            movie = results[choice-1]
            add_to_favorites(
                movie.get("title","N/A"),
                movie.get("release_date","N/A"),
                movie.get("vote_average",0)
            )
            print("Movie added to favorites!")
        else:
            print("Invalid selection.")
    
def main():
    init_db()
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            search_movie()
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()