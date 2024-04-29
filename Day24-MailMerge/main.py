#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open('./Input/Names/invited_names.txt') as names:
    names_list = [name.strip() for name in names.readlines()]

with open('./Input/Letters/starting_letter.txt') as file:
    lines = file.read()
    for name in names_list:
        striped_name = name.strip()
        new_letter = lines.replace(PLACEHOLDER,striped_name)
        with open(f'./Output/ReadyToSend/letter_to_{striped_name}.txt',mode='w') as createFile:
            createFile.write(new_letter)
    


    

