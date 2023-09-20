"""
https://leetcode.com/problems/encode-and-decode-tinyurl/

Category - Medium

Note: This is a companion problem to the System Design problem: Design 
TinyURL.
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL
such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and
decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You 
just need to ensure that a URL can be encoded to a tiny URL and the tiny URL 
can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given 
shortUrl. It is guaranteed that the given shortUrl was encoded by the same 
object.
"""

class Codec:

    URLS = {}
    COUNT = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        Codec.COUNT += 1
        short_url = str(Codec.COUNT)
        Codec.URLS[short_url] = longUrl
        return f"http://tinyurl.com/{short_url}"

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        try:
            return Codec.URLS[shortUrl.split("/")[-1]]
        except Exception as err:
            print("wrong short url")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
