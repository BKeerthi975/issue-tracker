from flask import Flask, render_template, request, redirect, url_for
from database import get_db, init_db

app = Flask(__name__)

# Home page - show all tickets
@app.route('/')
def index():
    conn = get_db()
    tickets = conn.execute('SELECT * FROM tickets ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', tickets=tickets)

# Create ticket
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        assigned_to = request.form['assigned_to']
        conn = get_db()
        conn.execute('INSERT INTO tickets (title, description, priority, assigned_to) VALUES (?, ?, ?, ?)',
                     (title, description, priority, assigned_to))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

# Update ticket status
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db()
    ticket = conn.execute('SELECT * FROM tickets WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        status = request.form['status']
        conn.execute('UPDATE tickets SET status = ? WHERE id = ?', (status, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('update.html', ticket=ticket)

# Delete ticket
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    conn.execute('DELETE FROM tickets WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Dashboard
@app.route('/dashboard')
def dashboard():
    conn = get_db()
    tickets = conn.execute('SELECT * FROM tickets').fetchall()
    open_count = conn.execute("SELECT COUNT(*) FROM tickets WHERE status='Open'").fetchone()[0]
    inprogress_count = conn.execute("SELECT COUNT(*) FROM tickets WHERE status='In Progress'").fetchone()[0]
    resolved_count = conn.execute("SELECT COUNT(*) FROM tickets WHERE status='Resolved'").fetchone()[0]
    conn.close()
    return render_template('dashboard.html', tickets=tickets,
                           open_count=open_count,
                           inprogress_count=inprogress_count,
                           resolved_count=resolved_count)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)