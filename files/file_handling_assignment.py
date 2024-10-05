def file_operations():
    try:
        # File Creation and Writing
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is line 2.\n")
            file.write("12345 is a number.\n")
        print("File 'my_file.txt' created and text written successfully.")

        # File Reading and Display
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)

        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("Appending more content here.\n")
            file.write("42 is another number.\n")
        print("\nAdditional lines appended to 'my_file.txt'.")

        # Display updated contents
        with open("my_file.txt", "r") as file:
            updated_content = file.read()
            print("\nUpdated contents of 'my_file.txt':")
            print(updated_content)

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile operations complete.")

# Directly calling the function at the end of the script
file_operations()
