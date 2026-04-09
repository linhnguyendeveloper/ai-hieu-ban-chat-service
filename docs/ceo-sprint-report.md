# CEO Sprint Report — Ai Hiểu Bạn
**Date:** 2026-04-09 | **Author:** Minh (CEO/Product Lead) | **Status:** Active Sprint

---

## 1. STRATEGIC DECISIONS

### #1 Priority: Ship a Working Chat Experience
The core value proposition is **"trò chuyện với nhân vật AI"**. Everything else (image gen, character creation, admin) is secondary. Users must be able to: open the app → see characters → pick one → chat → feel understood.

### Features CUT from MVP
| Feature | Decision | Reason |
|---------|----------|--------|
| Character creation by users | **CUT** | Use 10 curated characters. User-created chars need moderation |
| Admin panel | **CUT** | Use Prisma Studio or direct DB for now |
| Email notifications | **CUT** | No email service needed for MVP |
| Social sharing | **POST-MVP** | Nice-to-have, not critical for launch |
| Analytics dashboard | **CUT** | Use Vercel/Railway built-in analytics |
| Content moderation | **SIMPLIFIED** | Keyword filter only, no AI moderation |
| Conversation export | **CUT** | Not needed for MVP |
| Multiple languages | **CUT** | Vietnamese only, as planned |

### Features KEPT for MVP
| Feature | Priority | Status |
|---------|----------|--------|
| Character gallery + filtering | P0 | DONE |
| Google OAuth login | P0 | DONE |
| Guest mode (4 msgs) | P0 | DONE |
| Chat with text responses | P0 | DONE (mock, AI placeholder) |
| Image generation (Premium) | P1 | DONE (mock, AI placeholder) |
| SePay payment | P0 | DONE |
| Pricing page | P0 | DONE |
| User profile | P1 | DONE |
| Mobile responsive | P0 | DONE |
| SEO meta tags | P1 | DONE (just added) |

### Pricing Decision
| Tier | Price | Features |
|------|-------|----------|
| **Miễn Phí** (Free) | 0đ | 10 tin nhắn/ngày, chat text, 4 tin nhắn thử không cần đăng ký |
| **Premium** | **79.000đ/tháng** | Không giới hạn tin nhắn, tạo ảnh nhân vật, ưu tiên phản hồi |

**Reasoning:** 79k VND (~$3.20) hits the sweet spot for Vietnamese Gen Z:
- Lower than Netflix VN (108k), higher than typical mobile game (49k)
- Below "suy nghĩ lâu" threshold for Gen Z (dưới 100k = mua luôn)
- Room to add 149k/month tier later (Premium Plus) with more features

### Timeline
| Milestone | Target |
|-----------|--------|
| **Alpha** (internal testing) | NOW — already functional |
| **Beta** (invite 20-50 users) | When AI team integrates real LLM |
| **Public launch** | When real AI responses work + payment tested |

---

## 2. TODAY'S SPRINT PLAN

### CTO Tasks (DONE)
- [x] Verify all endpoints working (characters, chat, payment)
- [x] Harden SePay webhook (IP whitelist, signature verification, idempotency)
- [x] Fix Flask debug mode (both services)
- [x] Add SEO/OG meta tags to frontend

### Growth Lead Tasks (IN PROGRESS)
- [ ] Vietnamese SEO keyword research
- [ ] UX audit of all pages
- [ ] Content strategy for launch
- [ ] Marketing channel analysis
- [ ] Competitor analysis (Vietnamese market)

### NEXT Sprint (After AI Integration)
- [ ] Replace mock responses with real LLM
- [ ] Replace DiceBear with real image generation
- [ ] Test SePay payment flow end-to-end with real money
- [ ] Deploy image-service to Railway
- [ ] Load test with 50 concurrent users
- [ ] Create OG image for social sharing

---

## 3. MVP FEATURE CHECKLIST

| Feature | Status | MVP? |
|---------|--------|------|
| Character gallery browsing | DONE | Yes |
| Character gender filter | DONE | Yes |
| Google OAuth login | DONE | Yes |
| Guest mode (4 msgs, no signup) | DONE | Yes |
| Chat with characters (text) | DONE (mock) | Yes |
| Image generation in chat | DONE (mock) | Yes (Premium) |
| Character creation by users | UI DONE, API DONE | **CUT** from MVP |
| SePay QR payment | DONE | Yes |
| User profile page | DONE | Yes |
| Pricing page | DONE | Yes |
| SEO meta tags + OG | DONE | Yes |
| Mobile responsive | DONE | Yes |
| Admin panel | NOT STARTED | No |
| Content moderation | NOT STARTED | No |
| Analytics/tracking | NOT STARTED | No |
| Email notifications | NOT STARTED | No |
| Social sharing | NOT STARTED | No |
| Vietnamese localization | DONE (all UI) | Yes |

**MVP Score: 12/13 core features DONE** (pending: real AI integration from AI team)

---

## 4. RISKS & MITIGATION

| # | Risk | Severity | Mitigation |
|---|------|----------|------------|
| 1 | **AI team delays** — no real LLM means no real product | CRITICAL | Mock responses feel real enough for demo. Ship beta with mock, replace later. Communicate clearly what's mock |
| 2 | **SePay payment fails** in production | HIGH | Test with sandbox first. Have simulate-payment endpoint for demo. Add error handling + user feedback |
| 3 | **No users care** — product doesn't resonate | HIGH | Beta test with 20 users, gather feedback BEFORE public launch. Iterate on character personalities |
| 4 | **Vietnamese content quality** — AI responses feel foreign/robotic | MEDIUM | Write Vietnamese-native response templates. AI team must prioritize Vietnamese fluency |
| 5 | **Legal/compliance** — AI companion app regulations in Vietnam | LOW | No nsfw = lower risk. Monitor Bộ TT&TT regulations. Add terms of service |

---

## 5. COMPETITIVE POSITIONING

### Differentiation from nectar.ai
| Aspect | nectar.ai | Ai Hiểu Bạn |
|--------|-----------|-------------|
| Content | NSFW, romantic/sexual | SFW, emotional support |
| Language | English | Vietnamese only |
| Characters | Photorealistic + anime | Anime only |
| Payment | Credit system (confusing) | Simple SePay QR (familiar) |
| Target | Global adults | Vietnamese Gen Z (18-30) |
| Pricing | $9.99+/month | 79.000đ/tháng (~$3.20) |

### Vietnamese Market Advantages
- **No direct Vietnamese competitor** in AI character chat space
- **SePay QR** = native payment experience (Vietnamese banks)
- **Vietnamese cultural context** = family pressure, thi cử, cô đơn, relationship stress
- **"Ai"** wordplay = memorable, organic Vietnamese branding

### Suggested Taglines
- **Primary:** "Ai Hiểu Bạn — Người bạn AI luôn hiểu và đồng hành cùng bạn"
- **Short:** "Luôn có ai hiểu bạn"
- **Chat CTA:** "Bắt đầu tâm sự ngay"
- **Marketing hook:** "Khi không ai hiểu bạn... AI hiểu"
- **TikTok hook:** "Thử chat với AI hiểu bạn hơn bạn thân"

---

## 6. GROWTH ROADMAP

### First 100 Users
1. **Personal network** — Founder + team invite friends/family
2. **Facebook Groups** — Post in "Tâm sự tuổi 20", "Gen Z Việt Nam" groups
3. **TikTok** — Short videos of character chat interactions
4. **University forums** — Target stressed students (Confessions pages)

### First 1,000 Users
1. **TikTok viral content** — "AI này hiểu mình hơn bạn thân" format
2. **Facebook Ads** — Target 18-25, interests: anime, tâm sự, mental health
3. **KOL partnerships** — Micro-influencers in anime/mental health space
4. **Zalo OA** — Official Account for notifications + mini-app

### Channels Strategy
| Channel | Priority | Content Type |
|---------|----------|-------------|
| **TikTok** | #1 | Chat reaction videos, character reveals, emotional moments |
| **Facebook** | #2 | Longer stories, community building, ads |
| **Zalo** | #3 | Direct messaging, OA notifications |
| **Instagram** | #4 | Character art, aesthetic posts |

### Partnership Ideas
- Vietnamese mental health orgs (Tâm An, Hello Bacsi)
- University counseling centers
- Anime communities (Anime Việt Nam, otaku groups)
- Vietnamese YouTubers covering AI/tech

---

## DECISION LOG

| Decision | Rationale | Date |
|----------|-----------|------|
| Price at 79k VND/month | Below 100k impulse-buy threshold for Gen Z | 2026-04-09 |
| Cut character creation from MVP | Needs moderation; 10 curated chars is enough | 2026-04-09 |
| Cut admin panel | Use Prisma Studio; build when we have users | 2026-04-09 |
| Keep image gen in MVP | Key differentiator from basic chatbots | 2026-04-09 |
| Vietnamese only | Focus > spread thin. English later if needed | 2026-04-09 |
