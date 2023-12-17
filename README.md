# Welcome

## This is my virtual assistant

I'm using this repository to learn about speech recognization, text to speech and maybe some openAI integration.

In this project I'll also use Object Oriented Programming concepts.

There are 3 main files
- main.py
- config.py
- classes/mic_recognizer.py

# main.py

This file is instanciating the mic recognizer and calling the listen method from mic and then calling the execute method from the class that was called in the voice command.
When a user speaks the script looks on LISTNER constant from **"config.py"** for a match command, when a command matches, the execute method from the respective command class is executed.

# config.py

This file contains the **LISTNER** constant that is a list of dictionaries where each property is a command and its value is a class name.
This file also imports all classes that is used in the LISTNER constant.

# classes/mic_recognizer.py

This file is where is implemented the speech recognization in the class **MicRecognizer** that have all the main methods to work with voice recognization.

# How to use

- Create a class that extends MicRecognizer 
- Create a method called **execute(self)**
- Add an item (dict) in the **LISTNER** constant in the config.py like ``` {"command": ClassName} ``` **don't forget to import this Class**

# That's all Folks
