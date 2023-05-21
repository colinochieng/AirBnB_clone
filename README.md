# Airbnb Clone

This project is a clone of the popular accommodation booking platform Airbnb.

## Command Interpreter

The command interpreter is a command-line interface that allows users to interact with the Airbnb clone. It is used to manage users, places, and bookings.

### How to Start It

To start the command interpreter, navigate to the root directory of the project and run the following command:

```
python3 console.py
```

### How to Use It

The command interpreter supports the following commands:

- `create`: creates a new object (user, place, or booking)
- `show`: displays information about an object
- `destroy`: deletes an object
- `update`: updates the attributes of an object
- `all`: displays all objects of a given class
- `count`: displays the number of objects of a given class

To use the command interpreter, simply type in the desired command followed by the necessary arguments. For example:

```
(hbnb) create User
52b441e7-fd8a-4010-8e83-1c2477cf334e
(hbnb) show User 52b441e7-fd8a-4010-8e83-1c2477cf334e
[User] (52b441e7-fd8a-4010-8e83-1c2477cf334e) {'id': '52b441e7-fd8a-4010-8e83-1c2477cf334e', 'created_at': datetime.datetime(2023, 5, 9, 14, 25, 59, 219786), 'updated_at': datetime.datetime(2023, 5, 9, 14, 25, 59, 219791)}
(hbnb) update User 52b441e7-fd8a-4010-8e83-1c2477cf334e first_name John
(hbnb) show User 52b441e7-fd8a-4010-8e83-1c2477cf334e
[User] (52b441e7-fd8a-4010-8e83-1c2477cf334e) {'id': '52b441e7-fd8a-4010-8e83-1c2477cf334e', 'first_name': 'John', 'created_at': datetime.datetime(2023, 5, 9, 14, 25, 59, 219786), 'updated_at': datetime.datetime(2023, 5, 9, 14, 27, 12, 893056)}
```

### Examples

To create a new user:

```
(hbnb) create User
52b441e7-fd8a-4010-8e83-1c2477cf334e
```

To show information about the user:

```
(hbnb) show User 52b441e7-fd8a-4010-8e83-1c2477cf334e
[User] (52b441e7-fd8a-4010-8e83-1c2477cf334e) {'id': '52b441e7-fd8a-4010-8e83-1c2477cf334e', 'created_at': datetime.datetime(2023, 5, 9, 14, 25, 59, 219786), 'updated_at': datetime.datetime(2023, 5, 9, 14, 25, 59, 219791)}
```

To update the first name of the user:

```
(hbnb) update User 52b441e7-fd8a-4010-8e83-1c2477cf334e first_name John
```

To show the updated information about the user:

```
(hbnb) show User 52b441e7-fd8a-4010-8e83-1c2477cf334e
[User] (52b441e7-fd8a-4010-8e83-1c2477cf334e) {'id': '52b441e7-fd8a-4010-8e83-1c2477cf334e', 'first_name': 'John', 'created_at': datetime.datetime(2023, 5, 9, 14, 25, 59, 219786), 'updated_at': datetime.datetime(2023, 5, 9, 14, 27, 12, 893056)}
```
