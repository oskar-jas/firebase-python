from firebase import firebase
firebase = firebase.FirebaseApplication('https://fir-read-temp.firebaseio.com/', None)

result = firebase.patch('TempRN/', {'Temperature': 7})
result1 = firebase.get('TempRN/', 'Temperature')

print("The temperature is:", result1, "degrees right now")