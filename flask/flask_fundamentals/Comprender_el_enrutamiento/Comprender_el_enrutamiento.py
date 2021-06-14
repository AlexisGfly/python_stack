from flask import Flask  

app = Flask(__name__)    


@app.route('/')          
def hello_world():
    return 'Hola Mundo!' 

@app.route('/dojo')
def success():
    return "Dojo!"


@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "¡Hola, " + name + "!"

@app.route('/repeat/<times>/<name>') 
def show_user_profile(times, name):
    print(times)
    print(name)
    return (name*int(times))

if __name__=="__main__":   
    app.run(debug=True)    