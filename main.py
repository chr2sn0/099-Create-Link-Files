import os


def create_linux_link_file(root, listing_id):
    print(f'[linux] root: {root}, filename: {listing_id}')
    desktop_file_name = f'{root}/pdp.desktop'
    print(f'[linux] desktop_file_name: {desktop_file_name}')

    fh = open(desktop_file_name, "w+")
    fh.write(f"""[Desktop Entry]
Icon=text-html
Name=pdp
Type=Link
URL[$e]=https://www.etsy.com/de/listing/{listing_id}""")
    fh.close()

    return True if os.path.isfile(desktop_file_name) else False


def create_win_link_file(root, listing_id):
    print(f'[win] root: {root}, filename: {listing_id}')
    url_file_name = f'{root}/pdp.url'
    print(f'[win] url_file_name: {url_file_name}')

    fh = open(url_file_name, "w+")
    fh.write(f"""[{{000214A0-0000-0000-C000-000000000046}}]
Prop3=19,11
[InternetShortcut]
IDList=
URL=https://www.etsy.com/de/listing/{listing_id}""")
    fh.close()

    return True if os.path.isfile(url_file_name) else False


def create_link_files(root, listing_id, ext):
    if create_linux_link_file(root, listing_id) and create_win_link_file(root, listing_id):
        if os.path.isfile(f'{root}/{listing_id}{ext}'):
            os.remove(f'{root}/{listing_id}{ext}')
        else:
            raise ValueError(f'Can\'t remove {root}/{listing_id}{ext}. Not found.')
    else:
        raise ValueError('Error creating link_files.')


def get_all_filepaths(root_path, ext):
    all_files = []
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            if filename.lower().endswith(ext):
                create_link_files(root, str.removesuffix(filename, ext), ext)
                all_files.append(os.path.join(root, filename))
    return all_files


get_all_filepaths(os.environ.get('PATH_IN_DATA_TO_SEARCHFOLDER'), '.pdp')
