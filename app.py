from flask import Flask, render_template, request
from tinydb import TinyDB

db = TinyDB('db.json')
app = Flask(__name__)

@app.route('/todo', methods=['GET','POST'])
def hello():
    if request.method == "POST":
        todo = request.form.get('todo')
        print("fljsdfjdfjlfdjlnfdslkjsdfnlsflnfksdsfnklfdsklndfsnkl")
        db.insert({"todo": todo})
    allTodos = db.all()
    return render_template('index.html', todos = allTodos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
