from pdf2image import convert_from_path

def image_to_pdf():
    

    # PDF 파일 경로
    pdf_path = 'C:\\Users\\김영호\\Downloads\\cjpoc_\\일본법인\\신규\\20231204105223_0789502325'


    # PNG로 변환하고자 하는 페이지 범위 설정 (예: 첫 페이지만 변환)
    pages = convert_from_path(pdf_path, first_page=1, last_page=2)

    # 각 페이지를 이미지로 저장
    for i, page in enumerate(pages):
        page.save(f'C:\\Users\\김영호\\Downloads\\cjpoc_\\일본법인\\신규\\page_{i+1}.png', 'PNG')
        
    # 변환 완료 메시지 출력
    print("PDF to PNG conversion completed!")
