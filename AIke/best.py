
import js2py
js1 = 'var x = /data/index.getElementById("story").value ; console.log("Hello World")'
js2 ='var x = document.getElementById("story").value' 
js3 = ' document.getElementById("story").value= x + "textmore" '
res1 = js2py.eval_js(js1)
res1