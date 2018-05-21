import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    '''
    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_username = app.session.privilege  # get the session_privilege
            if session_username == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_username == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_username = app.session.privilege # get the session_privilege
            if session_username == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():

    @staticmethod
    def POST_INSERT():
    '''

    def GET(self):
        return config.render.insert() # render insert.html

    def POST(self):
        form = config.web.input() # get form data
        image = config.web.input(product_image={})
        filedir = 'static/files'
        filepath = image.product_image.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
        fout = open(filedir + '/' + filename, 'w')
        fout.write(image.product_image.file.read())
        fout.close()
        product_image = filename


        # call model insert_products and try to insert new data
        config.model.insert_products(
            form['product'],form['stock'],form['description'],form['purchase_price'],form['price_sale'],product_image
        )
        raise config.web.seeother('/products') # render products index.html
