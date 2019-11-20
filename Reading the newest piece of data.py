from firebase import firebase
firebase = firebase.FirebaseApplication('https://fir-read-temp.firebaseio.com/', None)

result = firebase.get('MyTemperatures/', None)

names = []

for name in result:
    names.append(name)

print("The temperature is:", result[names[-1]]['Temperature'])

print("At", result[names[-1]]['Time'])