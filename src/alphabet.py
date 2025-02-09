import os

class Alphabet:

    #method returns a list of dictionaries in Alphabet Dictionaries directory
    def get_yaml_files(directory):
        yaml_files = []
        for filename in os.listdir(directory):
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                yaml_files.append(os.path.splitext(filename)[0])
        return yaml_files
            
    

    def convert(name: str, dictionary: dict):
       
        import re
        name = name.strip()
        name = name.replace("\n", " ")
        name = re.sub(' +',' ',name)
        name = name.lower()
        output=""
        for letter in name:
            if (dictionary.get(letter)==None)&(letter != " "):
                raise TypeError("Enter only alpha-numeric english characters, please!")
            
            else:
                if (letter == " "):
                    output = output + "space\n"
                    
                else:
                    output = output + dictionary.get(letter) + "\n"

        return output
    
