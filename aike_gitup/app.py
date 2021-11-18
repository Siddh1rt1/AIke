from flask import Flask, request, render_template, jsonify, json 
app = Flask(__name__)

import os
import jinja2

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/updatetext', methods=['POST'])
def updatetext(title):
    title =title
    return render_template(   
        'index.html', title=title )
#   server.updatetext("heyho")

#@app.route('/', methods=['POST'])
#def noreturn():
  #print("yes, ich werde ausgeführt")
  #return render_template('index.html',gifstoff="generate.gif")



@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    hell = open("input.txt","r+")
    hell.truncate(0)
    hell.write(text)
    hell.close()
    himmel =open("data/out.csv", "r+")
    top = himmel.read()

    if (str(text) not in str(top)):
      return render_template('index.html',data="Missing Data - 'Menschen' Eike hat darüber noch keinen Witz geschrieben.")  
    else:
      #data = text.upper()
      import train as till
      from train import dataset, model, text, args
      besult= till.train(dataset,model,args)
      result= till.predict(dataset,model,text)
      #train.predict(dataset, model, text, next_words=9)
      print(result)
      
      holy = open("end.txt", "r+")
      bdata = holy.read()
      holy.truncate(0)
      holy.close()
      hell = open("input.txt","r+")
      hell.truncate(0)
      hell.close()
    
      
      
      return render_template('index.html',data=bdata)



if __name__ == '__main__':
  app.run(debug=True)
  import argparse
