from multiprocessing import Process

from backend import flask_server

class App():
    def __init__(self, port: int=5000) -> None:
        self.port = port
        self.backend_server = Process(name="Backend server", target=flask_server.main, args=(port,))

    def run(self) -> None:
        self.backend_server.start()
        print(f"{'#'*80}\nServer runs at http://localhost:{self.port}\n{'#'*80}\n")

    def exit(self) -> None:
        self.backend_server.terminate()
        print("Program ended sucessfully")

if __name__ == "__main__":
    PORT = 5000

    app = App(PORT)
    
    try:
        app.run()
        while 1: pass
    except KeyboardInterrupt: pass
    finally: app.exit()
