from flask import Flask
from flask_restful import Api
from resources.reminders import Reminders, Reminder

app = Flask(__name__)
api = Api(app)

api.add_resource(Reminders, '/reminders')
api.add_resource(Reminder, '/reminders/<rem_id>')

if __name__ == '__main__':
    app.run(debug=True)
