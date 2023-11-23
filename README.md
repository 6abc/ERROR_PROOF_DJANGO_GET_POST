<br/>
<p align="center">
  <a href="https://github.com/6abc/ERROR_PROOF_DJANGO_GET_POST">
    <img src="https://avatars.githubusercontent.com/u/97246854?v=4" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ERROR_PROOF_DJANGO_GET_POST</h3>

  <p align="center">
    Let’s look at what XSS is and how XSS attacks work. We’ll then go through what security Django xss provides and how we can improve it.
    <br/>
    <br/>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/6abc/ERROR_PROOF_DJANGO_GET_POST/total) ![Contributors](https://img.shields.io/github/contributors/6abc/ERROR_PROOF_DJANGO_GET_POST?color=dark-green) ![Issues](https://img.shields.io/github/issues/6abc/ERROR_PROOF_DJANGO_GET_POST) ![License](https://img.shields.io/github/license/6abc/ERROR_PROOF_DJANGO_GET_POST) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Usage](#Features)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://raw.githubusercontent.com/6abc/ERROR_PROOF_DJANGO_GET_POST/main/Django%20XSS.png)

## Built With

Django frameworks with Python Code.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

* Python (3.6 or higher)
* Django (latest version)

### Installation

1. Clone the repo

```sh
git clone https://github.com/6abc/ERROR_PROOF_DJANGO_GET_POST.git
cd ERROR_PROOF_DJANGO_GET_POST
```

2.1 Create a virtual environment [Unix](optional but recommended):

```sh
python -m venv venv
source venv/bin/activate
```

2.2 Create a virtual environment [Windows](optional but recommended):

```sh
python -m venv venv
.\venv\Scripts\activate
```

3. Install project dependencies:
```sh
pip install -r requirements.txt
```

4. Apply migrations:
```sh
python manage.py migrate
```

## Usage

1. Start the development server:
```sh
python manage.py runserver
```

2. Open a web browser and navigate to http://127.0.0.1:8000/ to access the home page.

3. Enter a message and click the "Submit" button to see how GET and POST requests are handled.

## Features
* Demonstrates handling GET and POST requests in Django.
* Utilizes Django Forms for form handling and validation.
* Includes error handling and displays validation errors to the user.

## License

Distributed under the MIT License. See [LICENSE](https://github.com/6abc/ERROR_PROOF_DJANGO_GET_POST/blob/main/LICENSE) for more information.

## Authors

* **Ashish Thakur** - *Senior Command Center Analyst* - [Ashish Thakur](https://github.com/6abc)

## Acknowledgements

* [Inspired by the Django documentation and tutorials](https://docs.djangoproject.com/en/4.2/)
* [Inspired by the Django XSS: Examples and Prevention](https://www.stackhawk.com/blog/django-xss-examples-prevention/)
* [Inspired by ReadME-Generator](https://readme.shaankhan.dev/)
