from flask_restful import Resource, reqparse
from common.util import load_json, dump_json, get_max

parser = reqparse.RequestParser()
parser.add_argument('reminder')
parser.add_argument('note')


class Reminders(Resource):

    def get(self):
        return load_json()

    def post(self):
        args = parser.parse_args()
        json = load_json()

        max_rem_id = get_max(json, 'reminder')
        next_id = 'reminder{}'.format(max_rem_id + 1)

        if args['reminder']:
            json[next_id] = {'note0': args['reminder']}
            dump_json(json)

            return {next_id: {'note0': args['reminder']}}
        else:
            return {'error': 'Unsupported argument'}


class Reminder(Resource):

    def get(self, rem_id):
        json = load_json()
        if rem_id in json.keys():
            return json[rem_id]
        return {}

    def delete(self, rem_id):
        json = load_json()
        if rem_id in json.keys():
            deleted = json[rem_id]
            del json[rem_id]
            dump_json(json)
            return {rem_id: deleted}
        else:
            return {'error': '{} does not exist'.format(rem_id)}

    def put(self, rem_id):
        args = parser.parse_args()
        json = load_json()

        if args['note']:
            if rem_id in json.keys():
                max_note_id = get_max(json[rem_id], 'note')
                note_id = 'note{}'.format(max_note_id + 1)
                json[rem_id][note_id] = args['note']
                dump_json(json)

                return {note_id: args['note']}
            else:
                return {'error': '{} does not exist'.format(rem_id)}
        else:
            return {'error': 'Unsupported argument'}
