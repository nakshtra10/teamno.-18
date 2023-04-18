import requests
import json

# Define the YouTube API endpoint and API key
endpoint = "https://www.googleapis.com/youtube/v3/videos"
api_key = "YOUR_API_KEY_HERE"

# Define a function to analyze the tags and suggest changes
def analyze_tags(video_id):
    # Send a GET request to the YouTube API
    params = {
        "part": "snippet",
        "id": video_id,
        "key": api_key,

    }
    response = requests.get(endpoint, params=params)
    data = json.loads(response.text)

    # Retrieve the video's tags
    tags = data["items"][0]["snippet"]["tags"]

    # Analyze the tags and suggest changes
    suggested_tags = []
    for tag in tags:
        # Check if the tag is too short or too long
        if len(tag) < 3 or len(tag) > 25:
            continue

        # Check if the tag is in all uppercase or lowercase
        if tag.isupper() or tag.islower():
            suggested_tags.append(tag.title())
            continue

        # Check if the tag contains non-alphanumeric characters
        if not tag.isalnum():
            suggested_tags.append("".join(c for c in tag if c.isalnum()))
            continue

        # If none of the above conditions are met, keep the tag as is
        suggested_tags.append(tag)

    # Print the suggested changes
    if len(suggested_tags) == 0:
        print("No suggested changes.")
    else:
        print("Suggested changes:")
        for tag in suggested_tags:
            print(f"- {tag}")

# Call the function with a video ID
analyze_tags("VIDEO_ID_HERE")

