import os
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

FACEBOOK_HOSTNAME = os.environ.get("HOSTNAME", "graph.facebook.com")
FACEBOOK_API = "https://" + FACEBOOK_HOSTNAME + "/v14.0"
FACEBOOK_ACCESS_TOKEN = os.environ["FACEBOOK_ACCESS_TOKEN"]
FACEBOOK_POST_ID = os.environ["FACEBOOK_POST_ID"]


def get_post_data(post_id):
    """Get post data from Facebook API

    Args:
        post_id (str): Facebook post id. format: "pageid_postid"

    Returns:
        dict: Facebook get post data response

    Examples:
        >>> get_post_data("123456789_123456789")
            {
                "reactions":{
                    "data":[],
                    "summary":{
                        "total_count":2
                    }
                },
                "comments":{
                    "data":[],
                    "summary":{
                        "total_count":0
                    }
                },
                "shares":{
                    "count":1
                },
                "id":"103630545568311_169549302309768"
            }
    """
    response = requests.get(
        FACEBOOK_API + f"/{post_id}",
        params={
            "fields": "reactions.summary(total_count),comments.summary(total_count),shares",
            "access_token": FACEBOOK_ACCESS_TOKEN,
        },
    )
    return response.json()


def update_post_data(post_id, message):
    response = requests.post(
        FACEBOOK_API + f"/{post_id}",
        params={"message": message, "access_token": FACEBOOK_ACCESS_TOKEN},
    )
    return response.json()


@sched.scheduled_job("interval", minutes=3)
def main():
    post_data = get_post_data(FACEBOOK_POST_ID)
    print(post_data)
    shares = post_data["shares"]["count"] if "shares" in post_data else 0
    comments = post_data["comments"]["summary"]["total_count"]
    reactions = post_data["reactions"]["summary"]["total_count"]
    message = (
        f"{reactions} REACTIONS, {comments} COMMENTS, {shares} SHARES\n\n"
        "If you REACT, COMMENT, or SHARE"
        " on this post, It will be updated automatically a few minutes later!"
    )
    print(update_post_data(FACEBOOK_POST_ID, message))


# main()
sched.start()
