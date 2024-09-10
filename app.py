# app.py
from Flask import Flask, render_template

app = Flask(__name__)

# Dados dos signos
signos = {
    "Áries": "Áries é um signo de fogo, e as pessoas deste signo são conhecidas por sua energia e entusiasmo.",
    "Touro": "Touro é um signo de terra, e seus nativos são famosos por sua lealdade e determinação.",
    "Gêmeos": "Gêmeos é um signo de ar, e as pessoas deste signo são comunicativas e adaptáveis.",
    "Câncer": "Câncer é um signo de água, e os nativos deste signo são sensíveis e intuitivos.",
    "Leão": "Leão é um signo de fogo, caracterizado por seu carisma e autoconfiança.",
    "Virgem": "Virgem é um signo de terra, conhecido por seu perfeccionismo e atenção aos detalhes.",
    "Libra": "Libra é um signo de ar, e seus nativos são diplomáticos e amantes da harmonia.",
    "Escorpião": "Escorpião é um signo de água, marcado pela intensidade emocional e paixão.",
    "Sagitário": "Sagitário é um signo de fogo, famoso por seu espírito aventureiro e otimismo.",
    "Capricórnio": "Capricórnio é um signo de terra, conhecido por sua ambição e disciplina.",
    "Aquário": "Aquário é um signo de ar, caracterizado pela inovação e originalidade.",
    "Peixes": "Peixes é um signo de água, e seus nativos são compassivos e sonhadores."
}

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html', signos=signos)

# Rota para página específica do signo
@app.route('/signo/<nome>')
def signo(nome):
    descricao = signos.get(nome.capitalize(), "Signo não encontrado.")
    return render_template('signo.html', nome=nome.capitalize(), descricao=descricao)

if __name__ == '__main__':
    app.run(debug=True)