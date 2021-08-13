import requests

file_name = input('Введите имя файла: ')
token = ''
path_to_file = str(input('Путь файла: '))

headers = {
    'content-type': 'application/json',
    'accept': 'application/json',
    'authorization': f'OAuth {uploader.token}'
}

params = {
    'path': file_name
}


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        request = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload',
                               params=params,
                               headers=headers)
        upload_url = request.json()['href']
        request.put(upload_url, headers=headers, files={'file': file_name})


uploader = YaUploader(token)
result = uploader.upload(path_to_file)
