from django import forms
from taggit import forms as taggit_form
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         super(ArticleAddForm, self).__init__(*args, **kwargs)
         self.fields['category'].widget.attrs['form'] = 'addArticleForm'
         self.fields['category'].help_text = 'Pilih Kategori Artikel *(bisa lebih dari 1)'
         self.fields['category'].widget.attrs['style'] = 'width:100%; padding:10px'
         self.fields['title'].widget.attrs['style'] = 'width:100%; padding:10px'
         self.fields['is_featured'].widget.attrs['style'] = 'margin:10px 10px 0 0'
         self.fields['is_featured'].widget.attrs['data-toggle'] = 'toggle'
         self.fields['is_published'].widget.attrs['style'] = 'margin:10px 10px 0 0'
         self.fields['is_published'].widget.attrs['data-toggle'] = 'toggle'
         self.fields['content'].widget = CKEditorUploadingWidget()
         self.fields['tags'].widget.attrs['form'] = 'addArticleForm'
         self.fields['tags'].widget.attrs['style'] = 'width:100%; padding:10px'
         self.fields['tags'].help_text = 'Bisa lebih dari 1, pisahkan dengan koma ( , )'
    class Meta:
        model = Article
        fields = ('title','content','is_published','is_featured','featured_image', 'category', 'tags')
