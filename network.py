import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("FWs7xpTRtMEYCHVSIx2tNBgdM", 
    "SmyuYbCxcCAjWNIiZNcpLTOpaDflnusf1fSfmiLJsTf3quVZyL")
auth.set_access_token("1158896589651550208-DSEo1R4rvPZDkY1GO7oo0uYbZ6O2EI", 
    "PZgRNom5bxcItPMxEIczV2vqV9a7CosmJgBD06Z0ssLWE")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
