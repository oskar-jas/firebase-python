from firebase import firebase
firebase = firebase.FirebaseApplication('https://fir-read-temp.firebaseio.com/', None)
temperatur = 'Temperature'
newTemp = 2
result = firebase.post('MyTemperatures', {temperatur : newTemp})

print("The temperature that you just added is", newTemp)