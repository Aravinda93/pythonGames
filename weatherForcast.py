import tkinter as tk
from tkinter import font
import requests

HEIGHT  = 500
WIDTH   = 500

#http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=
def getWeather(city):
    weatherKey  =   '8d3badca2f750ca4041ba043b42eebf7'
    weatherURL  =   'http://api.openweathermap.org/data/2.5/weather'
    params      =   {'APPID':weatherKey,'q':city,'units':'metric'}
    response    =   requests.get(weatherURL,params=params)
    weatherData =   response.json()
    weatherimg  =   ''

    try:
        name        =   weatherData['name']
        condition   =   weatherData['weather'][0]['description']
        temp        =   weatherData['main']['temp']
        weatherimg  =   weatherData['weather'][0]['icon']
        allData     =   'City: '+str(name)+'\nCondition: '+str(condition)+'\nTemparature: '+str(temp)
    except:
        allData     =   'There was some problem during the retreival of information'

    label['text']   =   allData;
    #label['text'].append(Image.open(os.path.join(path,f));

#main window
root            =   tk.Tk();
canvas          =   tk.Canvas(root, height=HEIGHT, width=WIDTH);
canvas.pack();

backgroundimage =   tk.PhotoImage(file='weather.png');
backgroundlabel =   tk.Label(root,image=backgroundimage);
backgroundlabel.place(relwidth=1,relheight=1);

frame           =   tk.Frame(root, bg='#80c1ff', bd=5);
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1, anchor='n');

entry           =   tk.Entry(frame,font=('Courier',18));
entry.place(relwidth=0.65,relheight=1);

button          =   tk.Button(frame, text='Submit', bg='gray',font=('Courier',12), command=lambda:getWeather(entry.get()));
button.place(relx=0.7,relwidth=0.3,relheight=1);

lowerframe      =   tk.Frame(root,bg='#80c1ff', bd=10);
lowerframe.place(relx=0.5, rely=0.25,relwidth=0.75,relheight=0.6,anchor='n');

label           =   tk.Label(lowerframe,font=('Courier',16), anchor='center');
label.place(relwidth=1,relheight=1);

root.mainloop()