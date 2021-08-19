# djangoToy
장고 게시판 토이프로젝트

*****

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
>python manage.py migrate

5. 슈퍼 유저 생성
python manage.py createsuperuser

```
*****
## 하다가 막힌 것들
```
1. 데이터를 역순으로 정렬하기 위해선 views.py에서 오브젝트를 가져올 때 order_by('-칼럼명')을 해준다.

```

*****

