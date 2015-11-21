# Usage

To run:
`python app.py`

GET all reminders:
`curl http://localhost:5000/reminders`

GET a single reminder:
`curl http://localhost:5000/reminders/<rem_id>`

DELETE a reminder:
`curl http://localhost:5000/reminders/<rem_id> -X DELETE`

Add a new reminder:
`curl http://localhost:5000/reminders -d "reminder=new" -X POST`

Add a new note:
`curl http://localhost:5000/reminders/reminder0 -d "note=new" -X PUT`
