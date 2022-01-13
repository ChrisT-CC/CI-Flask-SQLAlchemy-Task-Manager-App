""" Import os in order to utilize environment variables within this file """
import os
from taskmanager import app


# Tell our app how and where to run the application
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
