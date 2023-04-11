from flask import Flask, render_template, request
# importando o re para uso de expressões regulares
import re

app = Flask(__name__)

# criando 'dicionário' de palavras censuradas
palavroes = ['porra', 'merda', 'foda', 'cu', 'filho da puta', 'caralho', 'arrombado', 'piranha', 'bosta']

# analisando o teor do comentário
def analisar_sentimento(texto):

    # limpando caracteres especiais e transformando o texto em minúsculas
    texto = re.sub(r'[^\w\s]', '', texto.lower())
    
    # verificando se alguma palavra ofensiva está presente no texto
    for palavra in palavroes:
        if palavra in texto:
            return 'Conteúdo impróprio'
    
    # caso nenhuma palavra ofensiva for encontrada, atribuir polaridade neutra ao texto
    return 'Conteúdo aprovado'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        resultado = analisar_sentimento(texto)
        return render_template('resultado.html', resultado=resultado)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()