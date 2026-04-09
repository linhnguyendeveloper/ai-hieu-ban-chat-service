# AI Hieu Ban — Chat Service (Flask)

Internal microservice xu ly chat/AI response. Duoc goi boi Node.js backend, KHONG truc tiep tu frontend.

## Kien truc

```
Frontend → Node.js Backend → [Flask Chat Service] → (AI/LLM Model placeholder)
              ↓                       ↓
         Auth, DB, Limits        Generate response
         (gatekeeper)            (replaceable engine)
```

## Yeu cau

- Python >= 3.9
- pip

## Cai dat local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Service chay tai `http://localhost:5001`

## Environment Variables

| Bien | Mo ta | Mac dinh |
|------|-------|----------|
| `SERVICE_SECRET` | Shared secret voi Node.js backend | `dev-service-secret-change-me` |
| `PORT` | Port chay service | `5001` |

**QUAN TRONG:** `SERVICE_SECRET` phai giong voi `CHAT_SERVICE_SECRET` trong Node.js backend.

## API Endpoints

| Method | Path | Auth | Mo ta |
|--------|------|------|-------|
| GET | `/health` | - | Health check |
| POST | `/chat` | X-Service-Secret | Generate chat response |

### POST /chat

Request (tu Node.js backend):
```json
{
  "message": "Xin chao ban",
  "character_id": "1",
  "character_name": "Linh Chi",
  "character_personality": "Diu dang, biet lang nghe...",
  "user_tier": "FREE"
}
```

Response:
```json
{
  "content": "(From Python Babe) Minh hieu cam giac cua ban...",
  "image_url": null
}
```

### Bao mat

- Chi chap nhan request co header `X-Service-Secret` khop voi `SERVICE_SECRET`
- Tra ve 403 neu secret sai
- Frontend KHONG BAO GIO goi truc tiep service nay

## Deploy len Railway

1. Tao service moi tren Railway tu repo nay
2. Set env vars:
   - `SERVICE_SECRET` = (giong voi `CHAT_SERVICE_SECRET` cua backend)
   - `PORT` = Railway tu set
3. Railway tu detect Dockerfile va build
4. Copy Railway URL, set vao backend: `CHAT_SERVICE_URL=https://<railway-url>`

## Thay the AI Model

Khi team AI san sang, sua file `app.py` tai ham `chat()`:

```python
# Thay dong nay:
content, _last_response_index = get_random_response(_last_response_index)

# Bang:
content = llm.generate(
    message=message,
    character_name=data.get("character_name"),
    character_personality=data.get("character_personality"),
)
```

## Chay 3 services local

```bash
# Terminal 1 — Flask Chat Service
cd ai-hieu-ban-chat-service
source venv/bin/activate && python app.py

# Terminal 2 — Node.js Backend
cd ai-hieu-ban-backend
npm run dev:local

# Terminal 3 — Next.js Frontend
cd ai-hieu-ban-frontend
npm run dev
```

Mo `http://localhost:3000`, gui tin nhan. Thay `(From Python Babe)` = Flask dang hoat dong.
