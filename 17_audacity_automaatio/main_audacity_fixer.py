import argparse
import logging
import subprocess
import time
import tempfile

from pathlib import Path

from pipe_client import PipeClient

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


AUDACITY_NAME = "audacity.exe"
AUDACITY_PATH = Path(r"D:\Program Files\Audacity") / AUDACITY_NAME
FFMPEG_PATH = Path(r"G:\tools\ffmpeg-2022-01-06-git-2b541b8c1d-full_build\bin\ffmpeg.exe")


def process_exists(process_name):
    """original source: https://stackoverflow.com/a/29275361"""
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode(errors='ignore')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


class AudacityConnection:

    def __init__(self):
        app_name = AUDACITY_NAME
        audacity_path = AUDACITY_PATH
        if not process_exists(app_name):
            logger.warning("audacity.exe might not be running, trying to launch it")
            subprocess.Popen([audacity_path])
            time.sleep(5)
        self.client = PipeClient()

    def command(self, message, time_out=60):
        start = time.time()
        reply = self.client.write(message)
        while not reply:
            time.sleep(0.1)  # allow time for reply
            if time.time() - start > time_out:
                reply = 'PipeClient: Reply timed-out.'
            else:
                reply = self.client.read()
        logger.info(reply)


def extract_audio_tracks(file, tmpdir):
    number_of_audio_streams = 2  # this is where I need to know how many audio streams there are
    new_fns = []
    for i in range(number_of_audio_streams):
        new_fn = tmpdir / f"{file.stem}_{i}.mp3"
        new_fns.append(new_fn)
        cmd = f'"{FFMPEG_PATH}" -i "{file}" -map 0:a:{i} "{new_fn}"'
        logger.debug(cmd)
        subprocess.call(cmd)
    return new_fns


def replace_audio_track(video_file: Path, audio_file: Path):
    new_fn = video_file.with_name(f"{video_file.stem}_fixed.mp4")
    logger.info("Creating file: %s", new_fn)
    cmd = f'"{FFMPEG_PATH}" -i "{video_file}" -i "{audio_file}" -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 "{new_fn}"'
    logger.debug(cmd)
    subprocess.call(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", required=True)
    args = parser.parse_args()

    file = Path(args.filename)
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_files = extract_audio_tracks(file, Path(tmpdir))
        conn = AudacityConnection()
        for fn in audio_files:
            conn.command(f"""Import2: Filename="{fn}" """)

        conn.command("SelectAll")

        conn.command(f"""Macro_PythonVinkit:""")  # This needs to be installed (manually or with a script)
        new_fn = file.with_name(file.stem + "_fixed.mp3")
        conn.command("SelectAll")

        # Exports to a named file. This version of export has the full set of export options. However, a current
        # limitation is that the detailed option settings are always stored to and taken from saved preferences. The
        # net effect is that for a given format, the most recently used options for that format will be used. In the
        # current implementation, NumChannels should be 1 (mono) or 2 (stereo).
        conn.command(f"""Export2: Filename="{new_fn}" NumChannels=2 """)

        replace_audio_track(file, new_fn)
        conn.command("SelectAll")
        # conn.command("RemoveTracks")


if __name__ == '__main__':
    main()
