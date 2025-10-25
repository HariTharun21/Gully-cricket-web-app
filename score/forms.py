from django import forms
from score.models import Player,Team,Match


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['match_number', 'team1', 'team2','total_overs']  # added total_overs
        widgets = {
            'match_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'team1': forms.Select(attrs={'class': 'form-select team-select'}),
            'team2': forms.Select(attrs={'class': 'form-select team-select'}),
        }
        





class PlayerSearchForm(forms.Form):
    name = forms.CharField(max_length=30, required=False, label='search by name')