# djangoToy
장고 게시판 토이프로젝트

*****
* bootstrap(dark) : 3.3.2v
* python : 3.9.5 64-bit
* django : 3.2.6
*****


```
1. 가상환경 세팅
python -m venv board

2. 가상환경에 장고 설치
pip install django

3. 장고 프로젝트 생성
django-admin startproject hee

4. 앱 추가
python manage.py startapp board
** 추가한 앱은 settings.py의 INSTALLED_APPS에 등록해주어야 한다.


데이터베이스 구조가 구성되어 있지 않을 경우 아래와 같은 오류 발생
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.    
Run 'python manage.py migrate' to apply them.
>python manage.py makemigrations  * 변경사항 마이그레이션 파일로 생성
>python manage.py migrate         * 변경된 마이그레이션 적용

5. 슈퍼 유저 생성
python manage.py createsuperuser

```
*****
## 하다가 막힌 것들
```
1. 데이터를 역순으로 정렬하기 위해선 views.py에서 오브젝트를 가져올 때 order_by('-칼럼명')을 해준다.

```
```
2. Models.py> foreign key를 설정할 경우 on_delete= '' 를 설정해주어야 한다.
on_delete 옵션
 - CASCADE : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField를 포함하는 모델 인스턴스도 삭제
 - PROTECT : ForeignKeyField가 바라보는 값이 삭제될 때 삭제가 되지 않도록 ProtectedError를 발생시킴
 - SET_NULL : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField값을 null로 바꾼다.(null=True일 때만 가능)
 - SET_DEFAULT : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField값을 default값으로 바꿈.(default값이 있을 때만 f가능)
 - SET() : ForeignKeyField가 바라보는 값이 삭제될 때 ForeignKeyField값을 SET에 설정된 함수 등에 의해 설정
 - DO_NOTHING : ForeignKeyField가 바라보는 값이 삭제될 때 아무런 행동을 취하지 않음. 
  * 참조무결성을 해칠 위험 존재
 
```
*****
## 고민한 점
```
1. user 삭제 시 user가 작성한 게시글도 함께 삭제할 지 고민
- 
```

