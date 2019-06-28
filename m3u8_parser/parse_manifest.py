import requests
import m3u8


def get_manifest(url):
    response = requests.get(url)
    return response.text


def parse_manifest(manifest_url, start_time, end_time):
    parsed_manifest = m3u8.load(manifest_url)
    time_delta = 0
    selected_segments = []
    # extra_segments = []
    for segment in parsed_manifest.segments:
        time_delta += segment.duration
        if time_delta < start_time:
            continue
        if time_delta > end_time:
            break
        selected_segments.append(segment)
    parsed_manifest.segments.clear()
    for segment in selected_segments:
        segment.uri = segment.absolute_uri
        parsed_manifest.segments.append(segment)
    parsed_manifest.dump('trimmed.m3u8')
    return parsed_manifest.dumps()


if __name__ == '__main__':
    manifest_url = 'https://hssportsprepack.akamaized.net/' \
                   'videos/cricket/icccwc2019/22_06_2019/1260006910/' \
                   'eng/V2/master_Layer7.m3u8'
    parse_manifest(manifest_url, 75, 135)
