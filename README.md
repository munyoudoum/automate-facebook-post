# Automate Facebook Post

## Export Environment Environment Variables
```bash
export FACEBOOK_POST_ID=pageid_postid
export FACEBOOK_ACCESS_TOKEN=XXX
```

## Generating a never expiring Facebook token
1. Go to https://developers.facebook.com/tools/debug/accesstoken/
2. Input your short lived token
3. Click `Extend Access Token`
4. GET `https://graph.facebook.com/v14.0/App-Scoped-User-ID/accounts?access_token=extendedtoken`

## References
- https://developers.facebook.com/docs/graph-api/reference/page-post
