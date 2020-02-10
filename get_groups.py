import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

GROUPS = {
    '9К9191', '9К9091', '9К9291', '9К9111', '8К1191', '8К1591', '8К1391', '9К9391', '9К9392', '9К9393', '9К9394',
    '9К9311', '8К2491', '8К2492', '8К2493', '8К2411', '7К2491', '7К2492', '7К2493', '9К9591', '9К9491', '8К3791',
    '8К3291', '8К1111', '7К1191', '7К1591', '7К1391', '7К1111', '61191', '61591', '61391', '7К2411', '62493', '62492',
    '62491', '7К3791', '7К3291', '63791', '63291'
}


def extract_text_by_page(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(pdf_path):
    test = {}
    i = -1
    for page in extract_text_by_page(pdf_path):
        i += 1
        page_groups = tuple(set(page.split(' ')) & GROUPS)
        test.update({page_groups: f"images/{i}.jpeg"})

    users_images_full = {
        group.lower(): value for key, value in test.items() for group in key
    }
    return users_images_full
