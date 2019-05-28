import os
from urllib import request
from imgurpython import ImgurClient
import timeit
import threading
from concurrent.futures import ThreadPoolExecutor

client_secret = os.getenv('CLIENT_SECRET')
client_id = os.getenv('CLIENT_ID')

client = ImgurClient(client_id, client_secret)


def download_image(image):
    """
    Function to download an image from a link provided.
    """
    link = image.link
    filename = link.split('/')[3].split('.')[0]
    fileformat = link.split('/')[3].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))
    print("{}.{} downloaded into downloads/ folder".format(filename, fileformat))


def download_album(album_id):
    images = client.get_album_images(album_id)
    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(download_image, images)


def main():
    download_album('PdA9Amq')


if __name__ == "__main__":
    print("Time taken to download images using multithreading: {}".format(timeit.Timer(main).timeit(number=1)))
