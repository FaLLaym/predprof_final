from multiprocessing import Process
import requests

from main import App

from .conftest import GLOBALS

def setup(module) -> None:
    already_running = True
    try:
        __test = requests.get("http://localhost:5000/api/session/get-session", timeout=3)
    except requests.exceptions.ConnectionError: already_running = False

    if not already_running:
        GLOBALS.app = App()
        GLOBALS.app.run()

def test_server() -> None:
    assert 1==1

def test_1():
    assert 4==4

def test_3():
    assert 5==5

def teardown_module(module) -> None:
    if GLOBALS.app: GLOBALS.app.exit()
