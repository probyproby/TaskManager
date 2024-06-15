from app import app, db
from app import Todo

# Set up app context
app.app_context().push()

# Create all tables
db.create_all()

# Optionally, add initial data
new_task = Todo(content='Example task')
db.session.add(new_task)
db.session.commit()

print("Database tables created and initial data added.")
