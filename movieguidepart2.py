with open("movies.txt", "w") as file:
    file.write("Titanic.\nDeep Blue Sea.\nInglorious Bastards.")


def populate_list(file_name):
    movie_list = []
    with open(file_name, "r") as file:
        for line in file:
            movie_list.append(line.strip())
    return movie_list


def display_menu():
    print("\nMovies")
    print("list --> Displays all movies")
    print("add --> Add a movie to the list")
    print("delete --> deletes a movie from the list")
    print("exit --> Closes the application")


def display_titles(movie_list):
    print("\nMovies:")
    for idx, title in enumerate(movie_list, start=1):
        print(f"{idx}. {title}")


def add_title(movie_list, title, file_name):
    movie_list.append(title)
    with open(file_name, "a") as file:
        file.write(title + "\n")
        print(f"\n{title} has been added to your list")


def delete_title(movie_list, index, file_name):
    if 1 <= index <= len(movie_list):
        delete_title = movie_list.pop(index - 1)
        with open(file_name, "w") as file:
            file.write("\n".join(movie_list))
        print(f"\n {delete_title} has been deleted from your movies")
    else:
        print(f"\nInvalid movie number")


def main():
    movie_file = "movies.txt"
    movie_list = populate_list(movie_file)

    while True:
        display_menu()
        choice = input("Enter your choice:  ")

        if choice == "list":
            display_titles(movie_list)
        elif choice == "add":
            new_title = input("Enter the new movie title: ")
            add_title(movie_list, new_title, movie_file)
        elif choice == "delete":
            display_titles(movie_list)
            index = int(input("Enter the number of the movie title you would to delete: "))
            delete_title(movie_list, index, movie_file)
            display_titles(movie_list)
        elif choice == "exit":
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
