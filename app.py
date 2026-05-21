from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():

    task = request.form.get('task')
    priority = request.form.get('priority')

    if task:

        tasks.append({
            'task': task,
            'priority': priority
        })

    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):

    if 0 <= index < len(tasks):
        tasks.pop(index)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)