from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("mcp-medium-accellerator")

@mcp.tool()
def extract_article_links(archive_url: str, limit: int = 10) -> list[str]:
    response = requests.get(archive_url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []

    for div in soup.find_all("article", attrs={"data-testid": "post-preview"}):
        for inner_div in div.find_all("div"):
            if inner_div.has_attr("data-href"):
                div_with_data_href = inner_div["data-href"]
                break
        if div_with_data_href:
            href = div_with_data_href
            if href not in links:
                links.append(href)
            if len(links) >= limit:
                break

    return links

@mcp.tool()
def extract_article_content_to_summarize(link: str) -> str:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    content = ""

    content = soup.find("article").get_text()

    return content