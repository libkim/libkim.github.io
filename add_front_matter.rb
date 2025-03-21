require 'yaml'
require 'fileutils'
require 'date'

# 디렉토리 내의 모든 .md 파일을 순회
Dir.glob("_my_posts/*.md").each do |post|
  # 파일 생성일 가져오기
  created_date = File.birthtime(post)

  # 파일 내용 읽기
  content = File.read(post)

  # 프론트 매터 추출
  front_matter, body = content.split(/---\s*\n/m, 3)[1..2]

  # 프론트 매터를 해시로 변환
  front_matter_hash = YAML.safe_load(front_matter, permitted_classes: [Date, Time])

  # 파일 생성일을 프론트 매터에 추가
  front_matter_hash['created-date'] = created_date

  # 수정된 프론트 매터와 본문을 결합
  new_content = front_matter_hash.to_yaml + "---\n\n" + body

  # 파일에 다시 쓰기
  File.write(post, new_content)

  # 로그 메시지 출력
  puts "Updated front matter for #{post}"
end
