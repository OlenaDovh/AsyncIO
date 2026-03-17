import asyncio
import aiohttp


async def fetch_content(url: str, session: aiohttp.ClientSession) -> str:
    """
    Asynchronously fetches the text content of a given URL.
    Args:
        url (str): The URL to fetch.
        session (aiohttp.ClientSession): The aiohttp session to use for the request.
    Returns:
        str: The content of the page or an error message if the request fails.
    """
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            content = await response.text()
            return f"Successfully fetched {url} ({len(content)} characters)"
    except aiohttp.ClientError as e:
        return f"Connection error for {url}: {e}"
    except asyncio.TimeoutError:
        return f"Timeout error for {url}"
    except Exception as e:
        return f"An unexpected error occurred for {url}: {e}"


async def fetch_all(urls: list[str]) -> None:
    """
    Fetches content from multiple URLs concurrently using a single session.
    Args:
        urls (list[str]): A list of URLs to fetch.
    Returns:
        None
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(url, session) for url in urls]

        print(f"Starting concurrent requests for {len(urls)} URLs...")
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)


urls_to_fetch = [
    "https://www.ukr.net/",
    "https://tsn.ua/",
    "https://web.telegrm.org/",
    "https://rozetka.com.ua/"
]

if __name__ == "__main__":
    asyncio.run(fetch_all(urls_to_fetch))
