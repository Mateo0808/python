# dependecia para hacer un bluprint
from flask import Blueprint     

# definimos paquete 'products'
products = Blueprint('products',
                     __name__,
                     url_prefix='/products',
                     template_folder='templates',
                     static_folder = 'imagenes')

from .import routes
