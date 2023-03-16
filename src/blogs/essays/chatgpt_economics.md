Title: ChatGPT API Napkin Math for Indie Hackers
Date: 2023-03-13
Modified: 2023-03-14
Slug: chatgpt_economics
Authors: Philip Kiely
Summary: Napkin math on the unit economics of the ChatGPT API (both GPT-3.5 and GPT-4) for various business models. 

GPT 3.5 chat API invocations cost $0.0002 per 1,000 tokens. GPT-4, as of launch, has much higher and more complex prices, ranging from 15x to 60x more expensive. What kind of business models does each support?

### Unit economics

It's a simple equation: is the marginal revenue from an additional user greater than the marginal API invocation costs that user incurs?

If yes, you have a viable monetization strategy.

### Invocation costs

At today's prices, a penny buys 5,000 tokens from GPT-3.5. That is about 4,000 words, counting both input and output. 

For a dollar, you can get:

* Two books about as long as *Moby Dick*
  * Or the first third of *Animal Farm* by GPT-4
* A standard-length blog post every day for eight months
  * Or one a month from GPT-4
* As many as 20,000 tweets
  * Or about 500 from GPT-4

Will they be good? Depends on the prompt! We're here to talk quantity, not quality.

### Monetization strategy: page views

We're specifically talking about monetizing API invocations, not creating a content site using generated content. 

Marginal revenue per user depends on the CPM of your ads, which in turn depends on the type of ad you display and the type of user you display it to.

To put a figure on it, [Google AdSense](https://adsense.google.com/start/) will earn you about $0.009 per user serving ads about technology to a North American audience.

So as long as your average user only prompts/generates a couple thousand words, you come out ahead.

You might use a more stochastic monetization strategy like ads for your own work or a tip jar. My [poetry generator](https://philipkiely.com/rhymes) makes 25 sonnets for a penny. Assuming users generate 5 poems each, I need about 1 in every 10,000 users to leave a five-dollar tip or buy a book and I come out ahead. So hobby projects with short outputs are entirely feasible to operate at breakeven with minimal monetization.

### Monetization strategy: subscription

If your user is generating more than a few thousand words, you probably won't make it on ads alone. Even tiny subscription prices, like 20 dollars a year (equivalent to a domain name registration) puts you in the black as long as your users only generate a few million words each.

With this strategy, GPT-4 becomes more viable if the value-add over GPT-3.5 is there. A Netflix-level ten dollars per month covers on the somewhere between fifty to a hundred thousand words per month, so your users can do NaNoWriMo every month and you should be good, but might need to increase the price a bit to make a reasonable margin.

#### BYO API key

Bring your own API key is another version of subscription pricing. With this, users generate their own API keys on OpenAI and pay for usage themselves, while you charge a flat fee for some kind of value-add platform, like a better UI or integrations.

The upside to this approach is you don't have to think about API usage at all in your pricing. But it does limit your customer base to the people with the technical knowledge and inclination to manage their own API keys.

Thanks to [Bruno Cruz](https://twitter.com/ImBrunoCruz) for suggesting this additional strategy.

### Monetization strategy: usage-based pricing

The low price of ChatGPT per token gives you a lot of headroom for healthy margins if you're doing usage-based pricing for some kind of value-add. On the other hand, it means you'll need a lot of volume to make a real business out of it.

On GPT-3.5, let's say you had this incredible situation: you charge a 500% markup and your average MAU uses 100,000 tokens.

You're still only making a dollar of MRR per MAU.

*I hope this napkin math helps your intuition on the feasibility for various projects with GPT models. I know running these numbers made me even more excited to experiment knowing that the API charges would be negligible. For example, the poetry generator cost 3 cents for all of the test invocations I made during development.*