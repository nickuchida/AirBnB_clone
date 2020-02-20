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

```
AirBnB_clone$: python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
AirBnB_clone$:
```


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes.
  * Public Instance Attributes: 
    * id
      * created_at
      	* updated_at
	* Public Instance Methods:
	  *	 save
	  	 *	to_dict

### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()). Now it’s time to re-create an instance with this dictionary representation.
  * Public Instance Methods
    * all
      * new
      	* save
	  * reload
	  * Private Class Attributes
	    * __file_path
	      * __objects


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
  * user
    * email
      * password
      	* first_name
	  * last_name
	  * state
	    * name
	    * city
	      * state_id
	      	* name
		* amenity
		  * name
		  * place
		    * city_id
		      * user_id
		      	* name
			  * description
			    * number_rooms
			      * number_bathrooms
			      	* max_guest
				  * price_by_night
				    * latitude 
				      * longitude
				      	* amenity_ids
					* review
					  * place_id
					    * user_id
					      * text

### How to start and exit the console
* Run console.py as an executable "./console.py"
  * Ex: **$ ./console.py**
* Enter "help" to view command options
  * Ex: **$ help**
* Enter "EOF" or "quit" to exit the console
  * Ex: **$ EOF**
  * Ex: **$ quit**
```
AirBnB_clone$: ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
AirBnB_clone$:
```

### Commands in the console:
* **create**: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
  * Ex: **$ create BaseModel**
  * Output: **a09349a5-66d8-42b2-bcb3-c6828393abff**
```
AirBnB_clone$: ./console.py
(hbnb) create BaseModel
a09349a5-66d8-42b2-bcb3-c6828393abff
(hbnb)
AirBnB_clone$:
```

* **show**: Prints the string representation of an instance based on the class name and id.
  * Ex: **$ show BaseModel a09349a5-66d8-42b2-bcb3-c6828393abff**
   * Output: **[BaseModel] (a09349a5-66d8-42b2-bcb3-c6828393abff) {'created_at': datetime.datetime(2020, 2, 19, 22, 34, 4, 624161), 'id': 'a09349a5-66d8-42b2-bcb3-c6828393abff', 'updated_at': datetime.datetime(2020, 2, 19, 22, 34, 4, 624194)}**
```
AirBnB_clone$: ./console.py
(hbnb) create BaseModel
a09349a5-66d8-42b2-bcb3-c6828393abff
(hbnb) show BaseModel a09349a5-66d8-42b2-bcb3-c6828393abff
[BaseModel] (9fcc0de6-c822-4c68-9cf9-9261507dbf41) {'updated_at': datetime.datetime(2020, 2, 19, 17, 39, 0, 254144), 'created_at': datetime.datetime(2020, 2, 19, 17, 39, 0, 254142), 'id': '9fcc0de6-c822-4c68-9cf9-9261507dbf41'}
AirBnB_clone$:
```
* **destroy**: Deletes an instance based on the class name and id (save the change into the JSON file).
  * Ex: **$ destroy BaseModel 1234-1234-1234**
```
AirBnB_clone$: ./console.py
(hbnb) create BaseModel
a09349a5-66d8-42b2-bcb3-c6828393abff
(hbnb) show BaseModel a09349a5-66d8-42b2-bcb3-c6828393abff
[BaseModel] (9fcc0de6-c822-4c68-9cf9-9261507dbf41) {'updated_at': datetime.datetime(2020, 2, 19, 17, 39, 0, 254144), 'created_at': datetime.datetime(2020, 2, 19, 17, 39, 0, 254142), 'id': '9fcc0de6-c822-4c68-9cf9-9261507dbf41'}
(hbnb) destroy BaseModel a09349a5-66d8-42b2-bcb3-c6828393abff
(hbnb) show BaseModel a09349a5-66d8-42b2-bcb3-c6828393abff
** no instance found **
AirBnB_clone$:
```

* **all**: Prints all string representation of all instances based or not on the class name.
  * Ex: **$ all BaseModel or $ all**
 ```
AirBnB_clone$: ./console.py
(hbnb) all
[BaseModel] (d74feb8c-eff4-4e1b-978e-44012fd88190) {'updated_at': datetime.datetime(2020, 2, 19, 17, 22, 31, 984292), 'my_number': 54, 'name': 'Nick', 'created_at': datetime.datetime(2020, 2, 19, 17, 22, 31, 984282), 'id': 'd74feb8c-eff4-4e1b-978e-44012fd88190'}
[BaseModel] (71d39c48-851e-45f9-b590-7f73efd933be) {'updated_at': datetime.datetime(2020, 2, 19, 18, 50, 57, 800896), 'name': 'Oregon', 'created_at': datetime.datetime(2020, 2, 19, 18, 50, 57, 800875), 'id': '71d39c48-851e-45f9-b590-7f73efd933be'}
[BaseModel] (07f924e1-1495-4b1b-be68-4f756355d833) {'updated_at': datetime.datetime(2020, 2, 19, 18, 14, 39, 4626), 'email': 'me@me.com', 'password': '1234', 'last_name': 'Uchida', 'created_at': datetime.datetime(2020, 2, 19, 18, 14, 39, 4622), 'id': '07f924e1-1495-4b1b-be68-4f756355d833', 'first_name': 'Nick'}
    ...
(hbnb) all BaseModel
[BaseModel] (3e6d4e45-b0cb-4bda-9f1f-e8e170770f1e) {'updated_at': datetime.datetime(2020, 2, 19, 18, 40, 13, 632442), 'my_number': 54, 'name': 'Nick', 'created_at': datetime.datetime(2020, 2, 19, 18, 40, 13, 632419), 'id': '3e6d4e45-b0cb-4bda-9f1f-e8e170770f1e'}
[BaseModel] (e2bbce95-f6e2-4b52-933a-8d734667271c) {'updated_at': datetime.datetime(2020, 2, 19, 18, 28, 41, 347956), 'my_number': 54, 'name': 'Nick', 'created_at': datetime.datetime(2020, 2, 19, 18, 28, 41, 347952), 'id': 'e2bbce95-f6e2-4b52-933a-8d734667271c'}
[BaseModel] (e7813b64-c01a-4d99-98b4-bcab7986a7f9) {'updated_at': datetime.datetime(2020, 2, 19, 17, 35, 45, 636680), 'my_number': 54, 'name': 'Nick', 'created_at': datetime.datetime(2020, 2, 19, 17, 35, 45, 636662), 'id': 'e7813b64-c01a-4d99-98b4-bcab7986a7f9'}
...
(hbnb) 
AirBnB_clone$:
```
* **update**: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
  * Ex: **$ update BaseModel 1234-1234-1234 email "airbnb@holbertonschool.com"**
 ```
AirBnB_clone$: ./console.py
(hbnb) update BaseModel 1234-1234-1234 email "airbnb@holbertonschool.com"
(hbnb) 
(hbnb) 
AirBnB_clone$:
```
---

## Author
* **Nick Uchida** - [nickuchida](https://github.com/nickuchida)
* **Christine Pang** - [christinepang1](https://github/com/christinepang1)