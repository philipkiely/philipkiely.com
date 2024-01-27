Title: Modeling the Obligatory Late November Sale in the Creator Economy
Date: 2020-11-24
Modified: 2020-12-01
Slug: november_sale
Authors: Philip Kiely
Summary: Black Friday and associated late November sales are collectively a neutron star warping the gravity field of the annual consumer spending cycle. Depending on your model, this can be a good or a bad thing.

Black Friday and associated late November sales are collectively a neutron star warping the gravitational field of the annual consumer spending cycle. The story of [how Black Friday came to be](https://en.wikipedia.org/wiki/Black_Friday_(shopping)) is fairly simple: a focal point for sales gaining momentum year after year. While Black Friday started with American big box retailers offering discounts to consumers shopping primarily for Christmas gifts, it has turned into a cultural event in itself and has, in recent years, even come to the creator economy.

Depending on your model, this can be a good or a bad thing. Sure, now-defunct department stores offering discounts on televisions a decade ago shouldn't be the basis for deciding how to price my information products. But, everyone choosing to run a discount at the same time of year is a great reason for me to choose to discount my own products. So, let's talk about the Obligatory Late November Sale (OLNS).

I've worked retail on holidays; I have reason to dislike Black Friday. But, I've also walked through midwestern malls with friends from Russia, Iran, and Germany, all staying over for Thanksgiving, spectating and indulging in the excesses of the America they have seen on TV. Rather than trying to develop moral arguments for and against Black Friday as a whole, I'm tackling the much easier task of developing one game theoretic model for and one against the OLNS specifically applied to the online creator economy.

If you have no background in Game Theory, spend a few minutes [here](https://www.investopedia.com/terms/g/gametheory.asp) or just look up terms that are unfamiliar as you go.

All models are wrong, some are useful. The usefulness of a model starts with the underlying assumptions. There are two important simplifying assumptions that I am making in the following models. The first is that offering a OLNS does not materially increase the creator's reach. This assumption is based on the difficulty of standing out from the noise of everyone offering some sort of Black Friday discount. Thus, another necessary assumption is that some percent of a creator's audience has not yet bought their product.

The second simplification is that I am playing fast and loose with the idea of a "player" in game theory. Game theorists have developed more sophisticated models than the ones presented below for modeling one player's interactions against a prevailing norm rather than a single other player. However, by making my model more wrong (using a two-person creator economy), I can actually make it more widely useful by requiring less econ background to understand the model.

### Model 1: Prisoner's Dilemma

Thesis: Creators don't want to run discounts because they lose out on margin.

If creators don't want to run discounts, running a OLNS is a prisoner's dilemma. Let's take two creators, Alice and Bob, who each sell a similar information product in the same market. Their information products each costs 33 dollars, each Alice and Bob is considering a 1/3 discount to 22 dollars.

If neither Alice nor Bob runs a discount, each will sell 10 units, the same as they sell every week. However, if Alice runs a discount, she will attract 6 more customers. Let's say that 3 are new participants in the market and the other 3 would have bought from Bob but for the discount. The same thing happens in reverse if Bob runs a discount. However, if they both run discounts, they each attract 3 new customers, but neither steals the others' customers. It is important to note here that I am NOT modeling a discount as a zero-sum game, which would be inappropriate for a large market like the creator economy.

Here is a payoff matrix of revenue for that situation:

![PD Payoff Matrix](/assets/img/blogs/essays/november_sale/olns_pd.png)

Alice and Bob both have a dominant strategy of running a discount, but both will end up with less revenue than if neither had discounted.

Astute readers may note that these numbers, which are totally fabricated, could be altered such that running a discount is a good deal for both parties. Why not conjure up more customers attracted by the discount?

### Model 2: Assurance

Thesis: Creators want to run discounts to generate marginal sales.

Let's slightly adjust the above model: regardless of whether Alice or Bob runs the discount alone or at the same time, if one runs a discount, they get 6 additional customers, and these are all new customers and not from each others' customer bases. The model is a bit different now, but they have the same dominant strategy: run the sale regardless of the others' action.

![A1 Payoff Matrix](/assets/img/blogs/essays/november_sale/olns_a1.png)

However, this model doesn't yet answer why it is strictly beneficial for creators to run discounts at the same time. Well, consumer psychology is a tricky thing. For information products, generally priced at a premium (charge more!) and targeted at professional audiences, frequent discounts can undermine the credibility of the price and product. Price uncertainty can delay purchases, after all, if the product is randomly discounted, why not wait? After running random sales, I've even had customers making a purchase a day before or after write to me asking to get refunded down to the sale price. People don't like to feel like they missed out.

So, if running a sale, especially a major discount that really attracts the marginal customer, is risky, and doing it too often cuts into your margin and credibility, then you want to run such sales infrequently but predictably. Thus, the Obligatory Late November Sale actually represents a wonderful opportunity! You can run your deep discount and customers are expecting it. Many creators and larger businesses participating isolates you from most backlash, after all, it is on the customer if they didn't see it coming or they missed it. Customers unwilling to pay full price will wait for a known date, while customers paying full price ahead of time will know that they could have waited and are choosing not to. 

Let *R* be the reputation hit from having a random sale. Then, for Alice and Bob, the assurance model of the OLNS is:

![PD Payoff Matrix](/assets/img/blogs/essays/november_sale/olns_a2.png)

Running a sale at the same time gives both creators extra revenue without the reputation hit.

Coordinating a sale between every creator would be very difficult. Assurance models have the idea of focal points, so everyone who knows the payoffs and participants could come up with the same focal point without communicating. Black Friday is, as I stated at the beginning, a neutron star of a focal point, making it easy for creators everywhere to run a sale at the same time.

### Model 3: Anecdote!

I ran my Obligatory Late November Sale from Monday the 23rd through the end of the month. After a tweet announcing the discounts, Monday I made enough to fill the fridge and pantry at Trader Joe's, Tuesday I made enough to buy some secondhand furniture for my new apartment. Fortunately, I'm not in the position of relying on this income to do those things, but even still paying for material expenses with information product money feels *really* good. All told, I made over 700 dollars running the sale, which is much more than I would have earned ordinarily. 

![Gumroad Analytics Screenshot](/assets/img/blogs/essays/november_sale/olns_ss.jpg)

The sale is over, but I'm already looking forward to next year's. By then, I should have more products and a much larger audience and be able to do more interesting and lucrative deals. 