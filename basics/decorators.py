def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce       # hello function is wrapped in announce decorator
def hello():
    print("hello world")

hello()
