from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
<<<<<<< HEAD
    return "Hello, this is the remix!"
=======
       return "Hello, World!"

if __name__ == "__main__":
       app.run()
>>>>>>> f299ec2518c9d321c790df483efd6d09abad92d4
