import get_data
import get_links
import time

def main(base_url, stem, filename):
    urls = get_links.get_links(base_url, "debates")
    for url in urls:
        url = stem + url
        data, metadata = get_data.parse_debate(url)
        get_data.build_file(data, filename)
        get_data.build_file(metadata, "metadata_" + filename)
        time.sleep(1)

if __name__ == "__main__":
    filename = 'debates.jsonlist'
    base_url = "https://www.presidency.ucsb.edu/documents/app-categories/elections-and-transitions/"
    stem = "https://www.presidency.ucsb.edu/"

    main(base_url, stem, filename)