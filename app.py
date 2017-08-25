

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    project_list = [
    			("Wex - NLP Weather extractor ","https://github.com/HarowitzBlack/WeX","Uses NLP to detect sentences like 'what's the weather' and gives  weather forecast.","https://static.vecteezy.com/system/resources/previews/000/098/703/non_2x/vector-weather-icon-set.jpg"),
    			("Vader Bot","https://twitter.com/TheVaderBot","VaderBot is a twitter bot which tweets random DarthVader quotes every 5 minutes to random people on twitter.","https://digitalagencynetwork.com/wp-content/uploads/2014/12/flat-star-wars-icons-darth-vader.png"),
    			("ImgEd","https://github.com/HarowitzBlack/Image-Editor-Python-tkinter","Simple Image editor to edit Images - Still Incomplete","https://raw.githubusercontent.com/HarowitzBlack/Image-Editor-Python-tkinter/master/display.png"),
    			("Pixo - Pixel art maker","https://github.com/HarowitzBlack/Pixo-python3","Pixo is a simple pixel art maker. You can make pixel art in it, but you can't edit any.",""),
    			("Duckymomo - Fully functional web app","https://github.com/HarowitzBlack/Flask-webapp","Duckymomo is a webapp containing little bit of every major website outthere! (in-progress)",""),
    			("Senor Botto - A messenger bot","https://github.com/HarowitzBlack/senor-botto","A messenger bot that shows you taco vendors in your town","")
    		]
    return render_template('index.html',projects= project_list)

if __name__ == '__main__':
    app.run( debug=True, port = 8080)