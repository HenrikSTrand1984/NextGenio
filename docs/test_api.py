import requests

# Test for ClickUp API
def test_clickup_api():
    url = "https://api.clickup.com/api/v2/task/TASK_ID"  # Sett inn riktig Task ID
    headers = {
        "Authorization": "your_clickup_api_key",  # Sett inn din ClickUp API-nøkkel
        "Content-Type": "application/json"
    }
    data = {
        "status": "complete"
    }
    
    response = requests.put(url, json=data, headers=headers)
    
    # Test for å sjekke at svaret er OK
    assert response.status_code == 200  # Sjekk at vi fikk en OK status (200)
    assert "complete" in response.json()["status"]  # Sjekk at status ble oppdatert

# Test for OpenAI API
def test_openai_api():
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": "Bearer your_openai_api_key",  # Sett inn din OpenAI API-nøkkel
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": "Write a short summary of the current build process.",
        "max_tokens": 50
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    # Test for å sjekke at svaret er OK
    assert response.status_code == 200  # Sjekk at vi fikk en OK status (200)
    assert "choices" in response.json()  # Sjekk at OpenAI sendte et svar

# Test for Supabase API (for databaseoperasjoner)
def test_supabase_api():
    url = "https://your-project.supabase.co/rest/v1/your_table"
    headers = {
        "Authorization": "Bearer your_supabase_api_key",  # Sett inn din Supabase API-nøkkel
        "Content-Type": "application/json"
    }
    data = {
        "column_name": "value"
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    # Test for å sjekke at svaret er OK
    assert response.status_code == 200  # Sjekk at vi fikk en OK status (200)
    assert "id" in response.json()  # Sjekk at et nytt element ble lagt til
