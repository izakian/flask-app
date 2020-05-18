from flask import Flask
from random import randint

def rand(low_num, high_num):
    """Generate rand number

    Arguments:
        low_num {int} -- int val
        hight_num {int} -- int val

    Returns:
        int -- random in range
    """
    return randint(low_num, hight_num)
  
app=Flask(__name__)
app.debug = True

@app.route('/')
def health_check():
    return "healthy!"

@app.route('/rand_generate/<int:low>/<int:high>')
def rand_generate(low, high):
    return  str(randint(low, high))

if __name__=='__main__':
    app.run()
