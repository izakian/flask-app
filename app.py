from flask import Flask
from random_number_generator import RandomNumber
  
app=Flask(__name__)
app.debug = True

@app.route('/')
def health_check():
    return "healthy!"

@app.route('/rand_generate/<int:low>/<int:high>')
def rand_generate(low, high):
    rand_val=RandomNumber(low, high).generate()
    return  str(rand_val)

if __name__=='__main__':
    app.run()
