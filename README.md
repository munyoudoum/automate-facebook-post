# Automate Facebook Post

## Preview:
![Screen Shot 2022-08-05 at 11 25 05 PM Cropped](https://user-images.githubusercontent.com/60089135/183120435-d1a43ab4-651d-412b-b342-a7c475a82adb.png)
https://www.facebook.com/169975945600437

### Youtube video: https://www.youtube.com/watch?v=3HvzgDzrG0c

## Generating a never expiring Facebook token
1. Go to https://developers.facebook.com/tools/debug/accesstoken/
2. Input your short lived token
3. Click `Extend Access Token`
4. GET `https://graph.facebook.com/v14.0/App-Scoped-User-ID/accounts?access_token=extendedtoken`
![Screen Shot 2022-08-05 at 3 36 04 AM](https://user-images.githubusercontent.com/60089135/183119721-75e5fe5c-1a7f-44c5-a91b-e30c2e1239ef.png)

## Export Environment Environment Variables
```bash
export FACEBOOK_POST_ID=pageid_postid
export FACEBOOK_ACCESS_TOKEN=XXX
```

## References
- Page Post Facebook Graph API: https://developers.facebook.com/docs/graph-api/reference/page-post
- Facebook app: https://developers.facebook.com/apps
- Get facebook post id: https://business.facebook.com/content_management
