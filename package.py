import pandas as pd
import matplotlib.pyplot as plt

def totalTime(y,n):

    print("You Have Spent",x['Duration'].sum(),"In Total To Watch",n)

def displayDetails(y,n):

    print(y.head(100))

def watchedByDay(y,n):

    y['Day']=pd.Categorical(y['Day'],categories=[0,1,2,3,4,5,6],ordered=True)
    days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    y_by_day=dict(y['Day'].value_counts())

    ya=sorted(y_by_day.keys())
    xa=[y_by_day[a] for a in ya]
    ya=[days[a] for a in days]

    plt.bar(ya,xa)
    plt.rcParams.update({'font.size':16})
    plt.xlabel('Day',size=16)
    plt.ylabel('Number Of Hours Watched',size=16)
    plt.title(name+' Episodes Watched by Day')
    plt.show()

def watchedByHour(y,n):

    y['Hour']=pd.Categorical(y['Hour'],categories=list(range(24)),ordered=True)
    y_by_hour=dict(y['Hour'].value_counts())

    ya=sorted(y_by_hour.keys())
    xa=[y_by_hour[a] for a in ya]

    plt.bar(ya,xa)
    plt.rcParams.update({'font.size':16})
    plt.xlabel('Hour',size=16)
    plt.ylabel('Number Of Times Watched',size=16)
    plt.title(name+' Episodes Watched by Hour')
    plt.show()
        

df=pd.read_csv('va.csv')
df=df.drop(['Attributes','Supplemental Video Type','Device Type','Bookmark','Latest Bookmark','Country'],axis=1)#Dropping Unnecessary Columns
df['Start Time']=pd.to_datetime(df['Start Time'],utc=True)
df=df.set_index('Start Time')
df.index=df.index.tz_convert('Asia/Kolkata')
df=df.reset_index()
df['Duration']=pd.to_timedelta(df['Duration'])

ch=1
while ch!=0:
    name=input("Enter The Show/Movie You Have Watched: ")

    x = df[df['Title'].str.contains(name)]
    x['Day']=x['Start Time'].dt.weekday
    x['Hour']=x['Start Time'].dt.hour
    x=x[(x['Duration']>'0 days 00:01:00')]

    print("1. Display The Amount Of Time You Have Spent Watching",name)
    print("2. Display A Table Containing Your Viewing History of",name)
    print("3. Display A Bar Graph Showing",name,"Episodes Watched By Day")
    print("4. Display A Bar Graph Showing",name,"Episodes Watched By Hour")
    print("0. Exit")
    ch=int(input("Enter Your Choice: "))

    if ch==1:

        totalTime(x,name)
    elif ch==2:

        displayDetails(x,name)
    elif ch==3:

        watchedByDay(x,name)
    elif ch==4:

        watchedByHour(x,name)
    else:

        break
    

