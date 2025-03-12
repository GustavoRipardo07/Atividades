from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/',  methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/resultados', methods = ['GET', 'POST'])
def result():
 try:
     numero1 = int(request.args.get('numero1'))
     numero2 = int(request.args.get('numero2'))

     soma = numero1 + numero2

     return render_template('resultados.html',numero1=numero1, numero2=numero2, soma=soma)
 except (ValueError, TypeError):
    return "Erro ao processar os números. Verifique os dados inseridos."

@app.route('/autor', methods = ['GET', 'POST'])
def aut():
   return render_template('autor.html')
  
if __name__ == "__main__":
    app.run(debug=True)