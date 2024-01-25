from pdf2image import convert_from_path
import fitz  # PyMuPDF
import os

def convert_pdf_to_image(pdf_path):

    # PDF전체 페이지를 PNG로 변환
    pages = convert_from_path(pdf_path)

    # 각 페이지를 이미지로 저장
    for i, page in enumerate(pages):
        page.save(f'page_{i+1}.png', 'PNG')


def convert_pdf_to_image(pdf_path, output_path=None):
    doc = fitz.open(pdf_path)
    directory_path = os.path.dirname(pdf_path)
    file_name = os.path.basename(pdf_path).split('.')[0]
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # 페이지 번호는 0부터 시작
        pix = page.get_pixmap()

        if output_path:
            output_filename = f"{output_path}/{file_name}_page_{page_num + 1}.png"
        else:
            output_filename = f"{directory_path}/{file_name}_page_{page_num + 1}.png"

        pix.save(output_filename)


if __name__ == "__main__":

    full_file_path = f"C:\\Users\\{os.environ.get('USERNAME')}\\Desktop\\test.pdf"   # 파일의 위치를 포함한 전체 경로 입력

    convert_pdf_to_image(full_file_path)

