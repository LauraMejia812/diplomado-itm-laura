import boto3

# Configura el cliente de DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Asegúrate de especificar la región correcta

# Nombre de la tabla a crear
table_name = 'tabla-laura-mejia-2'

# Esquema de la tabla (definición de atributos y claves)
table_definition = {
    'TableName': table_name,
    'KeySchema': [
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  
        },
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'id',
            'AttributeType': 'S'  
        },
       
    ],
    'BillingMode': 'PAY_PER_REQUEST'  # Modo de capacidad bajo demanda
}
