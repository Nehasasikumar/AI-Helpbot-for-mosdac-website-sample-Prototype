from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests, os, re, json
from urllib.parse import urljoin, urlparse

visited = set()
output = []

# Create directories
os.makedirs("data/images", exist_ok=True)
os.makedirs("data/pdfs", exist_ok=True)

def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()

def is_mission_link(href):
    return re.match(r"^/(insat|scatsat|meghatropiques|resourcesat|cartosat)[\w\-]*$", href)

def extract_data_from_page(url):
    print(f"🔍 Crawling: {url}")
    try:
        response = requests.get(url, timeout=10)
        if not response.ok:
            return
        soup = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        print(f"❌ Failed to load {url}: {e}")
        return

    text = clean_text(soup.get_text())

    # Extract images
    images = []
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            img_url = urljoin(url, src)
            img_name = os.path.basename(img_url.split("?")[0])
            images.append(img_name)
            try:
                img_data = requests.get(img_url).content
                with open(os.path.join("data/images", img_name), "wb") as f:
                    f.write(img_data)
            except:
                pass

    # Extract PDFs
    pdfs = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        if href.endswith(".pdf"):
            pdf_url = urljoin(url, href)
            pdf_name = os.path.basename(pdf_url)
            pdfs.append(pdf_name)
            try:
                pdf_data = requests.get(pdf_url).content
                with open(os.path.join("data/pdfs", pdf_name), "wb") as f:
                    f.write(pdf_data)
            except:
                pass

    output.append({
        "url": url,
        "text": text,
        "images": images,
        "pdfs": pdfs
    })

def crawl_missions_with_selenium(start_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(start_url)
    driver.implicitly_wait(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "lxml")

    mission_links = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        if is_mission_link(href):
            full_url = urljoin(start_url, href)
            if full_url not in visited:
                visited.add(full_url)
                mission_links.append(full_url)

    driver.quit()
    return mission_links

# === Main ===
if __name__ == "__main__":
    start_url = "https://www.mosdac.gov.in"
    mission_pages = crawl_missions_with_selenium(start_url)

    # Add FAQ page manually
    faq_url = "https://www.mosdac.gov.in/faq-page"
    if faq_url not in visited:
        visited.add(faq_url)
        mission_pages.insert(0, faq_url)

    print(f"\n✅ Found {len(mission_pages)} pages (missions + FAQ).")

    for link in mission_pages[:6]:  # Limit to 5 missions + 1 FAQ
        extract_data_from_page(link)

    with open("data/mosdac_missions.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("\n✅ Data saved to data/mosdac_missions.json")
