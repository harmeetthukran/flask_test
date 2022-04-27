from flask import Flask, redirect, url_for, render_template,request
import dl_translate as dlt
import time
mt = dlt.TranslationModel("m2m100")  
from multiprocessing import Process

app =Flask(__name__)
#

def trans(txt,lang):
    
    # p1 = Process(target=sleeping, args=()).start()
    data=mt.translate(txt,source=lang,target="English")
    return (data)
    

@app.route("/",methods=["POST","GET"])
def home():
    translated_text=""
    
   
    if request.method == "POST":
       
        user = request.form["input_text"]
        lang=(request.form["lang"])
       
        translated_text=trans(user,lang)
        
        
    return """
<body>
<div id="parent">
    <style>
    
    select {
  /* Reset */
  appearance: none;
 border-width: thick;
  outline: 0;
  font: inherit;
  /* Personalize */
  width: 20em;
  height: 3em;
/*  padding: 0 4em 0 1em;*/
/*
  background: url(https://upload.wikimedia.org/wikipedia/commons/9/9d/Caret_down_font_awesome_whitevariation.svg)
      no-repeat right 0.8em center / 1.4em,
    linear-gradient(to left, $glass-icon 3em, $glass 3em);
*/
  color: dimgrey;
  border-radius: 0.25em;
  box-shadow: 0 0 1em 0 rgba(0, 0, 0, 0.2);
  cursor: pointer;
  /* <option> colors */
  option {
    color: inherit;
    background-color: $option;
  }
  /* Remove focus outline */
  &:focus {
    outline: none;
  }
  /* Remove IE arrow */
  &::-ms-expand {
    display: none;
  }
}
button {
  /* Reset */
     text-align: center;
    background-color:white;
  appearance: none;
  border-width: thick;
  outline: 20;
  font: inherit;
  /* Personalize */
  width: 20em;
  height: 3em;
    
/*  padding: 0 4em 0 1em;*/
/*
  background: url(https://upload.wikimedia.org/wikipedia/commons/9/9d/Caret_down_font_awesome_whitevariation.svg)
      no-repeat right 0.8em center / 1.4em,
    linear-gradient(to left, $glass-icon 3em, $glass 3em);
*/
  color: dimgray;
  border-radius: 0.25em;
  box-shadow: 0 0 1em 0 rgba(0, 0, 0, 0.2);
  cursor: pointer;
  /* <option> colors */
  option {
    color: inherit;
    background-color: $option;
  }
  /* Remove focus outline */
  &:focus {
    outline: none;
  }
  /* Remove IE arrow */
  &::-ms-expand {
    display: none;
  }
}

textarea::-webkit-input-placeholder { opacity: 1; -webkit-transition: opacity .5s; transition: opacity .5s; }  /* Chrome <=56, Safari < 10 */
textarea:-moz-placeholder { opacity: 1; -moz-transition: opacity .5s; transition: opacity .5s; } /* FF 4-18 */
textarea::-moz-placeholder { opacity: 1; -moz-transition: opacity .5s; transition: opacity .5s; } /* FF 19-51 */
textarea:-ms-input-placeholder { opacity: 1; -ms-transition: opacity .5s; transition: opacity .5s; } /* IE 10+ */
textarea::placeholder { opacity: 1; transition: opacity .5s; } /* Modern Browsers */
    
*:focus::-webkit-input-placeholder { opacity: 0; } /* Chrome <=56, Safari < 10 */
*:focus:-moz-placeholder { opacity: 0; } /* FF 4-18 */
*:focus::-moz-placeholder { opacity: 0; } /* FF 19-50 */
*:focus:-ms-input-placeholder { opacity: 0; } /* IE 10+ */
*:focus::placeholder { opacity: 0; } /* Modern Browsers */



textarea::placeholder{
/*    color: transparent;*/
    text-decoration: underline;
  text-align:center;
    height: 50px;
/*  line-height:25px;*/
}
#parent {
  display: flex;
  justify-content: center;
  align-items: center;
}
.textarea {
  background-color: #dddddd;
  color: #666666;
  padding: 1em;
  border-radius: 10px;
  border: 2px solid transparent;
  outline: none;
  font-family: "Heebo", sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 1.4;
  width: 400px;
  height: 500px;
  transition: all 0.2s;
}


.textarea:hover {
  cursor: pointer;
  background-color: #eeeeee;
}

.textarea:focus {
  cursor: text;
  color: #333333;
  background-color: white;
  border-color: #333333;
}

    
    
    
    </style>
<h1  style = "font-size: 40px;">Multi Language Translator</h1>
    </div>
    <div id="parent">
<h4 style = "font-size: 20px;font-weight:normal;">Select Language</h4>
        
    </div>
    <form action="#" method="post">
       
  <div id="parent" >
  <select name="lang" style="margin-bottom: 20px;font-size: 20px;text-align: center;">
  <option name = "ps" selected value="ps">Pashto</option>
  <option name = "my" value="my">Burmese</option>
  <option name = "ne" value="ne">Nepali</option>
  <option name = "si" value="si">Sinhala</option>
  <option name = "ur" value="ur">Urdu</option>
  <option name = "zh" value="zh">Chinese</option>
</select>

</div>



      
    <div id="parent">
       
<textarea class="textarea" id="id_input" name="input_text" style="margin-right: 20px; " placeholder="Input"></textarea> 
       
    <textarea class="textarea" id="output" placeholder="Output">"""+translated_text+ """</textarea>
    </div>
 
    
<div id="parent">
    
    <button id="mybutton" type="submit" style="margin-top: 20px;text-align: center;font-size: 20px;">Translate Text</button>

    </div>
   
</form>
  """
    # return render_template("index.html",result=d)

       



if __name__ == "__main__":
    app.run(debug=True)