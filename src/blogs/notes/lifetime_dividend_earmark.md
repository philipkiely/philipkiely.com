Title: Lifetime Dividend Earmark
Date: 2020-12-22
Modified: 2020-12-22
Slug: lifetime_dividend_earmark
Authors: Philip Kiely
Summary: The Lifetime Dividend Earmark (LDK) is a tool for structuring equity-free long-term profit sharing as part of compensation packages for privately-held companies that do not intend to have liquidity events (though it does not preclude them).

Disclaimer: I am not a lawyer or financial professional. This note is for informational purposes only and has not been evaluated for factual accuracy, especially in its legal claims. This is not legal or financial advice. 

The Lifetime Dividend Earmark (LDK) is a tool for structuring equity-free long-term profit sharing as part of compensation packages for privately-held companies that do not intend to have liquidity events (though it does not preclude them). Importantly LDKs are not securities, they are non-transferrable internal bookkeeping records. Along with the Temporary Dividend Earmark (TDK), an LDK-based system removes the need for equity, a traditional profit share, and cash bonuses as part of the compensation structure over the lifetime of the company.

## The Problem

At large firms like Google, employees are compensated in four parts: base salary, benefits, cash bonus, and equity. The equity is re-sellable on the public markets, it is nearly as liquid as cash except for potential regulations about when and how it can be sold. Philosophically, cash bonuses are designed to provide individual and team incentives, while equity motivates some notion of alignment with the performance of the company as a whole. Furthermore, equity is vested over time, which is supposed to motivate employees to stick around for a period of generally four years. For large companies, this is a successful system.

At high-growth venture-backed startups, employees are compensated in the same four parts. Often, the base salaries, benefits, and bonuses are not as substantial as at larger companies. However, the equity is supposed to be worth more in the long run, which is supposed to make up for that discrepancy once the company achieves success. This requires a liquidity event, usually either an IPO or getting acquired. Equity still vests, but is not really useful and has unknown value until the liquidity event, which is why it is often compared to lottery tickets. Still, when the system works, it works well: early employees are well-compensated for their risk and efforts, later employees can expect to bridge the gap on the compensation they would have received at a bigger firm.

However, there are many companies for whom these structures don't work well. Either the company never intends to sell, or it is a bootstrapped operation growing into a midsize team, or it is a company built around one or more content creators and thus can't sell ... there are a large number of small companies across Indie Hackers, content creators, agencies, and professional services offices for whom a compensation structure of base salary, benefits, and LDKs would be a compelling option.

Let's briefly tour the disadvantages of equity, traditional profit sharing, and standard cash bonuses for these firms and their employees.

Equity has various disadvantages as a compensation mechanism:

1. No liquidity. Owning one percent of a small company is cool, but if you need to make a down payment on a house, it won't get you anywhere unless you can sell some of it. 
2. Regulation. The private market for securities in the United States is generally not open to people who are not millionaires (accredited investors) which contributes to the lack of liquidity of private shares.
3. Cost to exercise. Frequently, employees are paid in options, not shares, and then in the case of a liquidity event must come up with thousands or tens of thousands of dollars in a short window of time to exercise their options. 
4. Vesting. To ensure long-term alignment with the company, employees generally receive equity at signing and must wait up to four years until they actually receive all of it (vesting generally begins after one year).
5. Complexity. Issuing someone equity requires approval from the board of directors and at least an email to a lawyer for most companies. Then, you have to actually keep track of that equity.
6. Splitting ownership. By issuing equity, the founder or creator is giving away part of something they built.
7. International complexity. Private shares are actually sometimes easier to sell outside of the United States than within, but there are always additional complexities to crossing borders.

Profit sharing has various disadvantages as a compensation mechanism:

1. A profit share does not outlive the time an employee works at a company, even though the value their work created does. Essentially, profit sharing without long-term ownership fails to properly align incentives
2. Profit shares may need some way of accounting for both seniority and tenure
3. There aren't many industry standards around profit sharing as compared to equity

Cash Bonuses have various disadvantages as a compensation mechanism:

1. Cash bonuses are often seen as an expected part of compensation, yet their actual sums can be unpredictable and unstandardized
2. Cash bonuses generally only come once a year
3. Cash bonuses must be structured carefully to align with overall business goals

Per the list of disadvantages, profit sharing or cash bonuses are much better options than equity for these types of businesses, but with some standards on how to calculate them, a grounding in the business's ever-changing profit, and a mechanism for long-term ownership, they could be the perfect tool for the type of companies we're considering.

## The Solution

So, what is an LDK?

* Lifetime: for the shorter of the lifetime of the company or the person
* Dividend: quarterly cash payment
* Earmark: the person's portion thereof

As a complete sentence, an LDK is a lifetime promise of a portion of the company's profits, paid quarterly. Importantly, people actively working at the company continue to accumulate LDKs every quarter, rewarding tenure and diluting former employees (though everyone benefits as the company's profits grow).

For example, Alice owns a company and Bob and Claire are her new employees. In the first quarter, the company issues Alice 50 LDKs and Bob and Claire each 25 LDKs. The company makes $40,000 in profit that quarter and has decided that 50% of profits will be distributed through the LDKs. Thus, the LDK pool is $20,000. Alice has (50/50+25+25) = 50% of the LDKs, so she gets $10,000, while Bob and Claire each have (25/50+25+25) = 25% of the LDKs, they each get $5,000.

The next quarter, the same thing happens. Alice gets 50 more LDKs, Bob and Claire each get 25 more. Let's say the company made $50,000 in profit and the LDK pool is thus $25,000 dollars. Alice has (100/100+50+50) = 50% of the LDKs, so she gets $12,500, by similar math Bob and Claire each have (50/100+50+50) = 25% of the LDKs, they each get $6,250. 

Finally, the next quarter, Daniel joins the company. At the end of the quarter, Alice still gets 50 LDKs, and now Bob, Claire, and Daniel each get 25 LDKs. Let's say the company made $80,000 in profit this time, which leaves $40,000 in the LDK pool. Now, Alice has (150/150+75+75+25) ~ 46.1% of the LDKs, and receives ~ $18,460. Bob and Claire each have (75/150+75+75+25) ~ 23% of the LDKs and each get ~ $9,230. Daniel has (25/150+75+75+25) ~ 8% of the LDKs and gets ~ $3,100. Over the next few quarters, Daniel will bridge that gap, although this simplified model does incorporate a large and lasting rift in LDK compensation by seniority, which more complex models could avoid (e.g. some LDK grant on hiring, like a signing bonus, and then smaller ones in subsequent quarters).

Implementing LDKs requires coming up with two formulas, which I recommend are made public internally and used on a quarterly cycle, and are currently left as exercises for the reader:

1. How are LDKs to be awarded? Like cash bonuses, it should be through some combination of achievement, seniority, and tenure. There are certainly companies for which it could make sense to pay everyone the same salary and only differentiate on LDK distribution, other for which paying market salaries but distributing equal LDKs is better, and others at every point in between. Furthermore, you'll want to decide if the owner(s) of the company calculate their owners' draw through the LDK system, I recommend that they do.
2. How is profit calculated? This will almost certainly be a custom calculation different from profit for tax purposes or traditional financial statements (indeed, it must be, as LDKs are part of payroll and thus an expense that occurs before actual profit). It is likely prudent to calculate mostly on operating costs vs income and do what you can to abstract major purchases, but you have to actually have the cash to pay out. You also want to retain some profit to finance upcoming purchases, invest in growth, and so forth, but because LDKs are lifetime, this benefits everyone.

It is important to note that an LDK is not a security (otherwise it would be subject to regulation). Why isn't it a security? Simple: it is non-transferrable. If you have an LDK, you can't sell it (even to sell it back to the company), you can't trade it, and if the company ends, the LDKs end with it, if you die, your LDKs no longer exist. That is because LDKs are not a real legal artifact, but rather an internal bookkeeping tool for calculating cash bonuses for current and former employees. It is some combination of a profit share and a pension.

It is only fair to list the disadvantages of LDKs as well:

1. Non-transferrable, you can't cash them in, sell them to anyone, sell them back to the company, or pass them on. However, this means they aren't securities, making them much easier to work with.
2. Like holding equity, holding LDKs may present a conflict of interest if you try to get a new job. As they are non-transferrable, the only way to truly avoid that is to relinquish them, netting no gain. However, some contracts might allow for the continued receipt of LDK payouts if only because they don't know what they are.
3. LDK-based payouts are part of payroll and thus subject to all applicable taxes.
4. Granting someone LDKs is a fairly big commitment as they are a lifetime promise. See TDKs for potential solutions.
5. While it is just payroll, this likely wouldn't play well with equity, as shareholders may be uncomfortable with a "senior" claim to the business's profits.
6. LDKs are not as iron-clad legally as shares. Basically, as they are part of a negotiated (and, in the US, likely at-will) compensation package, rather than being part of the company's incorporating documents, they require a bit more trust from both parties. But, this means they are also more flexible.

Conspicuously missing from the disadvantages list is how LDKs perform in a liquidity event. Again, LDKs are intended for companies that don't sell, but instead make profit for a long time. However, LDKs handle sale rather well. A sale is just a rather large bit of profit, you have a set way of distributing profits, put the money through the system as normal. After that, the company doesn't exist, so no profits means no distributions. In the event of an acquisition paid in equity or with vesting or otherwise too complex for the above, issue equity in the company before the acquisition according to accumulated LDKs.

I believe many companies could apply LDKs to all situations. However, for some additional flexibility at the expense of additional complexity, you can augment any LDK-based system with Temporary Dividend Earmarks, or TDKs. A TDK is just an LDK with an expiration date in the format -XD where X is the number and D is the duration (either quarters or years). Potential uses, in increasing order of usefulness:

* Use a TDK-1Q as a traditional cash bonus for something one-time but exemplary (though I would recommend issuing a smaller number of LDKs instead).
* If the "L" in LDK is too big a commitment, run the same system on long-lasting TDKs, like TDK-5Y.
* To simulate vesting and avoid long-term commitments to short-term employees, start people on TDK-1Y for their first four grants and then convert the TDKs into LDKs along with any follow-up grants in quarters 5-8.

This explanation is for the general case, LDKs are very adaptable. I created this concept because it fits extremely well with certain other unusual structures in my business plan, but wrote it up because it works well as a stand-alone practice for other companies to adopt.

If you are interested in using an LDK-based system at your company, let me know at [philip@kiely.xyz](mailto:philip@kiely.xyz) and I'll be happy to walk you through anything that this explanation overlooks. Managing and paying out LDKs seems like it could be a small SaaS product, or a feature of a larger payroll tool like Gusto, if it caught on among the many companies for which I think it would be a good fit which exist today and the much greater number that will come to exist in the next decade.