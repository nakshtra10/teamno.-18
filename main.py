import requests
import pandas as pd

# Read the Excel sheet
df = pd.read_excel('Project1.xlsx')




# Define the upload functions for each platform
def upload_to_youtube(title, description, file_path):
    endpoint_url = 'https://www.googleapis.com/upload/youtube/v3/videos'
    params = {'part': 'snippet'}
    files = {'videoFile': open(file_path, 'rb')}
    data = {'snippet': {'title': title, 'description': description, 'status': status}}
    response = requests.post(endpoint_url, params=params, data=data, files=files)
    response.raise_for_status()
    return response.json()


def upload_to_linkedin(title, description):
    endpoint_url = 'https://api.linkedin.com/v2/ugcPosts'
    data = {'snippet': {'title': title, 'description': description, 'status': status}}
    response = requests.post(endpoint_url, json=data)
    response.raise_for_status()
    return response.json()


def upload_to_facebook(title, description, file_path):
    endpoint_url = 'https://graph-video.facebook.com/YOUR_FACEBOOK_PAGE_ID/videos'
    files = {'file': open(file_path, 'rb')}
    data = {'title': title, 'description': description, 'status': status}
    response = requests.post(endpoint_url, data=data, files=files)
    response.raise_for_status()
    return response.json()


# Loop through the Excel sheet and upload the videos/posts
for index, row in df.iterrows():
    title = row['TITLE']
    description = row['DESCRIPTION']
    file_path = row['FILE PATH']
    platform = row['PLATFORM']
    dateandtime = row['DATE']
    status = row['PRIVACY']

    if platform == 'YouTube':
        upload_to_youtube(title, description, file_path)
        print(f'Uploaded "{title}" to YouTube!')
    elif platform == 'LinkedIn':
        upload_to_linkedin(title, description)
        print(f'Uploaded "{title}" to LinkedIn!')
    elif platform == 'Facebook':
        upload_to_facebook(title, description, file_path)
        print(f'Uploaded "{title}" to Facebook!')
    else:
        print(f'Invalid platform specified for "{title}"!')