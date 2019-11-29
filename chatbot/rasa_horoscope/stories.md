## ask horoscope + positive feedback
* greet
  - utter_greet
* ask_horoscope{"horoscopelist": "capricon"}
  - action_horoscope
  - utter_did_that_help 
* affirm
  - utter_gratitude
  - action_restart

## ask horoscope + positive feedback
* greet
  - utter_greet
* ask_horoscope{"horoscopelist": "capricon"}
  - action_horoscope
  - utter_did_that_help
* ask_horoscope{"horoscopelist": "capricon"}
  - action_horoscope
  - utter_did_that_help
* affirm
  - utter_gratitude
  - action_restart


## ask horoscope + positive feedback
* greet
  - utter_greet
* ask_horoscope{"horoscopelist": "capricon"}
  - action_horoscope
  - utter_did_that_help
* ask_horoscope{"horoscopelist": "capricon"}
  - action_horoscope
  - utter_did_that_help
* deny
  - utter_sorry
  - action_restart


## ask horoscope + negative feedback
* greet
  - utter_greet
* ask_horoscope{"horoscopelist": "capricon"}
  - action_horoscope
  - utter_did_that_help
* deny
  - utter_sorry
  - action_restart



## thank you
* thankyou
  - utter_gratitude

