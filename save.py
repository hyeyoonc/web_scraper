import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w")
  # jobs.csv라는 csv파일 만들기 mode = "w"는 쓰기만 가능 
  writer = csv.writer(file)
  writer.writerow(["title","company","location","link"])
  # 파일에 정보 입력 
  for job in jobs:
    writer.writerow(list(job.values()))
    # values는 딕셔너리안의 값만 가져오기,딕셔너리는 type이 string이 아니기 때문에 list로 변환해야함
  return 