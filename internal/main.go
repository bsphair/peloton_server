package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

/*
APIs

1. Get workout history
https://api.pelotoncycle.com/api/user/{userID}/workouts?joins=peloton.ride&limit={limit || 1}&page=0&sort_by=-created

2. Get workout
https://api.pelotoncycle.com/api/workout/{workoutID}?joins=peloton,peloton.ride,peloton.ride.instructor,user

3. Get workout sample
https://api.pelotoncycle.com/api/workout/{workoutID}/sample?every_n=10&fields=seconds_since_pedaling_start,power,cadence,speed,heart_rate,distance&limit=14400
*/

func login(w http.ResponseWriter, r *http.Request) {

	// Read the request body to get the username and password
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		log.Printf("Error reading body: %v", err)
	}

	// Make http request to login and get basic data
	resp, err := http.Post("https://api.onepeloton.com/auth/login", "application/json", bytes.NewBuffer(body))

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	data, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	json.NewEncoder(w).Encode(string(data))
}

func homePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the homepage")
}

func handleRequests() {
	http.HandleFunc("/", homePage)

	http.HandleFunc("/login", login)

	log.Fatal(http.ListenAndServe(":10000", nil))
}

func main() {
	handleRequests()
}
