import json

from flask import Flask, request
from m3u8_parser.parse_manifest import parse_manifest


app = Flask(__name__)


@app.route('/trim_manifest', methods=['POST'])
def trim_manifest():
    payload = json.loads(request.data)
    manifest = parse_manifest(payload['manifest_url'],
                              payload['start_time'],
                              payload['end_time'])
    return manifest
