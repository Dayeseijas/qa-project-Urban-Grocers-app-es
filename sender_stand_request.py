import configuration
import requests
import data
import json

# SOLICITUD PARA CREAR NUEVO USUARIO
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# SOLICITU PARA CREAR NUEVO KIT PARA EL USUARIO
def post_new_client_kit(name):
    if name is not None:
        name_json = {
            "name": name
        }
    else:
        name_json = {}
    user_body = data.user_body.copy()
    user_response = post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=name_json,
                         headers=headers)