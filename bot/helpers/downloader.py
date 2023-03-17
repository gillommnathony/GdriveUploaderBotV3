import os
import wget
import glob
import youtube_dl
from pySmartDL import SmartDL
from urllib.error import HTTPError
from youtube_dl import DownloadError
from bot import DOWNLOAD_DIRECTORY, LOGGER
from pytube import YouTube


def download_file(url, dl_path):
  try:
    dl = SmartDL(url, dl_path, progress_bar=False)
    LOGGER.info(f'Downloading: {url} in {dl_path}')
    dl.start()
    return True, dl.get_dest()
  except HTTPError as error:
    return False, error
  except Exception as error:
    try:
      filename = wget.download(url, dl_path)
      return True, os.path.join(f"{DOWNLOAD_DIRECTORY}/{filename}")
    except HTTPError:
      return False, error

def download_fb(url, dl_path):
  try:
    filename = wget.download(url, dl_path)
    return True, os.path.join(f"{DOWNLOAD_DIRECTORY}/{filename}")
  except HTTPError as error:
    return False, error

def utube_dl(link):
    ytdl_opts = {
        'outtmpl' : os.path.join(DOWNLOAD_DIRECTORY, '%(title)s'),
        'noplaylist' : True,
        'logger': LOGGER,
        'format': 'bestvideo+bestaudio/best',
        'geo_bypass_country': 'IN',
        'verbose': True
    }
    try:
        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
            meta = ytdl.extract_info(link, download=True)
            for path in glob.glob(os.path.join(DOWNLOAD_DIRECTORY, '*')):
                if path.endswith(('.avi', '.mov', '.flv', '.wmv', '.3gp','.mpeg', '.webm', '.mp4', '.mkv')) and \
                        path.startswith(ytdl.prepare_filename(meta)):
                    return True, path
    except DownloadError as e:
        print(str(e))
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream is None:
            return False, 'No video file exists on server'
        else:
            stream.download(DOWNLOAD_DIRECTORY)
            return True, os.path.join(DOWNLOAD_DIRECTORY, stream.default_filename)
    except Exception as e:
        return False, str(e)
