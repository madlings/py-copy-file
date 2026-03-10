def copy_file(command):
    # Split the command into components
    parts = command.split()
    # Validate that there are exactly 3 elements and starts with "cp"
    if len(parts) != 3 or parts[0] != "cp":
        return
    source_name = parts[1]
    destination_name = parts[2]
    # Do nothing if the source and destination names are the same
    if source_name == destination_name:
        return
    try:
        # Open both files: source for reading and destination for writing
        with open(source_name, "r") as file_in, open(destination_name, "w") as file_out:
            # Copy the entire content
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: The file '{source_name}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
