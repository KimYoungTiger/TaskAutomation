import PyPDF2
import os

def split_pdf(file_path, output_directory):
    
    pathnow = os.path.abspath(__file__)
    
    # PDF 파일 열기
    pdf = PyPDF2.PdfReader(file_path)

    # 각 페이지를 개별 파일로 저장
    # for page_num in range(pdf.getNumPages()):
    for page_num in range(len(pdf.pages)):
        
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.addPage(pdf.getPage(page_num))

        # 출력 파일 이름 정의
        output_filename = f"{output_directory}/page_{page_num + 1}.pdf"

        # PDF 파일 작성
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print(f"Created: {output_filename}")

# 사용 예시
split_pdf("20231204094619_0342436271.pdf", os.path.abspath(__file__))

