
def ping(error="false"):
    
    if error == "false":
        print("here is the standard output")
    else:
        raise ValueError("here is the standard error")

    return None
