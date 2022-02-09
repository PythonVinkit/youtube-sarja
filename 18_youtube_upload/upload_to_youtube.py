import json
import logging
import json
import requests
from pathlib import Path
import requests

from pathlib import Path
from . import REFRESH_TOKEN

logger = logging.getLogger(__name__)


# https://developers.google.com/youtube/v3/guides/uploading_a_video
# https://xirtam.cxumol.com/upload-videos-to-youtube-brand-account-via-low-level-api/
# pip install google-api-python-client


creds_path = Path(r"C:\Users\Juhani Takkunen\Downloads\client_secret_898148648671-q16c86jc22uq15q7jdqaq3h467eln81n.apps.googleusercontent.com(1).json")


class Client:

    def __init__(self):
        self._access_token = self._get_access_token()

    def _get_access_token(self):

        creds = json.loads(creds_path.read_bytes())["web"]

        payload = {
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "refresh_token": REFRESH_TOKEN,
            "grant_type": "refresh_token"
        }
        r = requests.post("https://oauth2.googleapis.com/token", data=payload)
        r.raise_for_status()
        res = r.json()
        return res["access_token"]

    def get_upload_url(self, file_to_upload: Path, part_name: str):

        payload = {
            "snippet": {
                "title": part_name,
                "description": part_name,
                "tags": ["PythonVinkit", "Python", "Youtube"],
                "categoryId": 27  # Education, https://gist.github.com/dgp/1b24bf2961521bd75d6c
            },
            "status": {
                "privacyStatus": "private",
                "embeddable": True,
                "license": "youtube"
            }
        }
        payload = json.dumps(payload)
        headers = {
            "authorization": "Bearer " + self._access_token,  # Got before
            # "content-length": str(len(payload)), # not a necessary field
            "content-type": "application/json; charset=utf-8",
            "x-upload-content-length": str(Path(file_to_upload).stat().st_size),
            "X-Upload-Content-Type": "application/octet-stream"
        }
        r = requests.post(
            "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status,contentDetails",
            data=payload, headers=headers)
        r.raise_for_status()
        upload_url = r.headers["Location"]
        return upload_url

    def _upload_full(self, file_to_upload, part_name):
        file_size = Path(file_to_upload).stat().st_size
        upload_url = self.get_upload_url(file_to_upload, part_name)

        up_file_headers = {
            "authorization": "Bearer " + self._access_token,
            "Content-Length": str(file_size),
            "Content-Type": "application/octet-stream"
        }
        r = requests.put(upload_url, data=file_to_upload.read_bytes(), headers=up_file_headers)
        r.raise_for_status()

    def upload_in_chunks(self, file_to_upload: Path, part_name: str):
        file_size = Path(file_to_upload).stat().st_size
        upload_url = self.get_upload_url(file_to_upload, part_name)

        def read_in_chunks(file_object, chunk_size=32 * 1024 * 1024):  # or your favorite chunk size
            while True:
                data = file_object.read(chunk_size)
                if not data:
                    break
                yield data

        first_byte, last_byte = 0, 0

        with file_to_upload.open('rb') as f:
            for chunk in read_in_chunks(f):
                last_byte = first_byte + len(chunk) - 1
                up_file_headers = {
                    "authorization": "Bearer " + self._access_token,
                    "Content-Length": str(len(chunk)),
                    "Content-Range": f"bytes {first_byte}-{last_byte}/{file_size}",
                    "Content-Type": "application/octet-stream"
                }
                try:
                    r = requests.put(upload_url, data=chunk, headers=up_file_headers)
                    print(f"r: {r}, Content-Range: {up_file_headers['Content-Range']}")
                    r.raise_for_status()
                    first_byte = last_byte + 1
                except Exception as e:
                    # your custom error handling
                    raise e


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    Client().upload_in_chunks(
        file_to_upload=Path(r"D:\PythonVinkit\raw_recordings\2022-01-12 17-26-12_fixed.mp4"),
        part_name="Osa18b"
    )
