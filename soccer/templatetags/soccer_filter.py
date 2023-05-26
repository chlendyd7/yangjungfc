import markdown #마크다운
from django import template
from django.utils.safestring import mark_safe #마크다운



register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    """
    mark 함수는 markdown 모듈과 mark_safe 함수를 이용하여 입력 문자열을 HTML로 변환하는 필터 함수이다
    nl2br은 줄바꿈 문자를 <br> 로 바꾸어 준다. fenced_code는 위에서 살펴본 마크다운의 소스코드 표현을 위해 필요하다.
    nl2br을 사용하지 않을 경우 줄바꿈을 하기 위해서는 줄 끝에 스페이스(' ')를 두개 연속으로 입력해야 한다.
    """
    return mark_safe(markdown.markdown(value, extensions=extensions))