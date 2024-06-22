# Define the string

def Con_to_text(file,text):


    # Open a file in write mode and write the string

    with open(file, "w", encoding="utf-8") as file:
        for char in text:
            file.write(char)
            if char == ",":
                file.write("\n")
# my_string = "This is a sample text that I want to save as a file."
# name='osr.txt'
# Con_to_text(my_string,name)
