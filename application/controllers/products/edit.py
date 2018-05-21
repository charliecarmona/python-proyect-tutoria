import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_product, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_product) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_product, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_product) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_product, **k):

    @staticmethod
    def POST_EDIT(id_product, **k):
        
    '''

    def GET(self, id_product):
        
    	result = config._secure_val(id_product)
    	return config.render.edit(result)

    	def POST(self,id_product):
    		form = config.web.input()
    		image = config.web.input(product_image={})
    		filedir = 'static/files'
    		filepath = image.product_image.filename.replace('\\','/')
    		filename = filepath.split('/')[-1]
    		fout = open(filedir + '/'+ filename, 'w')
    		fout.write(image.product_image.file.read())
    		fout.close()
    		product_image = filename

    		config.model.edit_products(
                   form['id_product'],
                   form['product'],
                   form['description'],
                   form['stok'],
                   form['purchase_price'],
                   form['price_sale'],
                   product_image
                   )
    		
 

    			
