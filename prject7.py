from flask import *
import requests
import json

app=Flask(__name__)
@app.route("/")
def hee2():
   return render_template("weat1.html")

@app.route("/ab",methods=["POST","GET"])
def hee1():
   if request.method == 'POST': 
      city=request.form["city"]
      url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=34030538374555f778761b7694e3132d'.format(city)
      response = requests.get(url)
      data = response.json()
      weather=data['weather'][0]['description']
      country1=data['sys']['country']
      pressure1=data['main']['pressure']
      temprature=((data['main']['temp'])-273.15)
      humdity1=data['main']['humidity']
      
   return render_template("weat1.html", weather=weather,country1=country1,pressure1=pressure1,temprature=temprature, humdity1=humdity1,city=city)



if __name__=='__main__':
    app.run()





i
