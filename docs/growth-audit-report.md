# Growth & QA Audit Report — Ai Hiểu Bạn
**Date:** 2026-04-09 | **Author:** Hoa (Growth Lead / QA) | **Status:** Initial Audit

---

## 1. SEO ANALYSIS

### Current State (After Fixes)
- Title tag: "Ai Hiểu Bạn — Người bạn AI luôn hiểu và đồng hành cùng bạn" (good, ~55 chars)
- Description: 150 chars, includes key terms (good)
- Keywords: 13 keywords added
- Open Graph: Added (vi_VN locale, image placeholder)
- Twitter card: Added (summary_large_image)
- `lang="vi"` set on html tag (good)
- Be Vietnam Pro font (Vietnamese-optimized, good)
- `metadataBase` set to aihieuban.vn (needs domain purchase)

### Missing SEO Elements
- [ ] **OG image** — `/public/og-image.png` (1200x630) not created yet
- [ ] **Favicon** — needs custom favicon, not Next.js default
- [ ] **robots.txt** — needs explicit allow/disallow
- [ ] **sitemap.xml** — not generated
- [ ] **Structured data** (JSON-LD) — WebApplication schema
- [ ] **Page-level meta** — chat pages, pricing page need unique titles
- [ ] **Canonical URLs** — set for all pages
- [ ] **Alt text** — character images need descriptive alt text (Vietnamese)

### Vietnamese SEO Keywords (Priority Ranked)

| # | Keyword | Search Intent | Volume Est. |
|---|---------|---------------|-------------|
| 1 | trò chuyện với AI | discovery | High |
| 2 | AI tâm sự | emotional need | High |
| 3 | chatbot tiếng Việt | functional | High |
| 4 | bạn AI | companion search | Medium |
| 5 | nhân vật AI anime | specific interest | Medium |
| 6 | AI hiểu mình | emotional need | Medium |
| 7 | chat với nhân vật ảo | discovery | Medium |
| 8 | ứng dụng tâm sự | mental health | Medium |
| 9 | AI đồng cảm | emotional need | Low-Med |
| 10 | tạo nhân vật AI | creation intent | Low-Med |
| 11 | AI an ủi | emotional need | Low |
| 12 | bạn ảo AI | companion | Low |
| 13 | app tâm sự ẩn danh | privacy-focused | Med |
| 14 | AI giải stress | wellness | Med |
| 15 | chat AI miễn phí | price-sensitive | High |
| 16 | AI người yêu ảo | romantic (careful) | High |
| 17 | anime AI chat | niche | Low |
| 18 | trợ lý ảo tiếng Việt | functional | Med |
| 19 | AI tư vấn tâm lý | mental health | Med |
| 20 | chat bot thông minh | discovery | Med |
| 21 | AI cho người cô đơn | emotional | Med |
| 22 | ứng dụng AI Việt Nam | local discovery | Med |

### SEO Content Strategy
- **Blog/landing pages** (post-MVP): Create pages targeting "AI tâm sự", "chat AI miễn phí", "AI cho người cô đơn"
- **Character pages** should be indexable with unique meta titles: "Chat với [Tên] — Nhân vật AI [tính cách]"
- **FAQ page** targeting long-tail: "AI có hiểu cảm xúc không?", "Chat với AI có an toàn không?"

---

## 2. CONTENT STRATEGY

### Character Personality Types for Vietnamese Gen Z

| Archetype | Vietnamese Name | Why It Resonates |
|-----------|----------------|------------------|
| **Người chị/anh hiền lành** | Hiền, Minh Anh | Vietnamese respect for anh/chị figure |
| **Bạn thân vui vẻ** | Hương, Tuấn | Gen Z wants fun + understanding |
| **Người lắng nghe trầm lặng** | Linh, Khôi | For introverts who need quiet support |
| **Motivator/truyền cảm hứng** | Phúc, Thảo | Academic pressure relief |
| **Nghệ sĩ mơ mộng** | Mai, Sơn | Creative outlet companion |
| **Tsundere anime** | Yuki, Haruto | Anime fans love this trope |

### Vietnamese Cultural Pain Points (Content Angles)
1. **Áp lực học tập** — thi đại học, điểm số, kỳ vọng gia đình
2. **Cô đơn giữa đám đông** — có bạn bè nhưng không ai hiểu mình
3. **Mâu thuẫn gia đình** — bố mẹ không hiểu, generation gap
4. **Áp lực công việc đầu tiên** — lương thấp, sếp khó, so sánh bạn bè
5. **Tình cảm** — crush, chia tay, không dám nói
6. **Tự ti ngoại hình** — body shaming, chuẩn đẹp xã hội
7. **Lo âu về tương lai** — không biết mình muốn gì

### Social Media Content Ideas

#### TikTok (Priority #1)
- "Chat với AI và phản ứng bất ngờ" — screen record real chat
- "AI này hiểu mình hơn bạn thân" — emotional reaction format
- "Kể cho AI nghe chuyện buồn" — vulnerability content
- "Tạo nhân vật anime và chat thử" — product demo
- "Khi AI nói đúng tâm trạng mình" — relatable moments
- Sound: trending Vietnamese audio + text overlay

#### Facebook
- Longer story posts: "Câu chuyện: Khi mình tìm được AI hiểu mình"
- Character introductions with backstories
- User testimonials (anonymous)
- Memes about "không ai hiểu mình"
- Community polls: "Bạn muốn tâm sự điều gì?"

#### Zalo
- Official Account for updates
- Direct character chat teasers
- Payment confirmation + tier updates

### Vietnamese Copywriting

**Hero section:** "Luôn có ai hiểu bạn" ✓ (current is good)

**CTAs:**
- "Tâm sự ngay" (Talk now)
- "Thử miễn phí" (Try free)
- "Nâng cấp Premium" (Upgrade)
- "Bắt đầu trò chuyện" (Start chatting) ✓

**Pricing page copy suggestions:**
- Free tier: "Trải nghiệm cơ bản — 10 tin nhắn/ngày"
- Premium: "Không giới hạn — Thoải mái tâm sự mọi lúc"
- CTA: "Nâng cấp chỉ 79.000đ/tháng — Rẻ hơn một ly trà sữa"

---

## 3. UX AUDIT

### Homepage (`page.tsx`) — Score: 7.5/10
**Good:**
- Clean hero section with clear value proposition
- Character grid with gender filter tabs
- Featured section draws attention
- Loading skeletons (good UX)
- Guest can browse without login

**Issues:**
- [ ] **No empty state for errors** — if API fails, no feedback shown
- [ ] **Hero CTA "Bắt đầu trò chuyện"** links to `/tro-chuyen/1` (hardcoded character ID = fragile)
- [ ] **No character count** — "Tất cả nhân vật" doesn't show "(10)" count
- [ ] **No search** — with 10 chars it's fine, but needed when more are added
- [ ] **Missing "Tạo nhân vật" CTA** on homepage for logged-in users (currently cut from MVP, but button exists in nav)

### Layout (`layout.tsx`) — Score: 8/10
**Good:**
- Vietnamese font (Be Vietnam Pro) with proper subsets
- Sidebar + bottom nav responsive pattern
- Auth initializer on mount
- Toast notifications

**Issues:**
- [ ] **No error boundary** — if React crashes, blank screen
- [ ] **No 404 page** — missing `not-found.tsx`
- [ ] **No loading page** — missing `loading.tsx` at root level

### Pricing Page (`goi-dich-vu/page.tsx`) — Score: 7/10
- Needs actual VND price (currently may show placeholder)
- Premium card should have stronger visual emphasis
- Add "Phổ biến nhất" badge on Premium
- Add comparison table for features
- SePay QR should be explained (Vietnamese users know QR but need trust signals)

### Chat Page (`tro-chuyen/[id]/page.tsx`) — Score: 8/10
- Good message flow, auto-scroll
- Typing indicator during AI response
- Guest limit warning
- Image display for generated images

**Issues:**
- [ ] **No character header** showing who you're talking to (name, avatar, personality snippet)
- [ ] **No back button** on mobile
- [ ] **No timestamp** on messages
- [ ] **Text-only** — no emoji picker, no quick replies

### Character Card — Score: 8/10
- Clean design, good aspect ratio
- Shows name + tagline
- Click → navigates to chat

**Issues:**
- [ ] **No chat count badge** (chatCount field exists but may not be displayed)
- [ ] **Avatar alt text** is missing/generic

### Overall UX Priorities
1. **Add error boundary + 404 page** (prevents blank screens)
2. **Chat header with character info** (critical for user context)
3. **Fix hardcoded hero CTA** (link to first available character)
4. **Add trust signals on pricing** (security badges, SePay logo)

---

## 4. MARKETING STRATEGY

### Best Channels for Vietnamese Gen Z
| Channel | MAU (Vietnam) | Our Priority |
|---------|---------------|-------------|
| TikTok | ~50M | #1 — viral potential, AI content trending |
| Facebook | ~70M | #2 — groups, ads, community |
| Zalo | ~75M | #3 — messaging, OA, payments |
| Instagram | ~15M | #4 — aesthetic, character art |
| YouTube | ~60M | #5 — longer reviews, tutorials |

### Launch Strategy: First 100 Users
1. **Week 1:** Founder + team personal invites (10-20 people)
2. **Week 1-2:** Post in Facebook groups (Tâm sự, Gen Z, Anime VN) — organic
3. **Week 2:** First TikTok video — "Chat thử với AI hiểu mình"
4. **Week 2-3:** Invite friends-of-friends, university Confessions pages
5. **Week 3-4:** Facebook micro-ads ($5-10/day), target anime fans 18-25

### Pricing Psychology for Vietnamese Market
- **79.000đ/month** = ~2.5 ly trà sữa = below "suy nghĩ" threshold
- Vietnamese users compare to: Netflix (108k), Spotify (59k), game top-up (50-100k)
- **Anchoring trick:** Show "Chỉ 2.600đ/ngày" instead of monthly price
- **Trial period:** Consider 3-day free Premium trial after signup
- **Annual plan:** 590.000đ/year (save 358k = "tiết kiệm 38%")

### Vietnamese Branding
- **Name:** "Ai Hiểu Bạn" — perfect wordplay, memorable, emotional
- **Logo:** Should incorporate both "AI" text and a friendly anime character
- **Colors:** Soft pastels (pink/purple gradient = matches anime aesthetic + comfort feeling)
- **Voice:** Warm, understanding, non-judgmental. Use "mình/bạn" (casual Vietnamese)
- **Domain:** aihieuban.vn (check availability) or aihieuban.com

---

## 5. COMPETITOR ANALYSIS (Vietnamese Market)

### Direct Competitors (AI Chat in Vietnam)
| Product | Type | Language | Pricing |
|---------|------|----------|---------|
| **Kiki AI** | General AI assistant | Vietnamese | Free |
| **Replika** | AI companion | English (some VN users) | Free + Pro ($20/mo) |
| **Character.AI** | Character chat | English | Free + Plus ($10/mo) |
| **Candy.AI** | AI companion (NSFW) | English | Credits-based |
| **Zalo AI** | Chatbot | Vietnamese | Free |

### Key Insight
**No Vietnamese-native AI companion app exists** that combines:
- Vietnamese language
- Anime characters
- Emotional support focus
- Local payment (SePay/VNPay)

This is a genuine market gap.

### Vietnamese Mental Health Apps
- **Hello Bacsi** — health info, not AI chat
- **Tâm An** — meditation/mindfulness
- **Betterhelp** — English, expensive for VN market

### Opportunity
Position Ai Hiểu Bạn as: **"Bạn tâm sự AI đầu tiên cho người Việt"** (First AI companion for Vietnamese)

---

## TOP 10 ACTIONABLE RECOMMENDATIONS

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | **Create OG image** (1200x630) with anime character + "Ai Hiểu Bạn" branding | HIGH (social sharing) | LOW |
| 2 | **Add 404 page + error boundary** in frontend | HIGH (prevents blank screens) | LOW |
| 3 | **Add character header in chat** (avatar, name, personality) | HIGH (UX context) | LOW |
| 4 | **Buy domain aihieuban.vn** and configure | HIGH (branding/SEO) | LOW |
| 5 | **Create TikTok account** + first 3 demo videos | HIGH (user acquisition) | MED |
| 6 | **Add page-level SEO** (unique titles for chat, pricing) | MED (SEO) | LOW |
| 7 | **Add trust signals on pricing page** (SePay logo, security badges, "2.600đ/ngày") | MED (conversion) | LOW |
| 8 | **Create Facebook page + Zalo OA** | MED (presence) | LOW |
| 9 | **Add structured data** (JSON-LD WebApplication) | MED (search appearance) | LOW |
| 10 | **Generate sitemap.xml** (next-sitemap package) | MED (indexing) | LOW |

---

## SOCIAL MEDIA LAUNCH CHECKLIST

### Pre-Launch
- [ ] TikTok account created (@aihieuban)
- [ ] Facebook Page created (Ai Hiểu Bạn)
- [ ] Zalo Official Account applied
- [ ] Instagram account created (@aihieuban)
- [ ] OG image designed and deployed
- [ ] 3 TikTok videos filmed (screen recordings of chat)
- [ ] 5 Facebook posts drafted
- [ ] Domain purchased (aihieuban.vn)

### Launch Week
- [ ] Post TikTok video #1: "Chat thử với AI hiểu mình"
- [ ] Share in 5 Facebook groups (Tâm sự, Gen Z, Anime VN)
- [ ] Post on personal social media (team members)
- [ ] University Confessions page submissions
- [ ] Monitor user feedback + iterate

### Post-Launch
- [ ] Daily TikTok content (1 video/day for first month)
- [ ] Facebook ads A/B test ($5/day budget)
- [ ] Collect user testimonials
- [ ] Iterate on character personalities based on chat data
- [ ] Community building in Facebook group

---

## UX BUGS FOUND

| # | Page | Bug/Issue | Severity |
|---|------|-----------|----------|
| 1 | Homepage | Hero CTA hardcoded to `/tro-chuyen/1` — breaks if char ID changes | Medium |
| 2 | Layout | No 404 page — navigating to invalid URL shows blank | Medium |
| 3 | Layout | No error boundary — React crash = blank screen | Medium |
| 4 | Chat | No back button on mobile view | Low |
| 5 | Chat | No character header (user doesn't know who they're talking to at glance) | Medium |
| 6 | Pricing | May not show actual VND price | High |
| 7 | All pages | No favicon (shows Next.js default) | Low |
| 8 | Character cards | Missing alt text on avatar images | Low (a11y) |

---

## UNRESOLVED QUESTIONS

1. **Domain:** Is aihieuban.vn available? Who purchases?
2. **OG Image:** Who designs the branded social sharing image?
3. **Real AI timeline:** When will AI team deliver LLM integration?
4. **SePay production:** Has production SePay merchant account been set up?
5. **Legal:** Do we need Terms of Service / Privacy Policy for launch?
6. **App Store:** Future plan to port to React Native — timeline?
