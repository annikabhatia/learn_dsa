# 🐍 Flask Hello World - Getting Started with Web Development with Python & Flask


Welcome to your very first Flask project! This assignment will help you set up a minimal Python web server using Flask and display a simple message in the browser.

---

## 📚 Objective

- Learn how to create a basic Flask app using Python
- Run a local server on your computer
- Display a “Hello, World!” message on a webpage

---

## 📁 Folder Structure

```

flask\_hello\_world/
│
└── app.py            # Your main Flask application file

````

---

## 🛠️ Setup Instructions

### 1. Create and Open the Project Folder

- Open Visual Studio Code
- Create a new folder called `flask_hello_world`
- Inside this folder, create a new file named `app.py`

### 2. Install Flask

Make sure Flask is installed. In your terminal, type:

```bash
pip install flask
````

If you're using a virtual environment, activate it first.

---

## 🧑‍💻 Your Task

### 1. Write this code in `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

### 2. Run Your Flask App

In the terminal, run:

```bash
python app.py
```

You should see output that says:

```
Running on http://127.0.0.1:5000/
```

---

### 3. View It in Your Browser

* Open your browser
* Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
* You should see:

```
Hello, World!
```

---

## ✅ What to Submit/push/upload to the repo directory

* Your `app.py` file into the repo
* A screenshot of the browser showing the “Hello, World!” message (Update README.md to add the picture)

---

## 🌟 Optional Challenge (Extra Practice)

Add another route, like `/about`, and make it return a new message.

Example:

```python
@app.route('/about')
def about():
    return 'This is a simple Flask project by Annika'
```

Now go to [http://127.0.0.1:5000/about](http://127.0.0.1:5000/about) to test it.

---

## 📘 References – Learn More About Flask

Here are some great beginner-friendly resources:

* 🔗 [Flask Official Documentation (Quickstart)](https://flask.palletsprojects.com/en/latest/quickstart/)
* 📺 [Corey Schafer’s Flask Tutorial on YouTube (Very beginner-friendly)](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
* 📖 [Real Python: Flask by Example](https://realpython.com/flask-by-example-part-1-project-setup/)
* 📘 [Tutorial: Flask Web App with Python (FreeCodeCamp)](https://www.freecodecamp.org/news/how-to-build-a-web-app-using-flask-and-python-3/)


Happy coding! 🎉

---
