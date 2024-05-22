from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_news(number):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    # Un pedido mas que vulnerable...
    cursor.execute(f"SELECT titulo, cuerpo FROM noticias WHERE id='{number}'")
    news = cursor.fetchone()
    conn.close()
    return news

@app.route('/api/invulnerable', methods=['GET', 'POST'])
def invulnerable():
    if request.method == 'POST':
        entered_number = request.form.get('number')
        if entered_number.isdigit():
            # ...si no fuera porque exijo que lo que entre sea un numero.
            news = get_news(entered_number)
            if news:
                return render_template('noticia.html', title=news[0], content=news[1])
            # Puede ser un numero y fallar,
            else:
                return 'Noticia no encontrada', 404
        # o no ser un numero, y fallar.
        else:
            return 'Noticia buscada no valida', 404
    return render_template('pagina.html')


if __name__ == '__main__':
    app.run(debug=True)
