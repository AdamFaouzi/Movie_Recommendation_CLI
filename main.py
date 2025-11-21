def show_menu():
    print("\n=== Movie Recommendation CLI ===")
    print("1. Search Movies")
    print("2. View Favorite Movies")
    print("3. Exit")
    
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("Feature coming soon: Search Movies")
        elif choice == "2":
            print("Feature coming soon: View Favorite Movies")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()