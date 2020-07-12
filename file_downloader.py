import os
import requests
import shutil


def downloader(directory_name='downloads'):
    # generate directory for downloads
    base_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(base_dir, directory_name)
    os.makedirs(download_dir, exist_ok=True)

    # recursive function to download files from a list of urls
    def download_files(urls=[], index=0):
        if len(files) == index:
            return True

        current_url = files[index]
        filename = os.path.basename(current_url)
        filename_directory = os.path.join(download_dir, filename)

        with requests.get(current_url, stream=True, headers={'User-Agent': 'custom_header'}) as request:
            with open(filename_directory, 'wb') as file_object:
                shutil.copyfileobj(request.raw, file_object)

        return download_files(urls, index + 1)

    return download_files


if __name__ == "__main__":
    files = []
    for f in range(0, 10):
        url = f"https://pokeres.bastionbot.org/images/pokemon/{f + 1}.png"
        files.append(url)

    file_downloader = downloader()
    is_complete = file_downloader(urls=files)

    # currying shape function
    # file_downloader = downloader('pokemones')(urls=files)

    if is_complete:
        print('Success downloads!')
    else:
        print('Somenting went wrong!')
