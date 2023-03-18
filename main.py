from multiprocessing import Process

class App():
    def __init__(self, frontend_port: int=8081) -> None:
        self.frontend_port = frontend_port
        self.frontend_server = Process(name="Frontend server", target=..., args=(self.frontend_port)) #TODO
        self.backend_server = Process(name="Backend server", target=...) #TODO

    def run(self) -> None:
        self.backend_server.start()
        self.frontend_server.start()

    def exit(self) -> None:
        self.backend_server.terminate()
        self.frontend_server.terminate()
        print("Program ended sucessfully")

if __name__ == "__main__":
    FRONTEND_PORT = 8081

    app = App(FRONTEND_PORT)
    
    try:
        app.run()
        while 1: pass
    except KeyboardInterrupt: pass
    finally: app.exit()
