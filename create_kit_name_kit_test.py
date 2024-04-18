import configuration
import pytest
import requests
import sender_stand_request
import data
import json

# PRUEBA 1
def test_name_field_match_one_caracter():
    # Definir los datos de prueba con el numero permitido de caracteres
    kit_body = {"name": "a"}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Extraer el cuerpo de la respuesta
    response_body = response.json()

    # Comprobar que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    assert response_body["name"] == kit_body[
        "name"], f"Expected 'name' field in response body to be '{kit_body['name']}', but got '{response_body['name']}'"

    # PRUEBA 2
def test_maximum_character_length():
    # Definir los datos de prueba con el nombre de longitud máxima
    name_max_length = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    kit_body = {"name": name_max_length}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Extraer el cuerpo de la respuesta
    response_body = response.json()

    # Comprobar que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    assert response_body["name"] == kit_body["name"], f"Expected 'name' field in response body to be '{kit_body['name']}', but got '{response_body['name']}'"

# PRUEBA 3
def test_empty_name_field():
    # Definir los datos de prueba con un nombre vacío
    kit_body = {"name": ""}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

# PRUEBA 4
def test_exceed_max_length_name_field():
    # Definir los datos de prueba con un nombre que excede la longitud máxima permitida
    name_exceed_max_length = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    kit_body = {"name": name_exceed_max_length}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

# PRUEBA 5
def test_special_characters_name_field():
    # Definir los datos de prueba con un nombre que contiene caracteres especiales
    kit_body = {"name": '"№%@"'}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Extraer el cuerpo de la respuesta
    response_body = response.json()

    # Comprobar que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    assert response_body["name"] == kit_body["name"], f"Expected 'name' field in response body to be '{kit_body['name']}', but got '{response_body['name']}'"

# PRUEBA 6
def test_spaces_in_name_field():
    # Definir los datos de prueba con un nombre que contiene espacios
    kit_body = {"name": " A Aaa "}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Extraer el cuerpo de la respuesta
    response_body = response.json()

    # Comprobar que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    assert response_body["name"] == kit_body["name"], f"Expected 'name' field in response body to be '{kit_body['name']}', but got '{response_body['name']}'"

# PRUEBA 7
def test_numbers_in_name_field():
    # Definir los datos de prueba con un nombre que contiene solo números
    kit_body = {"name": "123"}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Extraer el cuerpo de la respuesta
    response_body = response.json()

    # Comprobar que el campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
    assert response_body["name"] == kit_body["name"], f"Expected 'name' field in response body to be '{kit_body['name']}', but got '{response_body['name']}'"

# PRUEBA 8
def test_missing_parameter():
    # Definir los datos de prueba sin ingresar el parámetro
    kit_body = {}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

# PRUEBA 9
def test_parameter_type_mismatch():
    # Definir los datos de prueba con un tipo de parámetro diferente al esperado
    kit_body = {"name": 123}

    # Token de autenticación
    auth_token = "f06a72f0-553a-45dc-9a4b-d1c7c99fae03"

    # URL completa para la solicitud
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    # Cabeceras de la solicitud con el token de autenticación
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Realizar la solicitud POST con las cabeceras
    response = requests.post(url, json=kit_body, headers=headers)

    # Comprobar el código de respuesta
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"