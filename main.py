from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

quotes = [
    {"id": 1, "author": "Albert Einstein", "text": "Logik bringt dich von A nach B. Fantasie bringt dich überall hin."},
    {"id": 2, "author": "Isaac Newton", "text": "Wenn ich weiter sehen konnte, lag das daran, dass ich auf den Schultern von Riesen stand."},
    {"id": 3, "author": "Marie Curie", "text": "Nichts im Leben muss gefürchtet werden, es muss nur verstanden werden. Jetzt ist es an der Zeit, mehr zu verstehen, damit wir weniger Angst haben."},
    {"id": 4, "author": "Charles Darwin", "text": "Es ist nicht der Stärkste der Arten, der überlebt, noch der Intelligenteste, sondern derjenige, der am empfänglichsten für Veränderungen ist."},
    {"id": 5, "author": "Nikola Tesla", "text": "Die Zukunft gehört denen, die an die Schönheit ihrer Träume glauben."},
    {"id": 6, "author": "Leonardo da Vinci", "text": "Es ist einfacher, starke Kinder zu erziehen, als gebrochene Männer zu reparieren."},
    {"id": 7, "author": "Thomas Edison", "text": "Ich habe nicht versagt. Ich habe nur 10.000 Wege gefunden, die nicht funktionieren."},
    {"id": 8, "author": "Galileo Galilei", "text": "Wir können nicht leugnen, dass die Natur uns mit fünf Sinnen ausgestattet hat; aber sie hat uns nicht damit ausgestattet, dass wir die Wahrheit erkennen können."},
    {"id": 9, "author": "Stephen Hawking", "text": "Intelligenz ist die Fähigkeit, sich dem Wandel anzupassen."},
    {"id": 10, "author": "Aristoteles", "text": "Wir können den Wind nicht ändern, aber die Segel anders setzen."}
]

@app.route('/')
def index():
    return render_template('index_quotes.html', quotes=quotes)

@app.route('/add_quote', methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        author = request.form['author']
        text = request.form['text']
        new_quote = {"id": len(quotes) + 1, "author": author, "text": text}
        quotes.append(new_quote)
        return redirect(url_for('index'))
    return render_template('add_quote.html')

@app.route('/edit_quote/<int:quote_id>', methods=['GET', 'POST'])
def edit_quote(quote_id):
    quote = next((q for q in quotes if q['id'] == quote_id), None)
    if quote is None:
        return redirect(url_for('index'))
    if request.method == 'POST':
        quote['author'] = request.form['author']
        quote['text'] = request.form['text']
        return redirect(url_for('index'))
    return render_template('edit_quote.html', quote=quote)

@app.route('/delete_quote/<int:quote_id>')
def delete_quote(quote_id):
    global quotes
    quotes = [q for q in quotes if q['id'] != quote_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
