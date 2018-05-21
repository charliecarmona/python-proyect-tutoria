import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_tutoria, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_tutoria) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_tutoria, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_tutoria) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_tutoria, **k):

    @staticmethod
    def POST_EDIT(id_tutoria, **k):
        
    '''

    def GET(self, id_tutoria, **k):
        message = None # Error message
        id_tutoria = config.check_secure_val(str(id_tutoria)) # HMAC id_tutoria validate
        result = config.model.get_tutoria(int(id_tutoria)) # search for the id_tutoria
        result.id_tutoria = config.make_secure_val(str(result.id_tutoria)) # apply HMAC for id_tutoria
        return config.render.edit(result, message) # render tutoria edit.html

    def POST(self, id_tutoria, **k):
        form = config.web.input()  # get form data
        form['id_tutoria'] = config.check_secure_val(str(form['id_tutoria'])) # HMAC id_tutoria validate
        # edit user with new data
        result = config.model.edit_tutoria(
            form['id_tutoria'],form['alumno'],form['tutor'],form['carrera'],form['grupo'],form['area_tutoria'],form['nombre_responsable'],form['acciones'],form['resolucion'],form['fecha'],
        )
        if result == None: # Error on udpate data
            id_tutoria = config.check_secure_val(str(id_tutoria)) # validate HMAC id_tutoria
            result = config.model.get_tutoria(int(id_tutoria)) # search for id_tutoria data
            result.id_tutoria = config.make_secure_val(str(result.id_tutoria)) # apply HMAC to id_tutoria
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/tutoria') # render tutoria index.html
