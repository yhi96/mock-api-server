import requests
import pytest

def test_get_list_of_inventory_devices():

    url = "http://localhost:8080/inventory/devices"

    response = requests.get(url)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"
    assert len(response.json()) > 0, "Response is not empty, it contains at least 1 element"

def test_add_new_device_to_inventory():

    url = "http://localhost:8080/inventory/devices"

    send_data = {

        "id": "TEST",
        "model": "TEST_DEVICE"
    }

    response = requests.post(url, json=send_data)

    assert response.status_code == 201, f"Response status code is not as expected, instead we got {response.status_code}"

    response_data = response.json()
    assert response_data.get("id"), "The response does not contain 'id'"
    assert response_data.get("model") == send_data["model"], "The device name in the response, does not match the created device name"

def test_add_device_to_inventory_without_populating_required_body():

    url = "http://localhost:8080/inventory/devices"

    send_data = {

        "id": "",
        "model": "",
        
    }

    response = requests.post(url, json=send_data)

    assert response.status_code == 400, f"Response status code is not as expected, instead we got {response.status_code}"

def test_update_existing_device():

    url = "http://localhost:8080/inventory/devices"

    updated_data = {

        "id": "TEST2",
        "model": "Updated_Device",
    }

    response = requests.put(url, json=updated_data)

    assert response.status_code == 201, f"Response status code is not as expected, instead we got {response.status_code}"

    response_data = response.json()
    assert response_data.get("model") == "Updated_Device", f"Expected status was 'Inactive', but instead we got {response_data['status']}"

def test_get_device_details_by_id():

    url = "http://localhost:8080/inventory/devices/TEST1"

    response = requests.get(url)

    assert response.status_code == 200, f"Response status code is not as expected, instead we got {response.status_code}"
    