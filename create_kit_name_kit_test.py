import configuration
import pytest
import requests
import sender_stand_request
import data

# FUNCIÓN PARA PRUEBA POSITIVA
def positive_assert(name):
    kit_response = sender_stand_request.post_new_client_kit(name)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# FUNCIÓN PARA PRUEBA NEGATIVA
def negative_assert_code_400(name):
    kit_response = sender_stand_request.post_new_client_kit(name)
    assert kit_response.status_code == 400

# PRUEBA 1
def test_one_character_field():
    positive_assert(data.one_character)

# PRUEBA 2
def test_maximum_character_length():
    positive_assert(data.maximum_character_length)

# PRUEBA 3
def test_empty_name_field():
    negative_assert_code_400(data.empty_name_field)

# PRUEBA 4
def test_exceed_max_length_name_field():
    negative_assert_code_400(data.exceed_max_length_name_field)

# PRUEBA 5
def test_special_characters_name_field ():
    positive_assert(data.special_characters_name_field)

# PRUEBA 6
def test_spaces_in_name_field ():
    positive_assert(data.spaces_in_name_field)

# PRUEBA 7
def test_numbers_in_name_field():
    positive_assert(data.numbers_in_name_field)
# PRUEBA 8
def test_missing_parameter():
    negative_assert_code_400(data.missing_parameter)

# PRUEBA 9
def test_parameter_type_mismatch():
    negative_assert_code_400(data.parameter_type_mismatch)
