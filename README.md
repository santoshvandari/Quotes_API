# Quotes API
## Introduction
This is an API for performing the CRUD Operation on the Database. It is developed using Python (FastAPI Framework) as well as MOngoDB database.


## Features
The URL Shortner has the following features.
 - User can perform `GET`,`POST`,`PUT` and `DELETE` Operation.

## Usages
You System must have the following things to use this Blog App.
 - Installation of `python` and  `pip`

    Python is available for every platform. Download it according to you os. You can download it from [Here.](https://www.python.org/downloads/)


Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
    git clone https://github.com/santoshvandari/Quotes_API
    cd Quotes_API
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and MAC User
     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Update the Connection String of the MongoDB From [DB/db.py](/DB/db.py)

 - Run the Server
```bash
    uvicorn app:app --reload 
```
 - Open the url in Browser
 ```bash
    For Get Request: http://127.0.0.1:8000/  
    For POST Request: http://127.0.0.1:8000/add/
    For PUT Request: http://127.0.0.1:8000/update/
    For DELETE Request: http://127.0.0.1:8000/delete/
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this Blog app, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this app.

## License
This project is licensed under the [License](LICENSE).