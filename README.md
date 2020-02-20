# 0x00. AirBnB clone - The console

## Description
What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---
#### The following links will take you to the code that implements each of the following objectives of the project.

### [1. Be PEP8 compliant!](./tests/)
* Write beautiful code that passes the PEP8 checks.


### [2. Unittests](./models/base_model.py)
* All your files, classes, functions must be tested with unit tests


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes:


### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()). Now it’s time to re-create an instance with this dictionary representation.


### [5. Store first object](./console.py)
* Recreate a BaseModel from another one by using a dictionary representation:


### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:


### [7. Console 0.1](./models/user.py)
* Update your command interpreter (console.py) to have these commands:


### [8. First User](./models/state.py)
* Write a class User that inherits from BaseModel:


### [9. More classes!](./console.py)
* Write all those classes that inherit from BaseModel:

### How to start and exit the console
* Run console.py as an executable "./console.py"
  * Ex: **$ ./console.py**
* Enter "help" to view command options
  * Ex: **$ help**
* Enter "EOF" or "quit" to exit the console
  * Ex: **$ EOF**
  * Ex: **$ quit**

### Commands in the console:
* **create**: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. 
  * Ex: **$ create BaseModel**
  * Output: **a09349a5-66d8-42b2-bcb3-c6828393abff**
* **show**: Prints the string representation of an instance based on the class name and id. 
  * Ex: **$ show BaseModel a09349a5-66d8-42b2-bcb3-c6828393abff**
  * Output: **[BaseModel] (a09349a5-66d8-42b2-bcb3-c6828393abff) {'created_at': datetime.datetime(2020, 2, 19, 22, 34, 4, 624161), 'id': 'a09349a5-66d8-42b2-bcb3-c6828393abff', 'updated_at': datetime.datetime(2020, 2, 19, 22, 34, 4, 624194)}**
* **destroy**: Deletes an instance based on the class name and id (save the change into the JSON file). 
  * Ex: **$ destroy BaseModel 1234-1234-1234**
* **all**: Prints all string representation of all instances based or not on the class name. 
  * Ex: **$ all BaseModel or $ all**
* **update**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 
  * Ex: **$ update BaseModel 1234-1234-1234 email "airbnb@holbertonschool.com"**
---

## Author
* **Nick Uchida** - [nickuchida](https://github.com/nickuchida)
* **Christine Pang** - [christinepang1](https://github/com/christinepang1)
