from django.shortcuts import render
import joblib
import pandas as pd
import datetime
from geopy.distance import geodesic
import numpy as np

model = joblib.load('./savedModels/best_model.pkl')


# Create your views here.
#def Welcome(request):
#    return render(request,'UI.html')
cols = ['Traffic Condition', 'pickup_longitude', 'pickup_latitude',
       'dropoff_longitude', 'dropoff_latitude', 'hour', 'day', 'month',
       'weekday', 'year', 'bearing', 'distance']
def measure_distance(point1, point2):
    distance = geodesic(point1, point2).km
    return distance

def formInfo(request):
    if request.method == 'POST':
        Traffic_Condition = request.POST['Traffic_Condition']
        pickup_longitude = request.POST['pickup_longitude']
        pickup_latitude = request.POST['pickup_latitude']
        dropoff_longitude = request.POST['dropoff_longitude']
        dropoff_latitude = request.POST['dropoff_latitude']
        '''
        hour = request.POST['hour']
        day = request.POST['day']
        month = request.POST['month']
        weekday = request.POST['weekday']
        year = request.POST['year']
        distance = request.POST['distance']
        bearing = request.POST['bearing']
        '''
        hour = datetime.datetime.now().hour
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        weekday = datetime.datetime.now().isoweekday()
        year = datetime.datetime.now().year
        '''
        #for bearing calculations
        point1 = np.array([pickup_longitude,pickup_latitude],dtype='str').astype(np.float32)
        point2 = np.array([dropoff_longitude,dropoff_latitude],dtype='str').astype(np.float32)
        bearing = np.linalg.norm(point1 - point2)
        '''
        bearing = request.POST['bearing']
        # pickup and dropoff coordinates
        pickup = (pickup_longitude,pickup_latitude)
        dropoff = (dropoff_longitude,dropoff_latitude)
        # measure the distance
        distance = measure_distance(pickup,dropoff)
        data = [Traffic_Condition, pickup_longitude, pickup_latitude,
                dropoff_longitude, dropoff_latitude,hour, day, month,
                weekday, year, bearing,distance]
        data = pd.DataFrame([data],columns=cols)
        print(data)
        y_pred = model.predict(data)
        print(y_pred)
        return render(request,'test.html',{'result' : y_pred})
    return render(request, 'test.html')