import subprocess

# Inicia o subprocesso em background
subprocess.Popen(['python', '-c', 'import requests; requests.get(\"https://si-activities-api.onrender.com/api/activities\")'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
print('Requisição enviada.')
