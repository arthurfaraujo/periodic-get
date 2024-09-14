import request

def make_request():
  response = request.get("https://si-activities-api.onrender.com/api/activities")
  print(response.status_code, response.text)

if __name__ == "__main__":
  make_request()
