import get_links
import build_data
import time

def main(base_url, stem, filename, mode):
    urls = get_links.get_links(base_url, mode)
    for url in urls:
        url = stem + url
        data, metadata, raw_data = build_data.build_debate(url, mode)
        build_data.build_file(data, filename)
        build_data.build_file(metadata, "metadata_" + filename)
        build_data.build_file(raw_data, "raw_data_" + filename)
        time.sleep(1)
    build_data.zip_file("metadata_" + filename)
    build_data.zip_file("raw_data_" + filename)
    build_data.zip_file(filename)

if __name__ == "__main__":
    filename = 'debates_refined.jsonlist' 
    base_url = "https://www.presidency.ucsb.edu/documents/app-categories/elections-and-transitions/"
    stem = "https://www.presidency.ucsb.edu/"
    mode = "debates"

    main(base_url, stem, filename, mode)