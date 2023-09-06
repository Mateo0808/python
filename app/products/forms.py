from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

#FORMULARIO DE REGISTRO DE NUEVO PRODUCTO
class NewProductForm(FlaskForm):
    nombre = StringField(validators= [ InputRequired(message= "Este Campo No Puede Estar Vacio") ],
                        label= "Ingrese nombre:")
    precio = IntegerField("Ingrese su precio:" ,
                          validators=[
                                        InputRequired(
                                            message="Precio Requerido"
                                        ),
                                        NumberRange(
                                            message="precio fuera de rango",
                                            min = 1000,
                                            max = 10000
                                        )
                                    ])
    image = FileField(label= "Cargue la imagen de su producto: ",
                      validators = [
                          
                          FileRequired(
                              
                                    message = "Suba Una Imagen"

                                    ),
                          FileAllowed( 

                                        ["jpg", "png"],
                                        message = "Debes Selecionar El Tipo De Archivo Correcto (jpg, png, jpge)"

                           )
                        
                       ])
    submit = SubmitField ("Registrarse")


