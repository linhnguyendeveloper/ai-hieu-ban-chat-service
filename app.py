"""
AI Hiểu Bạn — Chat Service (Flask)
Internal service called by Node.js backend to generate chat responses.
Auth: service-to-service shared secret (not user-facing).
"""

import os
import random
import time
from functools import wraps

from flask import Flask, request, jsonify

app = Flask(__name__)

SERVICE_SECRET = os.environ.get("SERVICE_SECRET", "dev-service-secret-change-me")
PORT = int(os.environ.get("PORT", "5001"))

# ── Mock responses (same as Node.js but prefixed) ──────────────────────

MOCK_RESPONSES = [
    "(From Python Babe) Mình hiểu cảm giác của bạn. Bạn không đơn độc đâu nhé.",
    "(From Python Babe) Cảm ơn bạn đã chia sẻ với mình. Mình luôn ở đây lắng nghe bạn.",
    "(From Python Babe) Bạn đã rất mạnh mẽ rồi đó. Hãy tự hào về bản thân mình nhé!",
    "(From Python Babe) Đôi khi cuộc sống khó khăn, nhưng mình tin bạn sẽ vượt qua được.",
    "(From Python Babe) Mình rất vui được trò chuyện với bạn hôm nay.",
    "(From Python Babe) Bạn có muốn kể thêm cho mình nghe không? Mình đang lắng nghe đây.",
    "(From Python Babe) Mọi chuyện rồi sẽ ổn thôi. Hãy cho bản thân thời gian nhé.",
    "(From Python Babe) Bạn xứng đáng được yêu thương và hạnh phúc.",
    "(From Python Babe) Hãy nhớ rằng, mỗi ngày là một cơ hội mới để bắt đầu lại.",
    "(From Python Babe) Mình thấy bạn là người rất đặc biệt đấy!",
    "(From Python Babe) Cảm xúc của bạn hoàn toàn hợp lý. Đừng ngại thể hiện nhé.",
    "(From Python Babe) Bạn không cần phải hoàn hảo. Chỉ cần là chính mình thôi.",
    "(From Python Babe) Mình luôn ở đây khi bạn cần. Đừng ngại chia sẻ bất cứ điều gì.",
    "(From Python Babe) Hôm nay bạn đã làm tốt lắm rồi! Hãy thưởng cho mình một chút nghỉ ngơi.",
    "(From Python Babe) Hãy dành thời gian cho bản thân mình nhé. Bạn xứng đáng được chăm sóc.",
    "(From Python Babe) Mình tin vào bạn. Bạn có thể làm được mọi thứ mình muốn!",
    "(From Python Babe) Đừng so sánh mình với người khác. Bạn có giá trị riêng của mình.",
    "(From Python Babe) Cảm ơn bạn đã tin tưởng và chia sẻ những điều này với mình.",
    "(From Python Babe) Mỗi bước nhỏ cũng là tiến bộ. Hãy kiên nhẫn với bản thân nhé.",
    "(From Python Babe) Bạn không cô đơn. Mình sẽ luôn đồng hành cùng bạn trên con đường này.",
]

MOCK_IMAGE_RESPONSES = [
    "(From Python Babe) Đây là bức ảnh mình vẽ cho bạn nè! Hy vọng bạn thích.",
    "(From Python Babe) Mình đã tạo một bức ảnh đặc biệt dành riêng cho bạn.",
    "(From Python Babe) Xem bức ảnh này nhé! Mình vẽ bằng cả tấm lòng đấy.",
]

IMAGE_KEYWORDS = ["ảnh", "hình", "vẽ", "tạo ảnh", "tạo hình", "gửi ảnh", "xem ảnh", "draw", "image", "picture"]

MOCK_IMAGE_URLS = [
    "https://api.dicebear.com/9.x/adventurer/svg?seed=gen1&backgroundColor=ffd5dc&size=512",
    "https://api.dicebear.com/9.x/adventurer/svg?seed=gen2&backgroundColor=e8d5f5&size=512",
    "https://api.dicebear.com/9.x/adventurer/svg?seed=gen3&backgroundColor=d4f5d0&size=512",
]

_last_response_index = -1


# ── Service auth decorator ─────────────────────────────────────────────

def require_service_auth(f):
    """Verify X-Service-Secret header matches our shared secret."""
    @wraps(f)
    def decorated(*args, **kwargs):
        secret = request.headers.get("X-Service-Secret", "")
        if secret != SERVICE_SECRET:
            return jsonify({"error": "Unauthorized service call"}), 403
        return f(*args, **kwargs)
    return decorated


# ── Helpers ─────────────────────────────────────────────────────────────

def is_image_request(content: str) -> bool:
    lower = content.lower()
    return any(kw in lower for kw in IMAGE_KEYWORDS)


def get_random_response(exclude: int) -> tuple[str, int]:
    global _last_response_index
    idx = random.randint(0, len(MOCK_RESPONSES) - 1)
    while idx == exclude and len(MOCK_RESPONSES) > 1:
        idx = random.randint(0, len(MOCK_RESPONSES) - 1)
    return MOCK_RESPONSES[idx], idx


# ── Routes ──────────────────────────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "chat-service", "engine": "mock"})


@app.route("/chat", methods=["POST"])
@require_service_auth
def chat():
    """
    Generate a chat response.
    Called by Node.js backend (not directly by frontend).

    Request body:
    {
        "message": "user message text",
        "character_id": "1",
        "character_name": "Linh Chi",
        "character_personality": "Dịu dàng...",
        "user_tier": "FREE" | "PREMIUM"
    }

    Response:
    {
        "content": "response text",
        "image_url": null | "https://..."
    }
    """
    global _last_response_index

    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request body"}), 400

    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Empty message"}), 400

    user_tier = data.get("user_tier", "FREE")

    # Simulate thinking delay (1-3s)
    time.sleep(random.uniform(1.0, 3.0))

    # Check if user wants an image
    wants_image = is_image_request(message)

    if wants_image and user_tier == "PREMIUM":
        content = random.choice(MOCK_IMAGE_RESPONSES)
        image_url = random.choice(MOCK_IMAGE_URLS)
    elif wants_image and user_tier == "FREE":
        content = "(From Python Babe) Tính năng tạo ảnh chỉ dành cho thành viên Premium. Nâng cấp để trải nghiệm nhé!"
        image_url = None
    else:
        content, _last_response_index = get_random_response(_last_response_index)
        image_url = None

    # TODO: Replace with actual AI/LLM model call
    # character_name = data.get("character_name", "")
    # character_personality = data.get("character_personality", "")
    # response = llm.generate(message, character_name, character_personality)

    return jsonify({
        "content": content,
        "image_url": image_url,
    })


if __name__ == "__main__":
    print(f"🐍 Chat Service đang chạy tại http://localhost:{PORT}")
    print(f"🤖 Engine: mock (placeholder cho AI/LLM)")
    app.run(host="0.0.0.0", port=PORT, debug=True)
