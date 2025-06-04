import asyncio
import os
import uuid
import json
from prompt_toolkit import Application
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import TextArea, Frame
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.containers import HSplit
import pywinpty

SESSIONS_FILE = 'sessions.json'

class Session:
    def __init__(self, session_id, command='cmd.exe'):
        self.session_id = session_id
        self.command = command
        self.spawn = pywinpty.Spawn(command)
        self.output = ""

    def read(self):
        try:
            data = self.spawn.read()
            self.output += data
            return data
        except Exception as e:
            return str(e)

    def write(self, data):
        self.spawn.write(data)

    def close(self):
        self.spawn.close()

class ScreenClone:
    def __init__(self):
        self.sessions = {}
        self.current_session_id = None
        self.output_area = TextArea(focusable=False)
        self.input_area = TextArea(height=1)
        self.load_sessions()

        self.kb = KeyBindings()
        self.bind_keys()

        self.app = Application(
            layout=Layout(HSplit([
                Frame(self.output_area, title="Output"),
                Frame(self.input_area, title="Input")
            ])),
            key_bindings=self.kb,
            full_screen=True,
        )

    def bind_keys(self):
        @self.kb.add('c-c')
        def _(event):
            self.save_sessions()
            event.app.exit()

        @self.kb.add('c-n')
        def _(event):
            self.create_session()

        @self.kb.add('c-s')
        def _(event):
            self.switch_session()

        @self.kb.add('enter')
        def _(event):
            if self.current_session_id:
                cmd = self.input_area.text + '\r\n'
                self.sessions[self.current_session_id].write(cmd)
                self.input_area.text = ''

    def create_session(self):
        session_id = str(uuid.uuid4())
        session = Session(session_id)
        self.sessions[session_id] = session
        self.current_session_id = session_id

    def switch_session(self):
        keys = list(self.sessions.keys())
        if self.current_session_id in keys:
            idx = (keys.index(self.current_session_id) + 1) % len(keys)
            self.current_session_id = keys[idx]

    def load_sessions(self):
        if os.path.exists(SESSIONS_FILE):
            with open(SESSIONS_FILE, 'r') as f:
                ids = json.load(f)
                for session_id in ids:
                    self.sessions[session_id] = Session(session_id)
                if ids:
                    self.current_session_id = ids[0]

    def save_sessions(self):
        with open(SESSIONS_FILE, 'w') as f:
            json.dump(list(self.sessions.keys()), f)
        for session in self.sessions.values():
            session.close()

    async def update_output(self):
        while True:
            if self.current_session_id:
                data = self.sessions[self.current_session_id].read()
                if data:
                    self.output_area.text = self.sessions[self.current_session_id].output
            await asyncio.sleep(0.2)

    def run(self):
        asyncio.ensure_future(self.update_output())
        self.app.run()


if __name__ == '__main__':
    screen = ScreenClone()
    screen.run()
