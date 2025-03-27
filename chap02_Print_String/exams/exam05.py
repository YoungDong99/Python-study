'''
문5) 다음과 같은 2개의 파일 경로(path)를 대상으로 각각 파일명을 추출하여 출력하시오.

  <출력결과>
  파일명1: emp.xlsx
  파일명2: report.docx
  
'''

file_path1 = "/user/itwill/emp.xlsx"
file_name1 = file_path1.split('/')

file_path2 = "/home/user/documents/report.docx"
file_name2 = file_path2.split('/')


print("파일명 1:", file_name1[-1]) # 파일명: emp.xlsx
print("파일명 2:", file_name2[-1]) # 파일명: report.docx

