from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_news(number:int):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    # Funcion sensible
    cursor.execute(f"SELECT titulo, cuerpo FROM noticias WHERE id='{number}'")
    news = cursor.fetchone()
    conn.close()
    return news

@app.route('/api/vulnerable', methods=['GET', 'POST'])
def vulnerable():
    if request.method == 'POST':
        # Lo que llega lo mando (variable manchada)
        entered_number = request.form.get('number')
        news = get_news(entered_number)
        if news:
            return render_template('noticia.html', title=news[0], content=news[1])
        else:
            return news, 404
    return render_template('pagina.html')

# Un pedido 'UNION+SELECT+username,+password+FROM+users-- devuelve todo
# Sabiendo el username, un WHERE te da lo que buscas

if __name__ == '__main__':
    app.run(debug=True)
