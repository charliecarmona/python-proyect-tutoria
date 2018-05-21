from . import config
import app

class Printer:

	def __init__(self):

     def GET(self):

     	if app.session.loggedin is True:

     		session_privilege = app.session_privilege
     	if session_privilege ==0:
     	     return self.GET_PRINTER()
     	elif session_privilege ==1:
             raise config.web.seeother('/products')
        else:
             raise config.web.seeother('/login')    
      
      def GET_PRINTER():
      	result = config.model.get_all_datos().list()
      	   for row in result:
      return config.render.printer(result)
     	      	
