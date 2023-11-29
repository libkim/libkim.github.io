data/ani-list
-> 타이틀 한글명, 일본어명, 년도추가
-> 레이아웃/테이블.md 파일 없애기

posts/ani-list
-> 한<->일, 가나다<->년도 라디오 버튼 추가
-> 보고 있는 애니메이션 다른 색으로 표시 기능

data/tags
-> 정리

layouts/tag-generator
-> display: block에서 none => addclass hiding
-> display: none에서 block => addclass show
-> post 타이틀 아래 프로젝트 설명추가
-> 이미지 뷰 배경 색상 바꿀수 있는 기능과 비율을 알 수 있는 3×3자 래버트먼트자 기능
-> 이미지를 보며 태그를 쓸수 있게 반반 나눠서 스크롤 적용

div클래스는 css로 디자인하기 위함. composition-box-wrapper 와 같은 클래스명에서 composition은 무의미한 접두어임. 따라서 이런건 data-~=compositon으로 포함시키는게 맞다.
