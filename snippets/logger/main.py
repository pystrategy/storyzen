import os
import logging

from kivy.config import Config

log_dir = os.path.join(os.getcwd(), 'logs')
Config.set('kivy', 'log_dir', log_dir)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Root(BoxLayout):
    pass


class LoggerApp(App):
    def build(self):
        root = Root()
        return root


if __name__ == "__main__":
    logging.info("Application Start")
    LoggerApp().run()
    logging.info("Application Finish")
