song_library = {}


def prompt():
    # #Delete this
    # song_library["brady"] = "brady"
    # song_library["anna"] = "anna"

    while True:
        try:
            user_input = input(
                f"Please select one of the options below: \n 1) Add a song. \n 2) Retrieve song details \n "
                "3) Update song details \n 4) Delete a song \n 5) Display all songs \n 9) exit \n").strip()
        except ValueError:
            print("Please enter a number.")
            continue

        if user_input == '1':
            add_song_to_library()
        elif user_input == '2':
            retrieve_song()
        elif user_input == '3':
            update()
        elif user_input == '4':
            delete()
        elif user_input == '5':
            display()
        elif user_input == '9':
            exit()
        else:
            print("Please enter the number of an option.")


def add_song_to_library():
    while True:
        try:
            title, artist = input("Please enter a song title and artist separated by a comma to add: ").lower().split(',')
            song_library[title] = artist
            user_input = input("Song added enter 1 if you would like to add another song or press enter to return to "
                               "the main menu.").strip()
            if user_input == '1':
                continue
            prompt()
        except ValueError:
            user_input = input("You did not format your input correctly please make sure you comma separate the song "
                               "title and the artist's name. Enter 9 if you would like to return to the main menu.")
            if user_input == '9':
                prompt()
            continue
        except UnboundLocalError:
            user_input = input("You did not format your input correctly please make sure you comma separate the song "
                               "title and the artist's name. Enter 9 if you would like to return to the main menu.")
            if user_input == '9':
                prompt()
            continue


def retrieve_song():
    while True:
        title = input("Please enter a song title you would like retrieve: ").lower()
        artist = song_library.get(title, None)
        if artist is None:
            print("The song title you entered does not exist in the collection yet.")
        else:
            print("That song is written by: {}".format(artist))
        user_input = input("Enter 1 if you would like to retrieve another song or press enter to return to the "
                           "main menu.").strip()
        if user_input == '1':
            continue
        prompt()


def update():
    while True:
        title = input("Please enter the song title whose artists you would like to update: ").lower()
        artist = song_library.get(title, None)
        if artist is None:
            user_input = input("The song title you entered does not exist in the collection yet. Enter 9 if you would "
                               "like to return to the main menu or press enter to try again")
            if user_input == '9':
                prompt()
            continue
        else:
            updated_artist = input("Please enter the new artist you would like to update this song with: ").lower()
            song_library.update({title: updated_artist})
            print("Updated artist successfully from {} to {}.".format(artist, updated_artist))
        user_input = input("Enter 1 if you would like to update another song or press enter to return to the "
                           "main menu.").strip()
        if user_input == '1':
            continue
        prompt()


def delete():
    while True:
        title = input("Please enter the song title whose artists you would like to delete: ").lower()
        artist = song_library.get(title, None)
        if artist is None:
            user_input = input("The song title you entered does not exist in the collection yet. Enter 9 if you would "
                               "like to return to the main menu or press enter to try again")

            if user_input == '9':
                prompt()
            continue
        else:
            song_library.pop(title)
            print("{} deleted successfully from collection".format(title))
        user_input = input("Enter 1 if you would like to delete another song or press enter to return to the "
                           "main menu.").strip()
        if user_input == '1':
            continue
        prompt()


def display():
    for k, v in song_library.items():
        print(f'Title: {k} \t Artist: {v}')


prompt()
