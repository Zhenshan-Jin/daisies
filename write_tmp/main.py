import tempfile
import os


tmpdir = tempfile.gettempdir()

def ping():
    with open(os.path.join(tmpdir, "my.txt"), "w") as istr:
        istr.write("here we go!")
