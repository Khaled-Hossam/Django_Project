from django import forms
from .models import Post,Comment

class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('comment_content',)






class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title','post_content',)
            # widgets={
            #     'title':forms.TextInput(attrs={'class':'form-control'}),
            #     'post_content':forms.TextInput(attrs={'class':'form-control'}),
            #     'city':forms.Select(attrs={'class':'form-control'}),
            #     'user':forms.Select(attrs={'class':'form-control'}),

            # }