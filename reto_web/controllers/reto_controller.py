from odoo import http
from odoo.http import request

class RetoController(http.Controller):
    @http. route('/reto', auth='public', website=True)
    def reto(self):
        try: 
            user = request.env.user
            if user and user.id and user.id!= request.env.ref('base.public_user').id:
                nombre = user.name
                return "<h1>Hello {}</h1>".format(nombre)
            else:
                return "<h1>Hello World!</h1>"
        except Exception as e:
            return "<h1>Error: {}</h1>".format(str(e))