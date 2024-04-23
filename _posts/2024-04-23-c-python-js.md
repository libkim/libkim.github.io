파이썬
1. 인터프리트 방식
2. 객체 지향 프로그래밍 언어
3. 동적 타입 언어
4. 자동 메모리 관리
5. 
5-1. num1 = 42
     num2 = 0b101010
     num3 = 0o52
     num4 = 0x2a
5-2. str1 = "\"How are you?\"\n\"I'm fine.\""
     str2 = '"How are you?"\n"I\'m fine."'
     str3 = '''"How are you?"
       "I\'m fine."'''
5-3. numbers = [[1, 3, 5], [2, 4]]
     odd_list1 = numbers[0]
     odd_list2 = numbers[0][0:3]
     odd_list3 = [numbers[0][0], numbers[0][1], numbers[0][2]]
     odd_list4 = numbers[-2]
     odd_list5 = numbers[-2][-3:]
     odd_list6 = [numbers[-2][-3], numbers[-2][-2], numbers[-2][-1]]
     odd_list7 = numbers[0][2::-1][::-1]
     odd_list8 = [numbers[0][2], numbers[0][1], numbers[0][0]][::-1]
5-4. num1 = int(input('첫 번째 정수 입력 >> '))
     num2 = int(input('두 번째 정수 입력 >> '))
     print('평균:', (num1 + num2) / 2)


C
1. 컴파일 방식
2. 절차적 프로그래밍 언어
3. 정적 타입 언어
4. 수동 메모리 관리
5-1. int num1 = 42;
     int num2 = 0b101010;
     int num3 = 052;
     int num4 = 0x2a;
5-2. char *str = "\"How are you?\"\n\"I'm fine.\"";
5-3. int numbers[2][3] = {{1, 3, 5}, {2, 4, 0}};
     int odd_list[3] = {numbers[0][0], numbers[0][1], numbers[0][2]};
5-4. int num1, num2;
     printf("첫 번째 정수 입력 >> ");
     scanf("%d", &num1);
     printf("두 번째 정수 입력 >> ");
     scanf("%d", &num2);
     printf("평균: %f\n", (num1 + num2) / 2.0);


자바스크립트
1. 인터프리트 방식
2. 객체 지향 프로그래밍 언어
3. 동적 타입 언어
4. 자동 메모리 관리
5-1. let num1 = 42;
     let num2 = 0b101010;
     let num3 = 0o52;
     let num4 = 0x2a;
5-2. let str1 = "\"How are you?\"\n\"I'm fine.\"";
     let str2 = '"How are you?"\n"I\'m fine."';
     let str3 = `"How are you?"
       "I'm fine."`;
5-3. let numbers = [[1, 3, 5], [2, 4]];
     let oddList1 = numbers[0];
     let oddList2 = numbers[0].slice(0, 3);
     let oddList3 = [numbers[0][0], numbers[0][1], numbers[0][2]];
     let oddList4 = numbers[-2];
     let oddList5 = numbers[-2].slice(-3);
     let oddList6 = [numbers[-2][-3], numbers[-2][-2], numbers[-2][-1]];
     let oddList7 = [...numbers[0]].reverse().slice(0, 3).reverse();
     let oddList8 = [numbers[0][2], numbers[0][1], numbers[0][0]].reverse();
5-4. let num1 = parseInt(prompt('첫 번째 정수 입력 >> '));
     let num2 = parseInt(prompt('두 번째 정수 입력 >> '));
     console.log('평균:', (num1 + num2) / 2);




|분류|파이썬|C|자바스크립트|
|---|---|----|--------------|
|숫자형         |int, float, complex         |int, float, double, short, long, unsigned 등            |Number, BigInt|
|문자열형       |str                         |char, char[]                                            |String        |
|불린형         |bool                        |_Bool (C99부터), int (0 또는 1로 표현)                  |Boolean       |
|시퀀스형       |list, tuple, range          |배열 (고정 크기)                                        |Array         |
|매핑형         |dict                        |구조체(struct)로 매핑 가능                              |Object        |
|세트형         |set, frozenset              |없음                                                    |Set, WeakSet  |
|파일           |파일 입출력 (open)          |파일 입출력 (fopen, fclose 등)                          |Blob/File (브라우저 환경)|
|None/Null      |None                        |NULL                                                    |null, undefined|
|날짜와 시간    |datetime 모듈               |time.h 라이브러리 등                                    |Date           |
|바이너리 데이터|bytes, bytearray, memoryview|없음 (직접 관리 필요)                                   |ArrayBuffer, TypedArray
