import asyncio
import aiohttp
import os


async def download_image(url: str, filename: str, session: aiohttp.ClientSession) -> None:
    """
    Downloads an image from a URL and saves it to a file asynchronously.
    Args:
        url (str): The URL of the image to download.
        filename (str): The local path/name to save the image.
        session (aiohttp.ClientSession): The active session for HTTP requests.
    Returns:
        None
    """
    try:
        async with session.get(url, timeout=15) as response:
            if response.status == 200:
                content = await response.read()

                with open(filename, 'wb') as f:
                    f.write(content)
                print(f"Saved {url} to {filename} successfully")
            else:
                print(f"Failed to download {url}. Status {response.status}")

    except Exception as e:
        print(f"Error while downloading {url}: {e}")


async def main() -> None:
    """
    Coordinates the concurrent downloading of multiple images.
    Returns:
        None
    """
    os.makedirs("downloads", exist_ok=True)

    images = [
        ("https://unsplash.com/photos/T-FSAK4Bv9c/download?force=true",
         "image1.png"),
        ("https://extension.unh.edu/sites/default/files/styles/max_width_480px/public/migrated_images/trees.jpg?itok=b-gZXROM",
         "image2.jpeg"),
        ("https://assets.ithillel.ua/images/blog/cover/_transform_blogSplash_desktop_2x/Blog-OnAlgorithm.jpg",
         "image3.jpg")
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [
            download_image(url, name, session)
            for url, name in images
        ]

        print(f"Starting download of {len(tasks)} images")
        await asyncio.gather(*tasks)
        print("All downloads finished")


if __name__ == "__main__":
    asyncio.run(main())
