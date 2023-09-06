from flask import render_template
from . import products
from .forms import NewProductForm
import app
import os

@products.route('/create' , 
                methods = ["GET" , "POST"] )
def crear_producto():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        #Llenar atributos
        #Del Objeto Producto
        #Con El Formulario
        form.populate_obj(p)
        #Registrar Producto En BD
        app.db.session.add(p)
        p.imagen = form.image.data.filename
        app.db.session.commit()
        #Trasladar La Imagen Cargada
        #a La Carpeta app/productos/imagen
        archivo = form.image.data
        archivo.save(   os.path.abspath(  
                                        
                                        os.getcwd() + 
                                    
                                        '/app/products/imagenes/' 
                                        
                                        + p.image)  )
        return os.getcwd()
    return render_template ('new.html',
                            form = form)


