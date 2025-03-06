import requests

# Replace 'base64_image_data' with a valid base64-encoded string of an image
base64_image_data = 'iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4' \
                    '//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='

response = requests.post('http://127.0.0.1:5000/recommend', json={'image': base64_image_data})
print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.content}")
assert response.status_code == 200
data = response.json()
print(data)
assert 'emotion' in data
assert 'weather' in data
assert 'playlists' in data
