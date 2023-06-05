from activity import club_users, get_user_list, all_club_users

def win_rate(user):
    return user['scoreWinCount'] / (user['scoreWinCount'] + user['scoreLoseCount'])

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVuaWQiOiJvY3RFQjVYV3dTVmVuZmR2b0ZXcENnMlF3ZWprIiwidXNlcklkIjo3NDAwNSwidXNlckNvZGUiOjk4MzAyNCwidW5pb25pZCI6Im9Vam9nMUc5eldBV3dTZldjZUxMUVY5YUZLS1UiLCJ1c2VyTmFtZSI6IuWVpuWVpuWVpiIsImdlbmRlciI6MSwic2VydmljZUF2YXQiOiJ1cGxvYWRzXzEvYXZhdGFyLzk4M18vOTgzMDI0LmpwZyIsInJlYWxBcmVhIjoiIiwicmVhbENpdHkiOiIiLCJyZWFsUHJvdmluY2UiOiIiLCJyZWFsQ291bnRyeSI6IiIsImNpdHlDb2RlIjo0NDAzMDAsImFjdGl2ZUNsYXNzaWZ5IjoxLCJhY3RpdmVQYXJhbXMiOiJ7XCJjbGFzc2lmeV8xXCI6W3tcImlkXCI6MTAwMSxcIm5hbWVcIjpcIue-veavm-eQg1wiLFwiY2xhc3NpZnlcIjoxLFwic2VhcmNoXCI6e1wiYXR5cGVzQ2xhc3NpZnlcIjoxLFwiYXR5cGVzVHlwZVwiOjEwMDF9LFwieGNoZWNrXCI6dHJ1ZX1dfSIsImJpcnRoZGF5IjoiIiwidHJhaXQiOiIiLCJob2JieSI6IiIsImJsYWNrQ291bnQiOjAsImZhbnNDb3VudCI6MywiZm9sbG93Q291bnQiOjAsImZyaWVuZENvdW50IjowLCJkb21haW4iOiJodHRwczovL3d3dy53YW5qdXdvdy5jb20vc2hvcC8iLCJuaWNrbmFtZSI6IuWVpuWVpuWVpiIsImF2YXRhcnVybCI6Imh0dHBzOi8vd3d3Lndhbmp1d293LmNvbS9zaG9wL3VwbG9hZHNfMS9hdmF0YXIvOTgzXy85ODMwMjQuanBnIiwiaWF0IjoxNjg1OTU3Mzc0LCJleHAiOjE2ODU5NjQ1NzR9.uJWOHf7AyR9JxCaXu2NHLsjiHBGySAPzPoBnJTH3DuY'

club_users = all_club_users(token)
signup_list = get_user_list(token, 277388)['data']['signUps']

player_win_rates = { user['userName'] : win_rate(user) for user in club_users }
player_score_rank = { user['userName'] : user['ranknum'] for user in club_users}

sorted_signup = sorted(signup_list, key=lambda x: player_win_rates.get(x['userName'], 0) or 0, reverse=True ) 
sorted_names = [user['userName'] for user in sorted_signup]

group_a = sorted_names[0::2]
group_b = sorted_names[1::2]
print(group_a)
print(group_b)