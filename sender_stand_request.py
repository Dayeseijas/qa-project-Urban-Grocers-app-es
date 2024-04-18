import configuration
import requests
import data
import json

# SOLICITUD PARA CREAR NUEVO USUARIO
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json={
  "firstName": "Daye",
  "phone": "+11234567890",
  "address": "123 Elm Street, Hilltop"
},
                         headers={"Content-Type": "application/json"})  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# SOLICITUD PARA CREAR KIT PERSONAL DE USUARIO
def post_new_client_kit(username, authtoken, cardId, name):
    # URL de la API para crear el kit personal
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Datos del kit personal a enviar
    data = {
        "usuario": username,
        "cardId": cardId,
        "name": name
    }

    # Encabezado con el token de autorización
    headers = {
        "Authorization": authtoken,
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con los datos y el encabezado
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Verificar el estado de la respuesta
    if response.status_code == 201:
        print("Kit personal creado exitosamente para el usuario", username)
        print(response.json())
    else:
        print("Error al crear el kit personal:", response.text)

# Datos de usuario
username = "Daye"
authtoken = "mi_token_de_autorizacion"
cardId = 1
name = "MiKitPersonal"

# Llamar a la función para crear el kit personal
post_new_client_kit(username, authtoken, cardId, name)