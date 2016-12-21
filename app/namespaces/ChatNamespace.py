from flask import session, request, current_app
from flask_socketio import Namespace, emit, join_room, leave_room, \
    close_room, rooms, disconnect

thread = None


class ChatNamespace(Namespace):
    def on_login(self, message):
        current_app.logger.info(message)
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']})

    def on_my_event(self, message):
        print message
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']})

    def on_my_broadcast_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']},
             broadcast=True)

    def on_join(self, message):
        join_room(message['room'])
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'In rooms: ' + ', '.join(rooms()),
              'count': session['receive_count']})

    def on_leave(self, message):
        leave_room(message['room'])
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'In rooms: ' + ', '.join(rooms()),
              'count': session['receive_count']})

    def on_close_room(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response', {'data': 'Room ' + message['room'] + ' is closing.',
                             'count': session['receive_count']},
             room=message['room'])
        close_room(message['room'])

    def on_my_room_event(self, message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']},
             room=message['room'])

    def on_disconnect_request(self):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()

    def on_my_ping(self):
        emit('my_pong')

    def on_connect(self):
        print "connect id", request.sid
        session['receive_count'] = session.get('receive_count', 0) + 1

        # global thread
        # if thread is None:
        # thread = self.socketio.start_background_task(target=self.background_thread)
        emit('heartbeat', {'data': 'Connected', 'count': session['receive_count']})

    def on_disconnect(self):
        print('Client disconnected', request.sid)

    def background_thread(self):
        """Example of how to send server generated events to clients."""
        self.count = 0
        while True:
            # from ..setup import socketio
            self.socketio.sleep(2)
            self.count += 1
            print "send my response.."
            print self.socketio
            self.emit('heartbeat', {'data': 'Server generated event', 'count': self.count})
