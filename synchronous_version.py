import os
from urllib import request
from imgurpython import ImgurClient
import timeit

client_secret = os.getenv('CLIENT_SECRET')
client_id = os.getenv('CLIENT_ID')

client = ImgurClient(client_id, client_secret)


def download_image(link):
    """
    Function to download an image from a link provided.
    """
    filename = link.split('/')[3].split('.')[0]
    fileformat = link.split('/')[3].split('.')[1]
    request.urlretrieve(link, "downloads/{}.{}".format(filename, fileformat))
    print("{}.{} downloaded into downloads/ folder".format(filename, fileformat))


def main():
    images = client.get_album_images('PdA9Amq')
    for image in images:
        print(image.link)
        download_image(image.link)


if __name__ == "__main__":
    print("Time taken to download images synchronously: {}".format(timeit.Timer(main).timeit(number=1)))
