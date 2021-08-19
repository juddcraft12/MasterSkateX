import os
from flask import url_for
import models
import routes

application = app = routes.app

if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            full_name='{First_name_Last_name}',
            email='{Email}',
            password='{Password}',
            mobile_no='{Mobile Number}',
            admin=True #This is gonna be your admin account so keep this as true
        )
    except ValueError:
        pass
    port = int(os.environ.get('PORT', 5000))
    application.run(debug = True, host='0.0.0.0', threaded=True,port=port)
