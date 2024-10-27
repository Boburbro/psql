from colorama import Fore

def check_func(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(Fore.RED+f"SQL ERROR: {error}")
    return wrapper_func

def greenPrint(msg: str):
    print(Fore.GREEN+msg)