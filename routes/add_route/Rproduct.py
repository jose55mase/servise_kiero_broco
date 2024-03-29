#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar

from app.services.Sproducts import Sproducts
from app.models.Mproduct import ModelProduct

import json
import time
import collections


#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios
# from app.services.connect_to_mysql import mysql


class Rproduct(resource):

    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass
    # Se optiene la lista de productos
    def get(self):
        objectoJson = {'Mensaje':None,'Resultados':[]}
        try:
            retorno = Sproducts().GET_ALL_PRODUCTS()
            listaJson = json.dumps(retorno)
            jsonTemplate = response(listaJson,status=200, mimetype='application/json')
            jsonTemplate.headers['Access-Control-Allow-Origin'] = '*'
            print("Process select OK")
            return jsonTemplate
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500

    # Se edita o  Inserta un registro
    def post(self, *args, **kwargs):
        try:
            methdPost = request.get_json()# Datos de entrada
            
            if len(methdPost) >= 7:
                # Capos requerido                
                if 'Product_id' in methdPost:
                    methdPost['Product_id']                
                else:
                    methdPost.setdefault("Product_id",-1)
                Categoria_id=methdPost["Categoria_id"]
                Titulo= methdPost["titulo"]
                Estado = methdPost["Estado"]
                Descripcion= methdPost["Descripcion"]                
                Creado_Por= methdPost["Creado_Por"]
                Modificado_Por= methdPost["Modificado_Por"]
                Fecha_Creacion= methdPost["Fecha_Creacion"]
                Fecha_Actualizacion = methdPost["Fecha_Actualizacion"]                
                Producto_Id = methdPost["Product_id"]
                #Campos opcionales
                Precio=methdPost['Precio']
                Precio_Descuento=methdPost['Precio_Descuento']
                #,Stock_Actual =methdPost['Stock_Actual']
                #,Stock_Limite=methdPost['Stock_Limite']
                Peso=methdPost['Peso']
                Alto=methdPost['Alto']
                Largo=methdPost['Largo']
                Ancho=methdPost['Ancho']
                Color=methdPost['Color']
                Talla=methdPost['Talla']
                SKU=methdPost['SKU']
                print(" UPDATE ",methdPost['SKU'])
                #,informacion=informacion
                Imagenes_1=methdPost["Imagenes_1"]
                #,Imagenes_2=Imagenes_2
                #,Imagenes_3=Imagenes_3
                #,Imagenes_4=Imagenes_4
                #,Imagenes_5=Imagenes_5
                #,Imagenes_6=Imagenes_6
                #,Imagenes_7=Imagenes_7
                print("Esta es la Imagenes_1",Imagenes_1)
                # Actualizar
                if int(methdPost['Product_id']) > 0  :
                    print(" UPDATE ")
                    Sproducts(
                        Producto_Id = Producto_Id
                        ,Categoria_id=Categoria_id
                        ,Titulo=Titulo
                        ,Descripcion=Descripcion
                        ,Estado=Estado
                        ,Creado_Por=Creado_Por
                        ,Modificado_Por=Modificado_Por
                        ,Fecha_Creacion=Fecha_Creacion
                        ,Fecha_Actualizacion =Fecha_Actualizacion
                        ,Precio=Precio
                        ,Precio_Descuento=Precio_Descuento
                        #,Stock_Actual = Stock_Actual
                        #,Stock_Limite=Stock_Limite                                           
                        ,Peso=Peso
                        ,Alto=Alto
                        ,Largo=Largo
                        ,Ancho=Ancho
                        ,Color=Color
                        ,Talla=Talla   
                        ,SKU=SKU                        
                        #,Imagenes_1=Imagenes_1
                        #,Imagenes_2=Imagenes_2
                        #,Imagenes_3=Imagenes_3
                        #,Imagenes_4=Imagenes_4
                        #,Imagenes_5=Imagenes_5
                        #,Imagenes_6=Imagenes_6
                        #,Imagenes_7=Imagenes_7

                    ).UPDATE_PRODUCT()
                    return{'Mensaje':'Producto  actualizado'}
                else:
                # Insertar                    
                    print(" INSERT ")                    
                    Sproducts(
                        Producto_Id = Producto_Id
                        ,Categoria_id=Categoria_id
                        ,Titulo=Titulo
                        ,Descripcion=Descripcion
                        ,Estado=Estado
                        ,Creado_Por=Creado_Por
                        ,Modificado_Por=Modificado_Por
                        ,Fecha_Creacion=Fecha_Creacion
                        ,Fecha_Actualizacion =Fecha_Actualizacion
                        ,Precio=Precio
                        ,Precio_Descuento=Precio_Descuento
                        #,Stock_Actual = Stock_Actual
                        #,Stock_Limite=Stock_Limite                                           
                        ,Peso=Peso
                        ,Alto=Alto
                        ,Largo=Largo
                        ,Ancho=Ancho
                        ,Color=Color
                        ,Talla=Talla   
                        ,SKU=SKU                        
                        #,Imagenes_1=Imagenes_1
                        #,Imagenes_2=Imagenes_2
                        #,Imagenes_3=Imagenes_3
                        #,Imagenes_4=Imagenes_4
                        #,Imagenes_5=Imagenes_5
                        #,Imagenes_6=Imagenes_6
                        #,Imagenes_7=Imagenes_7                        
                    ).INSERT_PRODUCT()
                    return{'Mensaje':'Producto  Insertado'}
            else:
                print(" Campos incompletos ")
                return{'Mensaje':'Campos incompletos'}
        except Exception as error:
            print(error)
            return {'Mensaje':'Problema interno'},500

    # Pausar
    def put(self):
        try:
            methdPost = request.get_json()
            Producto_Id = methdPost['Product_id']
            Estado = methdPost["Estado"]
            Sproducts(
                Producto_Id = Producto_Id,
                Estado=Estado
            ).STOP_PRODUCT()
            print("Producto a cambiado de estado")
            return{'Mensaje':'Producto a cambiado de estado'}

        except Exception as error:
            print(error)
            return {'Mensaje':'Problema interno'},500

    
    def delete(self, *args, **kwargs):
            try:
                methdPost = request.get_json()
                Producto_Id = methdPost['Product_id']
                Sproducts(
                    Producto_Id = Producto_Id
                ).DELETE_PRODUCT()
                print("Producto eliminado ( estado = 1 )")
                return{'Mensaje':'Producto  Eliminado'}
            except Exception as error:
                print(error)
                return {'Mensaje':'Problema interno'},500
