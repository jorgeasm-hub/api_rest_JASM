
#Aplicacion que calcula el monto o el capital de una cantidad de dinero, con interes compuesto
from flask import Flask, jsonify, request

app = Flask(__name__)

def calculo_monto(capital):
    calculo =capital*((1+(0.23/12))**(6))
    return calculo

def calculo_capital(monto):
    calculo = monto/(((1+(0.23/12))**(6)))
    return calculo

@app.route('/', methods = ['POST'])
def convert_temp():
    data = request.get_json()
    input_dinero=data.get('cantidad')
    
    if data['type'] == 'capital':
        output_unit = 'monto'
        result = calculo_monto(input_dinero)
        
    
    if data['type'] == 'monto':
        output_unit = 'capital'
        result = calculo_capital(input_dinero)
        
    return jsonify({"unit": output_unit, "cantidad": result})
    
 
if __name__ == '__main__':
    app.run(debug=False)
