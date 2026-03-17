import asyncio
import random


async def download_page(url: str) -> None:
    """
    Simulates downloading a web page with a random delay.
    Args:
        url (str): The URL of the page to "download".
    Returns:
        None
    """

    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)
    print(f"Page {url} downloaded in {delay:.2f} sec.")


async def main(urls: list) -> None:
    """
    Coordinates the concurrent downloading of multiple URLs.
    Args:
        urls (list): A list of strings representing the URLs to be downloaded.
    Returns:
        None
    """

    tasks = [download_page(url) for url in urls]

    print(f"Starting downloading {len(urls)} pages")
    await asyncio.gather(*tasks)
    print("All downloads completed!")


urls_to_load = [
    "https://rozetka.com.ua/",
    "https://www.ukr.net/",
    "https://tsn.ua/",
    "https://web.telegram.org/"
]

if __name__ == "__main__":
    asyncio.run(main(urls_to_load))
