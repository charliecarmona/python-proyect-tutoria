import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tutoria, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_tutoria) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tutoria, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_tutoria) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_tutoria, **k):

    @staticmethod
    def POST_DELETE(id_tutoria, **k):
    '''

    def GET(self, id_tutoria, **k):
        message = None # Error message
        id_tutoria = config.check_secure_val(str(id_tutoria)) # HMAC id_tutoria validate
        result = config.model.get_tutoria(int(id_tutoria)) # search  id_tutoria
        result.id_tutoria = config.make_secure_val(str(result.id_tutoria)) # apply HMAC for id_tutoria
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_tutoria, **k):
        form = config.web.input() # get form data
        form['id_tutoria'] = config.check_secure_val(str(form['id_tutoria'])) # HMAC id_tutoria validate
        result = config.model.delete_tutoria(form['id_tutoria']) # get tutoria data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_tutoria = config.check_secure_val(str(id_tutoria))  # HMAC user validate
            id_tutoria = config.check_secure_val(str(id_tutoria))  # HMAC user validate
            result = config.model.get_tutoria(int(id_tutoria)) # get id_tutoria data
            result.id_tutoria = config.make_secure_val(str(result.id_tutoria)) # apply HMAC to id_tutoria
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/tutoria') # render tutoria delete.html 
