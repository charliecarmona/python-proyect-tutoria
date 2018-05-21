import config


class Delete:
    
    def __init__(self):
        pass

  '''  
    def GET(self, id_product, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_product) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_product, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_product) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html
'''
    @staticmethod
    def GET_DELETE(id_product, **k):

    @staticmethod
    def POST_DELETE(id_product, **k):
   

    def GET(self, id_product):

    	result = config._secure_val(id_product)
    	return config.render.delete(result)


   def POST(self, id_product):
  	   form = config.web.input()
   	   config.model.delete_products(form['id_product'])



   	   