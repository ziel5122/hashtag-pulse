from tweepy import OAuthHandler

ckey = "akuev4PsTECrfbqNPsKyQT6fP"
csecret = "eLTRit1rmonG462a3B2lmdkb7JVY48DdlJaYd60Fk6AcUvq1hB"
atoken = "1456219693-61xWShfn0peSARV46Ucc5pPkxECw9ICrwFJwI1c"
asecret = "10RmuOTY1UK0UNRzYwDhDrdmEt3lXAY79epagrgqqHje6"

def getOAuth():
    oauth = OAuthHandler(ckey, csecret)
    oauth.set_access_token(atoken, asecret)
    return oauth
