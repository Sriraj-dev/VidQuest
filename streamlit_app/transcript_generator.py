from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi


def save_transcripts(links: list):
    video_ids = []


    #Converting links to video Ids.
    def get_video_ids(links):
        for link in links:
            parsed_url = urlparse(link)
            if parsed_url.netloc == "www.youtube.com" and parsed_url.path == "/watch":
                # Extract the video ID from the query parameter
                video_id = parsed_url.query.split("=")[-1]
                video_ids.append(video_id)
            else:
                print("The given link is not a valid video link!!")

    
    get_video_ids(links)
    # Save the transcripts in the data folder.
    for i in range(len(video_ids)):
        srt = YouTubeTranscriptApi.get_transcript(video_ids[i])
        with open(f"../data/video_{i}.txt","w") as file:
            text = ""
            for transcript in srt:
                text += transcript['text'] + "\n"
            file.write(text)