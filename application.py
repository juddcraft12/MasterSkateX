import os
from flask import url_for
import models
import routes

application = app = routes.app

if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            full_name='ZachariahJudd',
            email='juddcraft12@gmail.com',
            password='Zachj9605!',
            mobile_no='8644693128',
            admin=True
        )
    except ValueError:
        pass
    port = int(os.environ.get('PORT', 5000))
    application.run(debug = True, host='0.0.0.0', threaded=True,port=port)
