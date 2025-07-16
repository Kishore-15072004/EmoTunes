import webbrowser

def recommend_music(emotion, weather):
    weather_condition = weather.lower()
    
    music_recommendations = {
        "happy": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DWZ7mSWCFIT7v"],
            "cloudy": ["https://open.spotify.com/playlist/30OEGKX5eZkHgEBxAl5oS4"],
        },
        "sad": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DWX83CujKHHOn"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DWU13kKnk03AP"],
            "cloudy": ["https://open.spotify.com/playlist/37i9dQZF1DWXJfnUiYjUKT"],
        },
        "angry": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DX6mMeq1VVekF"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6"],
            "cloudy": ["https://open.spotify.com/playlist/37i9dQZF1E4y5ITKxjdD77"],
        },
        "fear": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DWWF3yivn1m3D"],
            "cloudy": ["https://open.spotify.com/playlist/37i9dQZF1DWStljCmevj7t"],
        },
        "neutral": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DWZ7mSWCFIT7v"],
            "cloudy": ["https://open.spotify.com/playlist/37i9dQZF1DX1s9knjP51Oa"],
        },
        "disgust": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DX5uokaTN4FTR"],
            "cloudy": ["https://open.spotify.com/playlist/37i9dQZF1DWWhB4HOWKFQc"],
        },
        "surprise": {
            "sunny": ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"],
            "rainy": ["https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"],
            "cloudy": ["https://open.spotify.com/playlist/30OEGKX5eZkHgEBxAl5oS4"],
        },
    }

    if emotion in music_recommendations:
        if weather_condition in music_recommendations[emotion]:
            return music_recommendations[emotion][weather_condition]
        else:
            return music_recommendations[emotion].get("default", ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"])
    else:
        return ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"]

def open_music_links(links):
    for link in links:
        webbrowser.open(link)

if __name__ == "__main__":
    weather = "cloudy"
    emotion = "happy"
    playlists = recommend_music(emotion, weather)
    for playlist in playlists:
        print(f"Recommended Playlist: {playlist}")
