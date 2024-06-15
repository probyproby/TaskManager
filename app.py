
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handle.db'
db = SQLAlchemy(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your task'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task_to_update)

if __name__ == "__main__":
    app.run(debug=True) 


'''
    
from flask import Flask, send_file, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)  # Corrected special variable __name_
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///handle.db'
db = SQLAlchemy(app) 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):  # Corrected special method __repr_
        return '<Task %r>' % self.id

@app.route('/')
def index():
    # Fetch all todos from the database and pass to the template
    todos = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    content = request.form['content']
    new_todo = Todo(content=content)
    
    try:
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue adding your task'

@app.route('/delete/<int:id>')
def delete_todo(id):
    todo_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(todo_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was a problem deleting that task'

if __name__ == "_main_":
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)'''