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
```
3. Models.py> foreign key를 설정할 경우
참조할 테이블의 컬럼명을 설정해 주지 않았는데 동작이 되는 것을 보고 의문이 들었다.
--> Primary key가 한 개인 테이블은 자동으로 Primary key를 참조하기 때문에 따로 설정할 필요가 없다.
--> 컬럼 설정은 db_column='컬럼명' 형태로 준다.

```
```
4. SQLITE3 를 사용하여 테스트 데이터를 만든 후, db 구조를 변경하는 데 id값이 꼬여서 sqlite3 를 초기화하게 되었다.
초기화 순서
--> django 각 앱의 migrations 파일에서 __init__.py 파일 빼고 전부 삭제해준다.
--> sqlite3 를 삭제해준다.
--> python manage.py makemigrations
--> python manage.py migrate

```
```
4-1. sqlite3 초기화 후 superuser가 삭제되었다. superuser의 저장위치가 궁금해졌다.
-- 찾는중 --

```
```
5. 게시글 테이블에서 사용자 테이블의 id 값을 참조하여 사용자의 이름을 가져오고 싶다.
오라클이나 mssql 에서는 join을 이용하여 간단하게 가져올 수 있지만 django에서는 어떤 방식으로 가져올 수 있는지 서치가 필요하다.

```

*****
## 고민한 점
```
1. user 삭제 시 user가 작성한 게시글도 함께 삭제할 지 고민
- set_null 형태로 게시글은 남겨두되 글을 쓴 작성자는 null값으로 변경한다.
```

