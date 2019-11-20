from firebase import firebase
firebase = firebase.FirebaseApplication('https://fir-read-temp.firebaseio.com/MyTemperatures/', None)

result1 = firebase.get('-LtOm60lsmu7a6A0UF3M', 'Temperature')
result2 = firebase.get('-LtOm60lsmu7a6A0UF3M', 'Time')

print("The temperature was:", result1)

print("At this time:", result2)