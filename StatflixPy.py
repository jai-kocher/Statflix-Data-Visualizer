import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import csv
import os

'''def totalTime(y, n):

    return y['Duration'].sum()'''

def displayDetails(y, n):

    return y.head(50)


def watchedByDay(y, n,path):

    y['Day'] = pd.Categorical(y['Day'], categories=[0, 1, 2, 3, 4, 5, 6], ordered=True)
    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    y_by_day = dict(y['Day'].value_counts())

    ya = y_by_day.keys()
    xa = [y_by_day[a] for a in ya]
    ya = [days[a] for a in days]
    print(ya)

    plt.bar(ya, xa,color=['red','black'])
    plt.xlabel('Day', size=16)
    plt.ylabel('Number Of Hours Watched', size=16)
    plt.title(n + ' Episodes Watched by Day',font='Helvetica 15')
    path=path+'/'+n+' By Day.jpeg'
    plt.savefig(path)
    plt.show()

def watchedByHour(y, n,path):

    y['Hour'] = pd.Categorical(y['Hour'], categories=list(range(24)), ordered=True)
    y_by_hour = dict(y['Hour'].value_counts())

    ya = y_by_hour.keys()
    xa = [y_by_hour[a] for a in ya]

    plt.bar(ya, xa ,color=['red','black'])
    plt.xlabel('Hour', size=16)
    plt.ylabel('Number Of Times Watched', size=16)
    plt.title( n + ' Episodes Watched by Hour',font='Helvetica 15')
    path=path+'/'+n+' By Hour.jpeg'
    plt.savefig(path)
    plt.show()

def watchedByDayPie(y, n,path):

    y['Day'] = pd.Categorical(y['Day'], categories=[0, 1, 2, 3, 4, 5, 6], ordered=True)
    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    y_by_day = dict(y['Day'].value_counts())

    ya = y_by_day.keys()
    xa = [y_by_day[a] for a in ya]
    ya = [days[a] for a in days]
    xa = [int(i) for i in xa]

    plt.pie(xa,labels = ya,colors=['r','k'])
    plt.title( n + ' Episodes Watched by Day',font='Helvetica 15')
    path=path+'/'+n+' By Day (Pie).jpeg'
    plt.savefig(path)
    plt.show()

def watchedByHourPie(y, n,path):

    y['Hour'] = pd.Categorical(y['Hour'], categories=list(range(24)), ordered=True)
    y_by_hour = dict(y['Hour'].value_counts())

    ya = y_by_hour.keys()
    xa = [y_by_hour[a] for a in ya]
    xa = [int(i) for i in xa]

    plt.pie(xa,labels = ya,colors=['r','k'])
    plt.title( n + ' Episodes Watched by Hour (Pie)',font='Helvetica 15')
    path=path+'/'+n+' By Hour.jpeg'
    plt.savefig(path)
    plt.show()

def genre(y):

    genreCount={'Action':0,'Adventure':0,'War':0,'Romance':0,'Drama':0,'Comedy':0,'Spiritual':0,'Fantasy':0,'Sci-Fi':0,'Superhero':0,'Thriller':0,'Musical':0,'Crime':0,'Horror':0}
    
    for i in y['Genre']:
        genreCount[i]+=1

    gc=""
    for i in genreCount.keys():
        gc=gc+"You Have Watched "+str(genreCount[i])+" "+i+" Movies/Shows\n"

    return gc

def genreBar(y,path):

    genreCount={'Action':0,'Adventure':0,'War':0,'Romance':0,'Drama':0,'Comedy':0,'Spiritual':0,'Fantasy':0,'Sci-Fi':0,'Superhero':0,'Thriller':0,'Musical':0,'Crime':0,'Horror':0}
    
    for i in y['Genre']:
        genreCount[i]+=1
    
    xa=genreCount.keys()
    ya=[genreCount[i] for i in genreCount]
    
    plt.bar(xa,ya,color=['red','black'])
    plt.xlabel('Genre',size=16)
    plt.ylabel('Number Of Movies/Shows Watched',size=16)
    plt.title('Genre Graph',font='Helvetica 15')
    path=path+'/Genre Graph.jpeg'
    plt.savefig(path)
    plt.show()

def genrePie(y,path):

    genreCount={'Action':0,'Adventure':0,'War':0,'Romance':0,'Drama':0,'Comedy':0,'Spiritual':0,'Fantasy':0,'Sci-Fi':0,'Superhero':0,'Thriller':0,'Musical':0,'Crime':0,'Horror':0}
    
    for i in y['Genre']:
        genreCount[i]+=1
    
    xa=genreCount.keys()
    ya=[int(genreCount[i]) for i in genreCount]
    
    plt.pie(ya,labels=xa,colors=['r','k'])
    plt.title('Genre Graph',font='Helvetica 15')
    path=path+'/Genre Graph.jpeg'
    plt.savefig(path)
    plt.show()

def open_recomendation():
    pass

def open_window(res, user):
    path='C:/Users/mjohn/Desktop/sem2/python/package/'+user
    mode=0o666
    if os.path.isdir(path):
        pass
    else:
        os.makedirs(path,mode)

    sg.theme('DarkBrown4')

    layout = [[sg.Text('Movie/Series : ', size=(30, 1), font='Consolas 16', justification='left')],
              [sg.Combo(res, font='Consolas 20', default_value='The Big Bang Theory', key='name')],
              [sg.Text('Choice : ', size=(30, 1), font='Consolas 16', justification='left')],
              [sg.Listbox(values=["Display The Amount Of Time You Have Spent Watching",
                                  "Display A Table Containing Your Viewing History", "Episodes Watched By Day (Bar Chart)",
                                  "Episodes Watched By Hour","Episodes Watched By Day (Pie Chart)","Episodes Watched By Hour (Pie Chart)",
                                  "Number of Movies/Shows You Have Watched of Each Genre","Movie/Show Genres And Number of Times Watched (Bar Chart)",
                                  "Movie/Show Genres And Number of Times Watched (Pie Chart)"], 
                                  font='Helvitica 16', select_mode='extended',size=(60, 6), key='options')],
              [sg.Button("OK", font="TimesNewRoman 16")]]

    win = sg.Window( user + '- Netflix History', layout)
    e, v = win.read()

    name = v['name']
    x = df[df['Title'].str.contains(name)]
    x['Day'] = x['Start Time'].dt.weekday
    x['Hour'] = x['Start Time'].dt.hour
    x = x[(x['Duration'] > '0 days 00:01:00')]
    for option in v['options']:
        if option == "Display The Amount Of Time You Have Spent Watching":
            sg.popup('Total Time', "You Have Spent " + str(x['Duration'].sum()) + " In Total To Watch "+ name, font="Consolas 18")
        if option == "Display A Table Containing Your Viewing History":
            sg.ScrolledTextBox(displayDetails(x, name),  font="helvetica 10")#button_color='Black',
        if option == "Episodes Watched By Day (Bar Chart)":
            watchedByDay(x, v['name'],path)
        if option == "Episodes Watched By Hour (Bar Chart)":
            watchedByHour(x, v['name'],path)
        if option == "Episodes Watched By Day (Pie Chart)":
            watchedByDayPie(x, v['name'],path)
        if option == "Episodes Watched By Hour (Pie Chart)":
            watchedByHourPie(x, v['name'],path)
        if option == "Number of Movies/Shows You Have Watched of Each Genre":
            sg.ScrolledTextBox(genre(df), size=(100,100),button_color='Black', font="helvetica 10")
        if option == "Movie/Show Genres And Number of Times Watched (Bar Chart)":
            genreBar(df,path)
        if option == "Movie/Show Genres And Number of Times Watched (Pie Chart)":
            genrePie(df,path)

    win.close()


file = open("va.csv", "r",errors='ignore')
csv_reader = csv.reader(file)

lists_from_csv = []
z=[]
users = []
for row in csv_reader:
    lists_from_csv.append(row)#The whole .csv file
for i in range(1, 1211):
    z.append(lists_from_csv[i][4])#Movie/Show Titles
for i in range(1, 1211):
    users.append(lists_from_csv[i][0])#Users
file.close()
res = []
userrev=[]
for i in z:
    if i not in res:
        res.append(i)#Duplicate Movie/Show Titles removed
for i in users:
    if i not in userrev:
        userrev.append(i)#Duplicate Users removed
file.close()


df = pd.read_csv('va.csv')
df = df.drop(['Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'],axis=1)
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df = df.set_index('Start Time')
df.index = df.index.tz_convert('Asia/Kolkata')#Since the data downloaded from Netflix displays time in UTC format, we change it to IST format
df = df.reset_index()
df['Duration'] = pd.to_timedelta(df['Duration'])
sg.theme('DarkBrown4')
layout = [[sg.Text('StatFlix User Login', size=(30, 1), font='Consolas 16', justification='center')],
          [sg.Text('Username'),sg.Combo(userrev, font='Consolas 16', default_value='Jai', key='name')],
          [sg.Text('Password'),sg.InputText(size=(21,21),key='pass')],
          [sg.Button("Login", font = 'Helvetica 14', key='open')]]
window = sg.Window("Login", layout)
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "open" and values['pass']=='netflix123':
        open_window(res, values['name'])
window.close()