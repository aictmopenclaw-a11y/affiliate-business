# ClickBank 2026 — How to Select Winning Offers

A tactical, data-backed playbook for picking your first (and twentieth) ClickBank offer to test on Meta with limited capital. Built for a LATAM-focused operation with $300-500 to risk per test.

**Purpose:** Avoid burning the test budget on offers that were structurally doomed. Most first-offer failures are not creative or copy failures — they are *selection* failures decided in the first 30 minutes of research.

**How to use this doc:** Re-read Section 3 (the 7-step framework) before every weekly offer pick. The rest is reference.

**Source-tagging convention used throughout:**
- `[VERIFIED]` — directly from ClickBank official documentation or vendor postings
- `[INDUSTRY STANDARD]` — consensus across multiple credible affiliate marketing publications
- `[COMMUNITY WISDOM]` — recurring advice from forums (Warrior, BlackHat, Reddit) — treat with skepticism
- `[PROPOSED]` — author synthesis based on research — test before trusting

---

## 1. Executive Summary

Picking a winning ClickBank offer in 2026 is an exercise in *elimination*, not selection. The marketplace shows roughly 5,000+ active offers. Most are:

- Saturated and overrun by 7-figure media buyers (top of every gravity list)
- Compliance time-bombs that will get your Meta account banned within 48 hours
- Vendor-side scams with refund rates that make profit mathematically impossible
- Front-end too thin to break even at any realistic CPC

The 90/10 reality: **90% of ClickBank offers should never be touched by a beginner with $300-500 to test.** This document exists to identify the 10% worth testing.

**The four non-negotiable filters for your first offer:**

1. **Front-end commission ≥ $40** — anything thinner kills you on Meta CPCs of $0.80-2.50 [PROPOSED]
2. **Vendor with 12+ months on ClickBank, 2+ products** — rules out fly-by-night refund-bait launches [INDUSTRY STANDARD]
3. **Compliance-safe VSL** (no disease cures, no dramatic before/after, no unverified doctor endorsements) [VERIFIED — Meta policy]
4. **Either: Spanish-translated by native speakers OR an English offer where you accept Tier-1 traffic costs**

**The four metrics that actually matter (in order):**

1. EPC (Earnings Per Click) — your real constraint vs. Meta CPC
2. Gravity in the 30-150 range — proves conversion without 7-figure competition
3. Initial $/sale ≥ $40 — the only money you can count on
4. Refund rate ≤ 15% (estimated via $/sale gap, not displayed)

Everything else is supporting evidence. Build the rest of your evaluation on those four.

---

## 2. Complete Metrics Decoder

Every metric ClickBank displays, what it actually means, the math behind it, and the 2026 thresholds.

### 2.1 Gravity

**What it measures:** A weighted count of unique affiliates who have generated at least one commission for the offer in the last 12 weeks. More recent sales weighted more heavily. An individual affiliate can never add more than 1.0 to a product's gravity, regardless of sales volume. [VERIFIED — ClickBank official; per White Hat Crew interpretation: each affiliate paid in the last 8 weeks adds between 0.1 and 1.0 weighted by recency.]

**The math (approximate, ClickBank does not publish exact weights):**
```
Gravity ≈ Σ (per affiliate) recency_weight(last_sale_date)
where recency_weight is between 0.1 and 1.0
window = 12 weeks rolling
```

**What good looks like in 2026:**

| Range | Interpretation | Recommended for |
|-------|---------------|-----------------|
| 0-10 | Brand new launch OR dead offer | Avoid as first pick — no proof of conversion |
| 10-30 | Early validation, less competition | Advanced affiliates with creative angle |
| **30-150** | **Sweet spot** — proven + room to compete | **First-time affiliates START HERE** |
| 150-300 | Saturated — only 7-figure buyers can compete on Meta | Avoid unless you have angle/audience advantage |
| 300+ | Hyper-saturated — every keyword auctioned, every angle done | Skip. Top affiliates pay $4-8 CPC profitably; you cannot |

[INDUSTRY STANDARD — ClickBank's own blog recommends 50-200; AffNinja and most affiliate publications converge on 30-150 as the realistic sweet spot for new affiliates with paid traffic]

**When high gravity is BAD:**
- 7-figure media buyers have already optimized every audience, hook, and creative angle
- Auction prices on Meta lookalikes are inflated — your CPC will be 2-3x what a low-competition offer costs
- Meta's algorithm has seen the offer's funnel pixel-fired millions of times — it knows the real buyer profile and will not show your ad to anyone else

**When low gravity is OPPORTUNITY:**
- Recently launched product with vendor running affiliate webinars (check tools page for date)
- Underserved niche (women's bladder, dental, specific menopause angles) where the marketplace simply hasn't caught up
- Vendor manually approves affiliates — barrier keeps gravity artificially low while quality is high

**Common misinterpretations:**
- **"Higher gravity = higher EPC"** — Wrong. Gravity counts affiliates, not sales-per-click. Often inversely correlated due to auction inflation.
- **"Gravity = current popularity"** — Partially. The 12-week window means a hot offer 10 weeks ago can still show inflated gravity today.
- **"Gravity tells me anything about refund rate"** — Zero correlation. A gravity-300 offer with 30% refund rate burns hundreds of affiliates monthly.

### 2.2 Avg $/Sale (a.k.a. Avg $/Conversion)

**What it measures:** Average commission per conversion over the last 90 days, *including* initial sales, upsells, downsells, and recurring rebills. [VERIFIED — ClickBank official]

**The math:**
```
Avg $/Sale = Total commissions paid / Total conversions
```

**What good looks like in 2026:**
- Below $30: front-end is too thin OR no upsell stack — risky for paid traffic
- $30-$80: workable for organic and affiliate landing-page funnels
- **$80-$200: target zone for Meta paid traffic**
- $200+: usually high-AOV nutra/info products with strong upsell stacks; great margin but verify refund

[INDUSTRY STANDARD — top ClickBank offers in April 2026 ranged $51-$173 Avg $/sale per ClickBank's official top-offers list]

**How to verify it's not inflated:** Compare Avg $/sale to Initial $/sale. The gap is the upsell value. If Avg = $120 and Initial = $30, you make $30 on the front and the rest depends on the upsell flow converting (and not refunding).

### 2.3 Initial $/Sale

**What it measures:** The commission you earn on the *first* transaction only — before any upsells, downsells, or rebills. [VERIFIED]

**Why it matters more than Avg $/Sale:** Your Meta ad sends a click, the click converts (or doesn't), and you receive credit for the front-end purchase. Whether the customer also buys the $89 upsell is largely outside your control — it depends on the vendor's upsell flow, copy, video, and timing.

**What good looks like in 2026:**
- < $25: front-end too small to absorb realistic Meta CPC + landing page bounce — SKIP
- **$25-$50: minimum viable for cold paid traffic with strong landers**
- **$50-$100: comfortable zone for first-offer testing**
- $100+: typically high-ticket info, energy, or premium nutra; strong margins but harder to justify cold-click conversion

**The trap:** Vendors aggressively market the Avg $/sale ("affiliates earn $147 per sale!"). If the Initial is $32 and you build your CPC math on $147, you are budgeting for revenue that 60-80% of buyers won't generate. **Always model break-even on Initial $/sale; treat upsell revenue as upside.** [PROPOSED based on industry consensus]

### 2.4 Avg %/Sale and Initial %/Sale

**What they measure:** Commission percentage of the sale price.

**What to know:**
- ClickBank caps commission at 75% on most products [VERIFIED]
- Higher percentage isn't automatically better — a 75% commission on a $20 ebook ($15) loses to a 50% commission on a $200 supplement ($100) [INDUSTRY STANDARD]
- Most quality nutra and supplement offers in 2026 sit at 60-75% on the front-end; physical product offers may show 40-60% [PROPOSED]

**The illusion of "75% commission":** A vendor offering 75% on a $17 ebook earns you $12.75. A vendor offering 50% on an $89 product earns $44.50 — roughly 3.5x more per customer. Never optimize for percentage; optimize for absolute dollars per click. [INDUSTRY STANDARD]

### 2.5 Avg Rebill Total / Recurring $/Rebill

**What it measures:** Average commission earned from recurring billing (subscriptions) per rebill cycle.

**Why it matters:** A subscription offer with $30/month rebill at 60% commission ($18/mo to you) generates LTV per customer over 6-12 months that vastly exceeds a single-payment offer. Top affiliates in 2026 increasingly favor rebill offers because:
- LTV math gives you room to overpay on first acquisition
- Compounds revenue across testing cycles (commissions land 3-4 months after first sale)
- Vendor has skin in the game for retention (better product = lower refund)

**What good looks like in 2026:**
- Avg Rebill Total ≥ $40: meaningful LTV uplift
- $80-$150: very strong, justifies higher CPA
- $150+: premium subscription tier — verify retention with vendor

[INDUSTRY STANDARD — recurring nutra and SaaS-style ClickBank offers are the highest-LTV affiliate plays in the marketplace]

**The watch-out:** Rebill commissions get clawed back when subscribers cancel within the refund window (60 days default). The displayed Rebill Total assumes typical churn — verify by asking the vendor directly via the affiliate manager.

### 2.6 Activation % (a.k.a. Conversion Rate / CVR)

**What it measures:** Percentage of clicks that become an *initial* sale, measured over the last 30 days, aggregated across ALL affiliates promoting the offer. [VERIFIED]

**The math:**
```
Activation % = Initial sales / Hops (clicks)
```

**What good looks like in 2026 (per ClickBank's April 2026 top-offers list):**
- 0.5-1.0%: typical for cold paid traffic to direct offer link
- **1.0-2.5%: good — most top offers fall here**
- 2.5%+: exceptional (Rocket Languages showed 6.74% — usually warm/educated traffic)

**Critical caveat:** Activation aggregates ALL traffic — SEO, email, organic, paid. Your Meta cold-traffic activation will almost always be *lower* than the displayed number. Plan for half the displayed activation in your CPC math. [PROPOSED]

### 2.7 EPC — Earnings Per Click

**What it measures:** Average net commission earned per affiliate click in the last 30 days, across all affiliates. [VERIFIED]

**The math:**
```
EPC = Total net commissions / Total hops (clicks)
EPC = Avg $/sale × Activation %
```

**What good looks like in 2026:**
- EPC < $0.50: untestable on Meta unless you have $0.20 CPC traffic source (rare)
- $0.50-$1.50: workable with disciplined audience and landing page
- **$1.50-$3.00: prime testing zone**
- $3.00+: top-tier — usually high-ticket or recurring offers

**The critical interpretation rule:** EPC is **only useful relative to your CPC.**
- If displayed EPC is $1.20 and your Meta cold-traffic CPC is $1.80 → mathematically impossible to break even at displayed activation rates
- If EPC is $2.40 and your CPC is $1.20 → 2x ROAS theoretical ceiling, room to optimize
- If EPC is $2.40 and your CPC is $4.50 → either find cheaper traffic or skip

[INDUSTRY STANDARD — ClickBank's own EPC blog post explicitly says "EPC is only a useful metric relative to what you're spending on traffic sources"]

**Common misinterpretations:**
- **Displayed EPC ≠ Your EPC** — Displayed EPC includes top affiliates with hyper-optimized funnels. Cold paid traffic typically achieves 30-60% of displayed EPC in the first 7 days of testing. [PROPOSED]
- **EPC drops as you scale** — Verified across multiple ClickBank publications. Plan for EPC at $20-50/day spend to be ~70% of EPC at $200+/day spend.

### 2.8 Hops Per Order (Implied Reverse Conversion)

**What it measures:** Inverse of activation — how many clicks it takes to produce one sale on average.
```
Hops Per Order = 1 / Activation %
```

**Threshold guideline [INDUSTRY STANDARD per The Clever Business]:**
- < 100 hops per order: excellent
- 100-200: acceptable
- 200+: indicates either pricing problems on the offer or unconvincing landing page — reconsider

### 2.9 The Refund Rate Problem

**ClickBank does not officially publish refund rates per offer.** [VERIFIED — multiple sources]

**Why this matters:** Refunds reverse your commission. A 30% refund rate effectively reduces your real per-sale earnings by 30% — and Meta has already charged you for the click.

**How to estimate refund rate (industry technique):**
```
Implied Refund Rate ≈ 1 - (Avg $/sale earned / Listed $/sale before refunds)
```
This requires comparing the marketplace-listed $/sale (gross) to what affiliates report netting (post-refund). The gap is your estimate.

**Practical approach for first offer:**

| Niche | Typical refund rate | Notes |
|-------|--------------------|----|
| Health supplements (nutra) | 8-15% | Lower if 60-day money-back is the stated policy |
| Weight loss / diets | 15-25% | Highest in the marketplace — buyers regret quickly |
| MMO / business opportunity | 20-35% | Avoid as first offer |
| Spirituality / new age | 10-18% | Variable — depends on emotional fit |
| Dental / specific health | 5-12% | Often best refund profile |
| Survival / preparedness | 8-15% | Stable buyer base |
| Languages / education | 6-12% | Lower if onboarding is good |

[COMMUNITY WISDOM — Warrior Forum threads on refund rates; broadly aligned across multiple sources but treat as approximations, not guarantees]

**Direct method to check:** Ask the vendor's affiliate manager directly via the email on the tools page. Top vendors will share refund stats; vendors that ghost the question are a red flag.

---

## 3. The 7-Step Offer Evaluation Framework

This is the practical playbook. Run every candidate offer through this in <30 minutes. Skip any step at your peril.

### Step 1 — Initial Numbers Filter (3 minutes)

Open the ClickBank Marketplace, sort by gravity descending, then filter to your target sub-niche.

**Hard filters (auto-disqualify if any are true):**
- Gravity < 15 OR > 200
- Initial $/sale < $25
- Avg $/sale < $40
- Activation < 0.5%
- EPC < $0.80

**Soft filters (flag, don't kill):**
- No rebill component (single-payment only) — flag for risk-of-thin-LTV
- Vendor approval required — note timeline (could be 24-72h delay before testing)
- "Affiliates only" tools page password-protected — note before requesting access

**Prompt for AI evaluator at this stage:**
```
I am evaluating ClickBank offer [NAME / VENDOR ID].
Marketplace stats:
- Gravity: [X]
- Initial $/sale: $[X]
- Avg $/sale: $[X]
- Avg %/sale: [X]%
- Avg Rebill Total: $[X]
- Activation: [X]%
- EPC: $[X]

Run hard filter check against the 5 thresholds in Section 3.1 of the framework.
Output: PASS / FAIL with reason for each filter.
If PASS, proceed to Step 2 with the offer's pitch page URL: [URL]
```

### Step 2 — VSL / Sales Page Deep Review (8 minutes)

Open the offer's pitch page in an incognito browser (the marketplace shows your view; vendors sometimes serve different pages to ClickBank affiliates).

**Watch the VSL with a stopwatch. Note:**

1. **Hook timing** — does the headline + first 30 seconds frame a clear pain point and tease a solution?
2. **Length** — VSL <8 minutes is unusual today; 12-30 minutes is standard for high-AOV; >45 minutes signals either premium offer or padded fluff
3. **Social proof depth** — testimonials with full names + photos + verifiable companies > generic stock photo "Sarah from Texas"
4. **Compliance markers** (CRITICAL — see Section 6):
   - Disease cure claims = AUTO-FAIL for Meta
   - "Doctors hate this" / fake authority = AUTO-FAIL
   - Dramatic before/after with body parts = AUTO-FAIL
   - Anxiety/desperation hooks ("Are you suffering from...") = AUTO-FAIL on Meta 2026
5. **Price reveal timing** — late-reveal indicates high AOV; early-reveal usually means low AOV
6. **Order form quality** — clean, mobile-optimized, single-page > multi-step on mobile

**Prompt for AI evaluator:**
```
I am about to send Meta paid traffic to this VSL: [URL]
Watch/transcribe key claims and tell me:
1. Does the VSL make any disease/cure claims that would violate Meta health policy 2026?
2. Are there before/after images of body parts or dramatic transformations?
3. Are there unverified doctor endorsements?
4. Is the desperation framing ("are you suffering from X") used as a hook?
5. Estimate the page load time on mobile (use any heuristic available).
6. Score compliance risk: LOW / MEDIUM / HIGH
If MEDIUM or HIGH, recommend SKIP for cold Meta traffic.
```

### Step 3 — Tools Page Audit (5 minutes)

Every legitimate ClickBank vendor maintains an affiliate tools page. Find the link on the pitch page footer or via "JV / Affiliates" navigation.

**What to extract:**
- **Allowed traffic sources** — explicit list (Meta, Google, native, email, SEO, YouTube, TikTok)
- **Prohibited traffic** — common bans: brand bidding, incentivized traffic, SMS, fake news pages, Telegram (CB-wide ban as of recent policy update) [VERIFIED]
- **Geo restrictions** — US-only? International OK? Spanish allowed?
- **Approved creatives** — pre-built ad copy, banners, videos? Use as inspiration, never copy verbatim
- **Funnel diagram** — what does the upsell flow look like? Bump? OTOs? Downsells?
- **Affiliate manager contact** — email, Skype, Telegram, Slack
- **Email swipes provided** — quality and recency (last update date)
- **Postback / pixel docs** — does the vendor support S2S CAPI / postback URLs?

**Hard fail triggers:**
- No tools page exists → vendor is amateur or hostile to affiliates → SKIP
- Tools page prohibits paid social → SKIP for Meta
- Tools page hasn't been updated in 12+ months → vendor is asleep
- Affiliate manager email bounces → SKIP

**Prompt for AI evaluator:**
```
Review this affiliate tools page: [URL]
Extract:
1. Allowed traffic sources (list explicitly)
2. Prohibited traffic sources (list explicitly)
3. Geo restrictions
4. Last updated date (if visible)
5. Affiliate manager contact info
6. Whether postback / CAPI integration is documented

Flag any of: prohibits paid social, no AM contact, last-updated > 12 months ago.
```

### Step 4 — Refund Rate Investigation (4 minutes)

Since ClickBank doesn't publish refund rates, triangulate from these sources:

1. **Vendor's customer-facing reviews** — Trustpilot, Reddit (search "[product name] refund"), BBB if US vendor
2. **Affiliate forums** — Warrior Forum, BlackHatWorld, STM forum for established vendors
3. **Direct vendor query** — email the affiliate manager: *"What's the current refund rate for cold Meta traffic over the last 30 days?"* — speed and specificity of answer is itself a signal
4. **Compare $/sale gap** — if vendor shows Initial $/sale = $50 and Avg $/sale = $52, with no rebill, the implied refund-adjusted earnings are roughly $30-35 (suggesting ~30-40% refund + minimal upsell)

**Hard fail trigger:** Vendor refund rate > 25% (or AM ghosts the question). [INDUSTRY STANDARD]

### Step 5 — Competitive Landscape Check (5 minutes)

Use Meta Ad Library + at least one ad spy tool to confirm the offer is currently being run profitably.

**Tools (free + paid):**
- **Meta Ad Library** (free) — search the offer name, vendor brand, or pitch page domain. Note: only shows active ads; archived ads disappear.
- **Foreplay / Atria / Magic Brief** — paid alternatives to the now-dead AdSpy; 2026 leaders for Meta creative spying
- **BigSpy** — free tier; useful for breadth scan
- **AdLibrary alternatives** — TikTok Creative Center, Google Ad Transparency Center for cross-channel

**What to look for:**
- 5+ active advertisers running the offer = validation that someone is profitable
- Ad creative diversity (multiple angles, hooks, audiences) = mature winning offer
- Same advertiser running ads for 30+ days continuously = profitable funnel
- Zero ads despite high gravity = red flag (gravity may be from email/SEO traffic; Meta may not work)

**Prompt for AI evaluator:**
```
For the ClickBank offer [NAME] with pitch page [URL]:
1. Search Meta Ad Library for ads pointing to this domain. List active advertisers and ad count.
2. Identify the dominant ad angles (problem-aware, solution-aware, social proof, authority, etc.)
3. Estimate how mature the winning angle is (1-30 days = early; 60+ days = saturated).
4. Identify any LATAM-targeted ads (Spanish copy, MX/CO/AR/CL/PE targeting).
Output: brief competitive map.
```

### Step 6 — Economics Math (5 minutes)

This is the make-or-break math. Run the calculator in Section 5 before any go/no-go decision. **No exceptions.**

### Step 7 — Final Go/No-Go Decision Matrix

Use this scoring rubric. Total score determines action.

| Criterion | Weight | Pass (1) | Fail (0) |
|-----------|--------|---------|---------|
| Gravity in 30-150 range | 1.0 | Yes | No |
| Initial $/sale ≥ $40 | 1.5 | Yes | No |
| Avg $/sale ≥ $80 | 1.0 | Yes | No |
| EPC ≥ $1.50 | 1.5 | Yes | No |
| Activation ≥ 1.0% | 1.0 | Yes | No |
| VSL compliance LOW or MEDIUM (not HIGH) | 2.0 | Yes | AUTO-FAIL |
| Tools page exists + allows paid social | 1.5 | Yes | No |
| Vendor 12+ months on ClickBank | 1.0 | Yes | No |
| Estimated refund rate ≤ 15% | 1.5 | Yes | No |
| Active competitive landscape (5+ Meta advertisers, mature) | 1.0 | Yes | No |
| Max CPC for 1.3x ROAS ≥ projected Meta CPC | 2.0 | Yes | AUTO-FAIL |
| **TOTAL POSSIBLE** | **15.0** | | |

**Decision thresholds:**
- 12.0+ : TEST CANDIDATE — proceed to creative + landing page build
- 9.0-11.9 : BORDERLINE — only test if you have a strong creative angle hypothesis
- < 9.0 : SKIP — find a better candidate

---

## 4. Niche Map 2026

[INDUSTRY STANDARD — derived from ClickBank's own published top-offers list April 2026, ClickBank's 10-best-niches blog, and cross-publication consensus]

### Top performing categories (rank by displayed top-offer payouts April 2026)

| Rank | Category | Hot in 2026? | Average top-offer AOV | Saturation |
|------|----------|-------------|---------------------|------------|
| 1 | Dietary Supplements (Nutra) | YES | $120-200+ | HIGH |
| 2 | Beauty | RISING FAST | $80-150 | MEDIUM |
| 3 | Men's Health | STABLE | $100-180 | MEDIUM-HIGH |
| 4 | E-business / MMO | SURGING | Varies $20-300 | HIGH |
| 5 | Spirituality / New Age | DECLINING | $40-120 | MEDIUM |
| 6 | Diets & Weight Loss (digital) | EVERGREEN | $30-90 | VERY HIGH |
| 7 | Women's Health | UNDERSERVED | $80-160 | MEDIUM-LOW |
| 8 | Dental Health | UNDERSERVED | $100-180 | LOW-MEDIUM |
| 9 | Survival / Prepper | STABLE | $50-120 | MEDIUM |
| 10 | Home & Garden | NICHE | Varies | LOW |

### Health & Fitness sub-niche map (the most important slice for first-time affiliates)

| Sub-niche | Saturation 2026 | Typical AOV | LATAM fit | First-offer recommendation |
|-----------|-----------------|------------|-----------|------------------------------|
| Weight loss (general) | OVERSATURATED | $80-200 | HIGH demand | AVOID — top offers run by 7-figure buyers |
| Sleep / insomnia | MEDIUM | $50-150 | HIGH | GOOD candidate; Derila Ergo-style offers convert in Spanish |
| Joint pain | MEDIUM-HIGH | $80-160 | HIGH | OK with strong angle |
| Prostate health | MEDIUM | $100-180 | MEDIUM (older male demo) | GOOD if you have male 50+ audience |
| Menopause | UNDERSERVED | $80-150 | MEDIUM-HIGH | EXCELLENT opportunity |
| Energy / focus | MEDIUM (brain song surge) | $50-120 | HIGH | Crowded but workable |
| Diabetes / blood sugar | HIGH but compliance-risky | $100-200 | VERY HIGH | RISKY — disease claim landmine |
| Skin care | MEDIUM (rising) | $60-130 | HIGH | GOOD candidate |
| Hair loss | MEDIUM | $80-160 | HIGH | OK with strong before/after-free angle |
| Sexual health | MEDIUM | $80-180 | HIGH | Compliance-tricky on Meta |
| Pelvic floor / bladder (women) | UNDERSERVED | $80-140 | MEDIUM | EXCELLENT for differentiation |
| Dental supplements | UNDERSERVED | $130-180 | MEDIUM-HIGH | EXCELLENT first-offer category |

### LATAM Spanish-speaking demographic preferences

[INDUSTRY STANDARD — affmaven, RichAds, ClickBank LATAM analyses]

- **Mexico, Colombia, Peru** lead opportunity. Argentina + Chile smaller but higher AOV tolerance.
- **Doctor authority outperforms celebrity endorsements** — opposite of US market in many verticals
- **Mobile-first is non-negotiable** — 70%+ traffic; landing pages must load <3s on 3G
- **Local Spanish > generic translation** — Mexican Spanish ≠ Spanish from Spain ≠ Argentinian. Test "tú" vs "usted" — varies by country
- **Average monthly income $700** — positions LATAM as Tier-2/3 traffic; CPCs $0.01-0.10 on Meta possible but conversion thresholds shift
- **Payment methods** — many LATAM buyers struggle with US-based USD checkout. Verify with vendor whether they support OXXO (MX), PSE (CO), boleto (BR), or local processors
- **Cultural angles that convert** — health/wellness, family-protection framing, financial-anxiety relief, traditional/natural remedy framing
- **Cultural angles to avoid** — direct sexual content, US-political angles, "lose weight for the beach" body-shaming narratives

---

## 5. Economics Calculator with Worked Examples

The single most important framework in this document. Use it before every test.

### 5.1 The Core Math

```
GIVEN:
  AOV (Average Order Value the customer pays) = $A
  Commission % to affiliate = C%
  Estimated landing page CTR (click → VSL view) = L%
  Estimated VSL conversion rate (VSL view → sale) = V%
  Combined funnel CVR (cold click → sale) = L% × V%
  Realistic Meta CPC (cold traffic) = $K

DERIVE:
  Net commission per sale (front-end only) = $A × C% = $N
  Required clicks per sale = 1 / (L% × V%)
  Cost to generate one sale (at $K CPC) = K / (L% × V%)
  Effective EPC = $N × L% × V%

DECISION RULES:
  Max CPC for 1.0x ROAS (break-even) = $N × L% × V%
  Max CPC for 1.3x ROAS (sustainable) = ($N × L% × V%) / 1.3
  Max CPC for 2.0x ROAS (winner threshold) = ($N × L% × V%) / 2.0

  If max CPC for 1.3x ROAS < your projected Meta CPC → SKIP
  If equal → BORDERLINE (test cautiously, $50/day budget cap)
  If higher → TEST CANDIDATE
```

[INDUSTRY STANDARD math, structured per the Berso Marketing breakeven ROAS framework adapted for affiliate / commission-based offers]

### 5.2 Worked Example A — Low-AOV digital offer (the trap)

**Offer:** "Manifest Your Best Life" — manifestation ebook
- AOV = $37
- Commission = 75%
- Net commission per sale = $27.75
- Estimated funnel CVR (cold Meta traffic) = 1.0%
- Effective EPC = $27.75 × 0.01 = **$0.28**

**Max CPCs:**
- Break-even = $0.28
- 1.3x ROAS = $0.21
- 2.0x ROAS = $0.14

**Projected Meta CPC for warm Tier-1 audience: ~$1.20**

**Verdict: SKIP.** The math is structurally impossible. Even at theoretical break-even you cannot afford the click. Common first-offer mistake: high-percentage commission on low-AOV blinds the affiliate to absolute dollars per click.

### 5.3 Worked Example B — Mid-AOV nutra offer (typical workable offer)

**Offer:** "Joint Genesis 2.0" — joint health supplement
- AOV = $89 (with bump)
- Commission = 60% on initial
- Net commission per sale (initial only) = $53.40
- Avg Rebill = $35/quarter, expected 1.5 rebills per buyer over 90 days = $52.50 LTV uplift, but DON'T model into break-even
- Estimated funnel CVR (cold Meta traffic) = 1.2%
- Effective EPC (initial only) = $53.40 × 0.012 = **$0.64**

**Max CPCs:**
- Break-even (initial) = $0.64
- 1.3x ROAS = $0.49
- 2.0x ROAS = $0.32

**Projected Meta CPC for joint pain audience (50+ targeting, US): ~$0.80**

**Verdict: BORDERLINE.** Initial math is tight. But the rebill upside makes this testable IF: (a) you can verify rebill retention with vendor, and (b) you're willing to lose money on initial test cycle to fund real ROAS measurement at day 60-90. NOT a first offer for $300-500 capital — too long a payback window.

### 5.4 Worked Example C — High-AOV nutra with strong upsell stack (target profile)

**Offer:** "ProDentim-style" dental supplement
- Initial $/sale = $89 (your front-end commission)
- Avg $/sale (with upsell stack) = $173
- Activation displayed = 0.8% (use 0.6% for cold Meta math = 0.75x discount)
- Effective EPC at displayed = $173 × 0.008 = $1.38
- Effective EPC at conservative cold-traffic estimate = $89 × 0.006 = **$0.53** (initial only) PLUS upsell upside

**Max CPCs (initial-only model — conservative):**
- Break-even = $0.53
- 1.3x ROAS = $0.41
- 2.0x ROAS = $0.27

**Max CPCs (Avg $/sale model — optimistic, only valid if you trust the upsell stack):**
- Break-even = $1.04
- 1.3x ROAS = $0.80
- 2.0x ROAS = $0.52

**Projected Meta CPC for dental health audience: ~$0.60-0.90**

**Verdict: TEST CANDIDATE.** Initial-only math is borderline; full-funnel math is workable. Recommended approach: budget the test assuming initial-only commission (conservative); if you hit break-even or better at initial-only by day 7, you know the upsell stack will push you to 1.5-2.0x ROAS. This is the prototypical good first-offer candidate.

### 5.5 Quick-reference CPC table

For a given Net Commission ($N) and Funnel CVR, the break-even CPC = $N × CVR.

| Net Commission | 0.5% CVR | 1.0% CVR | 1.5% CVR | 2.0% CVR |
|----------------|---------|---------|---------|---------|
| $25 | $0.13 | $0.25 | $0.38 | $0.50 |
| $40 | $0.20 | $0.40 | $0.60 | $0.80 |
| $60 | $0.30 | $0.60 | $0.90 | $1.20 |
| $80 | $0.40 | $0.80 | $1.20 | $1.60 |
| $100 | $0.50 | $1.00 | $1.50 | $2.00 |
| $150 | $0.75 | $1.50 | $2.25 | $3.00 |

**Read this table:** the cell value is your break-even CPC. Divide by 1.3 to get sustainable-CPC; by 2.0 to get winner-CPC. Compare to the realistic Meta CPC for your audience.

---

## 6. Red Flags vs Green Flags Scoring Rubric

### Red Flags — Hard Fail Criteria

Any one of these = SKIP, no further evaluation needed.

| Red Flag | Why it kills the offer |
|----------|----------------------|
| Disease cure / treat / prevent claims in VSL | Auto-disapproval on Meta health policy [VERIFIED] |
| Vendor's tools page prohibits paid social/Meta | You can't run Meta even if you wanted to |
| AOV < $50 | Front-end too thin for realistic Meta CPCs |
| Initial $/sale < $25 | Math impossible to break even at scale |
| Estimated refund rate > 25% | Even break-even funnel becomes net-negative |
| Single-payment only AND no upsell stack | No LTV, no flexibility |
| US-only checkout for LATAM target | Buyers can't complete purchase |
| No CAPI / postback documentation | Meta optimization blind, scaling impossible |
| Affiliate manager unresponsive >72h | Vendor will ghost when you have a real problem |
| Vendor < 6 months on ClickBank with single product | Pump-and-dump risk pattern |
| Tools page hasn't been updated in 12+ months | Vendor is asleep or out of business |
| Before/after body imagery in VSL | Meta auto-disapproval [VERIFIED] |
| "Doctors hate this" / unverified medical authority | Meta auto-disapproval + customer skepticism |
| Brand bidding required to compete | Meta won't allow brand bidding via affiliate links |
| Telegram-only support | ClickBank prohibits Telegram as traffic source [VERIFIED] |

### Green Flags — Strong Positive Signals

Tally these. The more you have, the higher confidence.

| Green Flag | Why it matters |
|-----------|---------------|
| Vendor 3+ years on ClickBank, 3+ products | Established business, refund handling tested |
| Recurring rebill component documented | LTV math gives you CPC headroom |
| Clean, mobile-optimized VSL <30s load time | Reduces bounce, improves CVR |
| Postback / CAPI documentation explicit | Meta optimization actually works |
| Spanish-language version with native localization | LATAM-ready, larger TAM |
| Affiliate manager replies within 24h with specifics | Real human, real support |
| Tools page updated in last 90 days | Active vendor relationship |
| Public webinars / Slack / FB group for affiliates | Community support, faster learning |
| 5+ active Meta advertisers with diverse angles (Ad Library) | Validated cold-traffic profitability |
| Reasonable refund rate self-reported (5-15%) | Vendor transparency + product quality |
| Working pixel + tested order form on mobile | No tech surprises mid-test |
| Multiple price points / OTOs in funnel | Upsell engine = revenue floor + ceiling |
| Documented A/B test results shared with affiliates | Vendor invests in optimization, sales-page evolves |
| Affiliate-only Slack / Discord with active discussion | Better reps, faster intel on what's working |

### Composite scoring

Use the weighted matrix from Section 3.7. Critical: a single AUTO-FAIL (compliance, math impossible) overrides any number of green flags. **Don't fall in love with a vendor whose VSL will kill your ad account.**

---

## 7. Tools and Resources Beyond ClickBank Marketplace

[INDUSTRY STANDARD — verified pricing as of mid-2026; check current pricing before subscribing]

### Marketplace research tools

| Tool | What it shows | Pricing 2026 | Worth it? |
|------|---------------|--------------|-----------|
| **CB Engine (cbengine.com)** | Historical gravity charts, top movers, recent gravity trends, vendor history | 7-day free trial; ~$27 lifetime Pro | YES — historical gravity is critical signal not in CB marketplace |
| **CBSnooper (cbsnooper.com)** | Historical product data, gravity tracking, top-products reports | Subscription tiers | Alternative to CB Engine; redundant if you have one |
| **OfferVault** | 70,000+ offers across 50+ networks (not just CB) | Free | YES — broaden beyond CB before committing |
| **CBProAds** | Vendor metrics, sales page analysis | Subscription | Optional |

### Ad spy / competitive intelligence

| Tool | Use case | Pricing 2026 |
|------|----------|--------------|
| **Meta Ad Library** | Active Meta ads — primary check | Free |
| **TikTok Creative Center** | TikTok ads inspiration | Free |
| **Google Ad Transparency Center** | Google active ads | Free |
| **Foreplay** | Meta ad spy with strong filters | $50-200/mo |
| **Atria** | Modern AdSpy successor | $100+/mo |
| **Magic Brief** | Creative analysis at scale | $100+/mo |
| **BigSpy** | Free tier broad scan; paid for depth | Free + paid tiers |

### Vendor reputation cross-reference

- **Trustpilot** — search vendor brand + product
- **BBB** (US vendors only) — complaint patterns
- **Reddit** — search "[product name] refund" or "[product name] scam"
- **Warrior Forum / BlackHatWorld** — affiliate-side complaints
- **STM Forum** (paid) — premium affiliate community discussions

### Tracking infrastructure

- **AnyTrack** — pixel + CAPI integration with ClickBank documented
- **Voluum** — premium affiliate tracker with full S2S
- **wecantrack** — alternative integration platform
- **ClickMagick** — affiliate-focused link tracker
- **Native ClickBank S2S Meta integration** — free, configured via Integrations → Postback/Pixels → Add Integration → Facebook [VERIFIED — ClickBank docs]

### Alternative networks (when ClickBank is wrong fit)

| Network | Strength | When to consider |
|---------|----------|------------------|
| **MaxWeb** | Top VSL nutra offers, paid social focus | When ClickBank gravity is too saturated in nutra |
| **Digistore24** | EU + LATAM strength, 8,500 offers | When LATAM-specific localization needed |
| **JVZoo** | Info products, MMO | When MMO is your niche |
| **Warrior+** | MMO and digital | Niche-specific |
| **DrCash, ShakesPro, Limonad** | Pure nutra CPA networks | When you've outgrown CB nutra |

---

## 8. First Offer Recommendation Framework

For someone starting fresh in 2026 with $2-3K capital, LATAM focus, and zero prior ClickBank wins.

### The "training wheels" offer profile

The ideal first offer optimizes for **learning velocity, not maximum profit.** Pick an offer where:

1. **Math works at conservative assumptions** — break-even achievable at 0.6% CVR and Tier-2 LATAM CPCs
2. **Compliance is structurally safe** — niches where Meta rarely auto-disapproves (sleep, dental, beauty, energy)
3. **Vendor is a known quantity** — 2+ years on ClickBank, multiple products, active AM
4. **Audience is well-defined and addressable** — clear demographic targetable on Meta (e.g., women 45-65 interested in beauty)
5. **You can build a competent landing page in 1-2 days** — not a 3-week creative project
6. **There's an existing winning angle to model** — Meta Ad Library shows 3-10 active advertisers you can study

### Attributes that make a good "training wheels" offer

| Attribute | Why |
|-----------|-----|
| Gravity 30-100 | Proven but not 7-figure-buyer infested |
| AOV $80-150 | Front-end commission of $50-90 — workable on Meta |
| Recurring rebill component | LTV cushion forgives early test losses |
| LATAM Spanish version with native localization | Tier-2 traffic costs while still earning USD |
| Vendor offers Spanish AM and Spanish customer support | Refund rate stays low |
| Underserved sub-niche (dental, menopause, pelvic floor, sleep) | Less competitive auction, easier to differentiate |
| Compliance-clean VSL (no disease cures, no before/after) | Ad account survives the test |
| Tools page documents Meta CAPI integration | Optimization and scaling actually work |

### Common first-offer mistakes (avoid)

1. **Picking the #1 gravity offer** — it's the most competitive in the marketplace; 7-figure buyers have already inflated every audience cost
2. **Optimizing for highest commission %** — 75% of $20 < 50% of $100
3. **Ignoring rebill component** — losing free LTV that funds your testing
4. **Picking a "guru" offer in MMO niche** — refund rates 25-35%, hostile audiences, compliance landmines
5. **Picking a US-only weight loss offer for LATAM traffic** — checkout fails, refund rate spikes
6. **Trusting displayed Activation/EPC for cold Meta traffic** — these include all traffic; cold Meta will hit ~50-70% of displayed
7. **Not contacting the affiliate manager** — you lose the most important due-diligence channel
8. **Spending the entire $300-500 on first creative without iteration budget** — keep $200 reserve for v2 creative if v1 underperforms

### First-offer "go" checklist

Before launching, confirm ALL of these:

- [ ] Score on Section 3.7 matrix is 12.0 or higher
- [ ] Affiliate manager has replied to at least one specific question
- [ ] CAPI / postback integration is configured and tested with a real conversion
- [ ] Landing page (yours, not vendor's) loads in <3s on mobile 3G
- [ ] You have at least 3 Meta creative variants (per OpenClaw quality rules) ready to launch
- [ ] You have 5+ Meta Ad Library ads from competitors saved as reference
- [ ] Hop link tracking ID structure decided (see Section 9 below)
- [ ] $50/day budget cap set; $300-500 total kill budget defined
- [ ] Pause / kill rules written down BEFORE launch (e.g., "if CPA > 2x target after 50 clicks, kill")
- [ ] Vendor terms of service screenshot saved (in case it changes mid-test)

---

## 9. Templates Ready to Use

### 9.1 Tracking ID convention

Use ClickBank tracking parameters (TIDs) to slice performance by source, campaign, ad set, and creative.

**Format:**
```
?tid=[platform]-[campaign]-[adset]-[creative]
```

**Examples:**
```
?tid=fb-jointgenesis-women45plus-vsl1
?tid=fb-jointgenesis-women45plus-static2
?tid=fb-prodentim-mx-spanish-v3
?tid=tt-brainsong-students-hook2
```

**Hard rules:**
- Lowercase only (CB tracking params are case-sensitive in some reports)
- No spaces, use hyphens
- Max 24 characters total per ClickBank limits — keep abbreviated
- Document the convention in a shared sheet so you can decode any TID 6 months later

### 9.2 UTM strategy (alongside TID)

ClickBank's TID handles affiliate-side tracking. UTMs handle YOUR analytics on the bridge / landing page if you use one.

```
utm_source=facebook
utm_medium=cpc
utm_campaign=[offer-slug]-[geo]-[YYYYMM]
utm_content=[creative-id]
utm_term=[audience-name]
```

### 9.3 CAPI / postback URL for ClickBank S2S Meta integration

**Setup steps (per ClickBank official docs):**
1. ClickBank Account → Integrations → Postback/Pixels → Add Integration → Facebook
2. Name it (e.g., "FB-OfferName-MainAccount")
3. Select role = Affiliate
4. Enter your verified Facebook domain
5. Set Integration Level = Custom; filter by `traffic_source=facebook`
6. Append `&fbclid={fbclid}&traffic_source=facebook` to your hop link
7. Test with a real $1 purchase, verify event arrives in Meta Events Manager within 30 minutes

### 9.4 First-offer evaluation worksheet

```
OFFER EVALUATION — [DATE]

Offer name: ________________
Vendor nickname: ____________
Pitch page URL: _____________
Tools page URL: _____________
Affiliate manager email: _____

MARKETPLACE STATS:
Gravity: ___ (target: 30-150)
Initial $/sale: $___ (target: $40+)
Avg $/sale: $___ (target: $80+)
Avg Rebill Total: $___
Activation %: ___ (target: 1.0%+)
EPC: $___ (target: $1.50+)

VSL COMPLIANCE CHECK:
Disease claims? Y/N (auto-fail if Y)
Before/after body imagery? Y/N (auto-fail if Y)
Unverified doctor endorsement? Y/N (auto-fail if Y)
Desperation hook? Y/N (auto-fail if Y)
Compliance score: LOW / MEDIUM / HIGH

TOOLS PAGE CHECK:
Meta paid social allowed? Y/N
LATAM/Spanish allowed? Y/N
Last updated: _____ (months ago: ___)
CAPI integration documented? Y/N

REFUND CHECK:
Trustpilot complaints about refunds? Y/N
Reddit/forum complaints? Y/N
AM responded to refund-rate question? Y/N (response: _____)
Estimated refund rate: ___%

COMPETITIVE LANDSCAPE:
Active Meta advertisers (Ad Library): ___
Dominant angle: ____________
LATAM Spanish ads visible? Y/N
Mature winning angle (60+ days)? Y/N

ECONOMICS:
Net commission per sale (initial only): $___
Estimated cold-traffic CVR: ___%
Effective initial-only EPC: $___
Projected Meta CPC for target audience: $___
Max CPC for 1.3x ROAS: $___
Math verdict: PASS / BORDERLINE / FAIL

DECISION SCORE (Section 3.7 matrix): ___ / 15

FINAL DECISION: TEST / BORDERLINE / SKIP
```

### 9.5 Affiliate manager outreach template

```
Subject: Affiliate inquiry — [Offer name] — Meta paid traffic, LATAM focus

Hi [AM Name],

I'm planning to test [offer name] with Meta paid traffic targeting [Mexico/Colombia/etc.] in Spanish. Before I launch, three quick questions:

1. What's the current refund rate for cold Meta traffic over the last 30 days?
2. Do you have Spanish-localized creatives or VSL versions for LATAM markets?
3. Is the CAPI/postback integration with Meta currently documented and tested?

I'm starting with a $300-500 test budget and plan to scale aggressively if the math works. Looking forward to building a long-term relationship if this offer fits.

Thanks,
[Your name]
ClickBank nickname: [your nickname]
```

Speed and specificity of the AM reply is itself a top-three signal in your evaluation. A vendor whose AM responds within 24h with specific numbers is a vastly better partner than one with the higher displayed gravity.

---

## 10. The "Second Offer" Question

Once your first offer is profitable (1.3x+ ROAS over 14+ days at meaningful spend), the natural next question is what to test next.

### When to add a second offer

[PROPOSED based on industry consensus]
- **Don't add a second offer until the first is consistently profitable for 30+ days** — splitting attention prematurely kills both
- **Don't add a second offer until you've scaled the first to its ceiling** — defined as the spend level where ROAS drops below your target despite optimization
- **DO add a second offer when the first plateaus AND you have learnings to apply to a new candidate**

### Same vendor, different product (lowest risk)

**When this is right:** The vendor has multiple offers in the same niche, you have established AM relationship, your audience research transfers, your funnel architecture transfers.

**Example:** You've won with a sleep supplement. Same vendor offers a stress-relief supplement targeting same demographic. You can reuse audience signals, copy patterns, lander template.

### Same niche, different vendor (medium risk)

**When this is right:** Your sub-niche is proven but you've hit ceiling on first offer's funnel. New vendor offers different angle, price point, or upsell stack.

**Cannibalization risk:** Same audience seeing both your ads. Mitigate by exclusion audiences and angle differentiation.

### Different niche entirely (highest risk)

**When this is right:** You've maxed out your first niche and have established creative production pipeline ready to repurpose. Treat as a new test cycle, not an extension.

**Common mistake:** Diversifying across niches before any single one is profitable. **Win one niche before adding the second.**

---

## Closing — The Honest Truth About First Offers

Most first offers lose money. That's not a defect — it's the cost of learning the platform, the audience, the creative angles, and the vendor relationships that will fund the second, third, and tenth offers.

The goal of this framework isn't to guarantee a winner on offer #1. It's to:

1. **Eliminate the structurally impossible offers** — math that can never work, compliance that will ban your account, vendors that will ghost you
2. **Maximize the chance that you LEARN from the test** — if you lose, you should know exactly why (CPC was too high, CVR was too low, refund rate killed it, creative didn't break through)
3. **Preserve capital for the second test** — never go all-in on offer #1; always reserve 50% of capital for iteration

If you can run 3-4 disciplined tests using this framework with $300-500 each, the probability that one of them is profitable is far higher than the probability that a single $1,500-2,000 test on a hyped offer is profitable. **Test cycles, not single bets.**

This document gets re-read every Monday before you pick the next offer to test. The frameworks don't change; the offers do.

---

## Sources Reference

- ClickBank — official Gravity Score blog: https://www.clickbank.com/blog/clickbank-gravity-score/
- ClickBank — Marketplace Stats: https://support.clickbank.com/en/articles/10535274-how-do-i-use-the-clickbank-marketplace-stats
- ClickBank — Top Offers April 2026: https://www.clickbank.com/blog/clickbank-top-offers/
- ClickBank — 10 Best Niches: https://www.clickbank.com/blog/best-affiliate-marketing-niches/
- ClickBank — Health & Fitness affiliate guide: https://www.clickbank.com/blog/health-fitness-affiliate-marketing
- ClickBank — EPC explained: https://www.clickbank.com/blog/what-is-earnings-per-click-aka-epc/
- ClickBank — Meta S2S Integration: https://support.clickbank.com/en/articles/10535369-s2s-tracking-integration-meta-facebook-pixel
- ClickBank — Affiliate Tracking Parameters: https://support.clickbank.com/en/articles/10535262-affiliate-tracking-parameters
- ClickBank — Advertising Guidelines: https://support.clickbank.com/hc/en-us/articles/360042538932-Advertising-Guidelines
- White Hat Crew — Gravity calculation deep dive: https://whitehatcrew.com/blog/how-clickbanks-gravity-is-calculated/
- The Clever Business — ClickBank statistics: https://thecleverbusiness.com/clickbank-statistics-and-terminology-explained/
- AffNinja — CB Engine review: https://affninja.com/cb-engine-review/
- AffMaven — LATAM Affiliate 2026: https://affmaven.com/latam-affiliate-arbitrage/
- Forge Digital Marketing — Meta supplement compliance 2026: https://forgedigitalmarketing.com/how-to-advertise-supplements-on-meta/
- Audit Socials — Meta Health & Wellness 2026: https://www.auditsocials.com/blog/meta-health-wellness-restricted-ads-2026-supplements-body-image-medical-claim-rules
- Berso Marketing — Breakeven ROAS calculator: https://bersomarketing.com/breakeven-roas-calculator/
- RichAds — Nutra vertical 2026: https://richads.com/blog/full-guide-on-nutra-vertical-in-affiliate-marketing-in-2022/
- Affilorama — 20 ClickBank alternatives 2026: https://www.affilorama.com/blog/alternatives-to-clickbank
- ClickBank — Alternatives blog: https://www.clickbank.com/blog/clickbank-alternatives/
- Meta Transparency — Health and Wellness policies: https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/

---

*Last updated: 2026-05-11. Re-validate metric thresholds quarterly — Meta CPC dynamics and ClickBank marketplace mix shift.*
