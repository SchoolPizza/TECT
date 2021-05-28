from django import forms

class SearchForm(forms.Form):
    # 일반 폼이므로 form을 통해 들어온 데이터를 cleaned_data를 이용해 유효한지 체크한 후 저장
    search_word = forms.CharField(label='Search Word ')