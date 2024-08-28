# -*- coding: utf-8 -*-


from odoo.http import Controller, request , route

class CarpoolingController(Controller):

    #c la route (/carpooling) ou la nouvelle page web avec une desription de cette route
    @route('/carpooling', methods=["GET"], auth='public' , website=True)

    #la fonction qui sera lancer une fois on accede a la pge web
    def carpooling(self):
        carpoolings =request.env['carpooling.carpooling'].search([]) #cette ligne c pour chercher les objets carpooling c'est une cpommande tres utile (on peut utiliser .sudo avant le search pour que les donnes de pages soient aceesbles au pubbblic
        return request.render('carpooling.carpooling_website',{'carpoolings' : carpoolings}) #carpooling_website sera l'id de la template siteweb qu'on a creer , le deuxieme arguments est dedie au passage des donnes à notre vue
