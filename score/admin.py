from django.contrib import admin
from score.models import Player, Team, Match, Over, PlayerMatchStats

# Player
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_runs', 'total_wickets', 'total_matches')
    search_fields = ('name',)

# Team
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Match
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'team1', 'team2', 'winners', 'date')
    search_fields = ('match_number','winners')
    list_filter = ('match_number', 'date')

# Over
class OverAdmin(admin.ModelAdmin):
    list_display = ('match_no', 'over_no', 'over_summary', 'bowler')
    search_fields = ('over_no', 'bowler__name')  # use related field
    list_filter = ('over_no',)

# Player Match Stats
class PlayerMatchStatsAdmin(admin.ModelAdmin):
    list_display = ('match', 'player', 'runs', 'balls', 'wickets')
    search_fields = ('match__match_number', 'player__name')  # use related field
    list_filter = ('match', 'player')

# Register models
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Over, OverAdmin)
admin.site.register(PlayerMatchStats, PlayerMatchStatsAdmin)
