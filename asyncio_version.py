import os
from imgurpython import ImgurClient
import timeit

import asyncio
import aiohttp

client_secret = os.getenv('CLIENT_SECRET')
client_id = os.getenv('CLIENT_ID')

client = ImgurClient(client_id, client_secret)


async def download_image(link, session):
    """
    Function to download an image from a link provided.
    """
    filename = link.split('/')[3].split('.')[0]
    fileformat = link.split('/')[3].split('.')[1]
    
    async with session.get(link) as response:
        with open("downloads/{}.{}".format(filename, fileformat), 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)
    
    print("{}.{} downloaded into downloads/ folder".format(filename, fileformat))


async def main():
    images = client.get_album_images('PdA9Amq')

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(image.link, session) for image in images]
 
        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = timeit.default_timer()

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())

    time_taken = timeit.default_timer() - start_time

    print("Time taken to download images using AsyncIO: {}".format(time_taken))
