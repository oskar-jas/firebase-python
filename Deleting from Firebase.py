from firebase import firebase
firebase = firebase.FirebaseApplication('https://fir-read-temp.firebaseio.com/', None)

firebase.delete('/dht', None)

print("You have successfully deleted from your firebase")