import json
import requests
import sys
import subprocess

#Constantes
REQUEST_COMMAND_LS_LA = 'http://localhost:8000/command/'
POST_COMMAND_OUTPUT_LS_LA = 'http://localhost:8000/command/command_output/'
OUTPUT_FILENAME = "command_output"

#Enviar requisicao
request_response = requests.get(REQUEST_COMMAND_LS_LA)

if request_response.status_code != 200:
    print("Request status code is not 200. Exiting.")
    sys.exit(1)

#Decodificar JSON
decoded_command = json.loads(request_response.text)

#Executar comando
output_file = open(OUTPUT_FILENAME, 'w')
subprocess.call([decoded_command['command'], decoded_command['options']], stdout=output_file)
output_file.close()

print("Comando executado!")

#Fazer upload do arquivo contendo a saida do comando
with open(OUTPUT_FILENAME, 'r') as output_file:
    request_header = {'enctype': 'multipart/form-data'}
    post_request = requests.post(POST_COMMAND_OUTPUT_LS_LA, data=output_file, headers =request_header)

