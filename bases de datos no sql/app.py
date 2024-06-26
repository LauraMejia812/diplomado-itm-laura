import boto3


#conectar base de datos 

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-laura-mejia')

#consulta por clave primaria
response = tabla.get_item(Key={'id':'1'})

#imprimir el item consultado
print(response['Item'])

# imprimir todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])


#insertar un registro en la tabla 
new_item = {
    "id": "3", 
    "nombre": "pepito",
    "direccion": "calle 10 norte"
    
}

#insertar el elemento en la tabla
tabla.put_item(Item=new_item)
   
print("Elemento insertado con éxito:")
    

# imprimir todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])


# modificar atributo de un registro existente

primary_key_value = '2'

# Nuevos valores para actualizar
update_expression = "SET nombre = :val1"
expression_attribute_values = {
    ':val1': 'pepita'
}

print("Elemento actualizado con éxito:")
# imprimir todos los elementos de la tabla
response = tabla.scan()

print(response['Items'])