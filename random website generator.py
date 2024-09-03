import random
import requests

def generate_random_website():
  """Generates a random website."""

  # Get a list of random domains.
  domains = ["https://www.google.com", "https://www.facebook.com", "https://www.amazon.com", "https://www.youtube.com", "https://www.wikipedia.org", "https://www.reddit.com", "https://www.twitter.com", "https://www.instagram.com", "https://www.tiktok.com", "https://www.twitch.tv", "https://www.netflix.com", "https://www.hulu.com", "https://www.disneyplus.com", "https://www.apple.com", "https://www.microsoft.com", "https://www.amazon.com", "https://www.ebay.com", "https://www.etsy.com", "https://www.walmart.com", "https://www.target.com", "https://www.bestbuy.com", "https://www.homedepot.com", "https://www.lowes.com", "https://www.cnn.com", "https://www.nytimes.com", "https://www.washingtonpost.com", "https://www.bbc.com", "https://www.theguardian.com", "https://www.espn.com", "https://www.nfl.com", "https://www.nba.com", "https://www.mlb.com", "https://www.nhl.com", "https://www.wikipedia.org", "https://www.quora.com", "https://www.stackoverflow.com", "https://www.github.com", "https://www.foxstudiosscratch.xyz", "https://github.com/Fox-Studios-Scratch", "https://www.youtube.com/@aidenjamesyt", "https://donosworlds.gg", "https://www.foxstudiosscratch.xyz", "https://www.discord.com", "https://www.foxstudiosscratch.xyz/discord", "https://github.com/Fox-Studios-Scratch"]

  # Choose a random domain.
  domain = random.choice(domains)

  # Get a random path.
  path = random.choice(["/", "/about", "/contact", "/products", "/services"])

  # Generate the random website URL.
  website_url = f"{domain}{path}"

  # Try to access the random website.
  response = requests.get(website_url)

  # If the website is accessible, return the URL.
  if response.status_code == 200:
    return website_url

  # Otherwise, try again.
  else:
    return generate_random_website()


# Example usage:

website_url = generate_random_website()

print(website_url)
