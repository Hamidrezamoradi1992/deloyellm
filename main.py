from fastapi import FastAPI
from fastapi.responses import HTMLResponse,Response
from app.db.engin import MongoDBHandler
from app.db.models.user import User
from app.router.user import router as user_router
from app.router.registerJwt import router as jwtRouter
from app.router.otp import router as OtpRouter
from config.settings import setting
from fastapi.staticfiles import StaticFiles
from app.router.wb import router as websocketRouter
import templates
# Dependency to get Redis client

document_models = [User]
app = FastAPI()

mongo_handler = MongoDBHandler(uri=setting.DB_CONNECTION_STRING, db_name=setting.DB_NAME, document_models=document_models)


@app.on_event("startup")
async def on_startup():
    await mongo_handler.connect()


@app.on_event("shutdown")
async def on_shutdown():
    await mongo_handler.close()


app.include_router(user_router, prefix="/user")
app.include_router(jwtRouter, prefix="/token")
app.include_router(OtpRouter, prefix="/otp")
app.include_router(websocketRouter, prefix="/web")
html ="""
<!DOCTYPE html>
<html>
<head>
    <title>WebRTC Ping-Pong</title>
</head>
<body>
    <h1>Ping-Pong with AI</h1>
    <form id="form">
        <input type="text" id="messageInput" autocomplete="off" placeholder="Type your message..." />
        <button>Send Ping</button>
    </form>
    <ul id="messages"></ul>

    <script>
        const form = document.getElementById('form');
        const input = document.getElementById('messageInput');
        const messages = document.getElementById('messages');

        // اتصال به WebSocket برای signaling
        const ws = new WebSocket('ws://127.0.0.1:8000/web/12/');

        ws.onmessage = function(event) {
            const data = JSON.parse(event.data);
            if (data.type === "pong") {
                // نمایش پاسخ AI
                const li = document.createElement('li');
                li.textContent = `AI: ${data.response}`;
                messages.appendChild(li);
            }
        };

        form.addEventListener('submit', function(event) {
            event.preventDefault();

            // ارسال پیام پینگ به سرور
            const message = input.value;
            ws.send(JSON.stringify({ type: "ping", content: message }));

            // نمایش پیام ارسال شده
            const li = document.createElement('li');
            li.textContent = `You: ${message}`;
            messages.appendChild(li);
            input.value = '';
        });
    </script>
</body>
</html>

"""
# html = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>WebSocket Test</title>
# </head>
# <body>
#     <h1>WebSocket Test</h1>
#     <form id="form">
#         <input type="text" id="messageInput" autocomplete="off"/>
#         <button>Send</button>
#     </form>
#     <ul id="messages"></ul>
#     <script>
#         const form = document.getElementById('form');
#         const input = document.getElementById('messageInput');
#         const messages = document.getElementById('messages');
#
#         const ws = new WebSocket('ws://127.0.0.1:8000/web/12/');
#
#         ws.onmessage = function(event) {
#             const li = document.createElement('li');
#             li.textContent = event.data;
#             messages.appendChild(li);
#         };
#
#         form.addEventListener('submit', function(event) {
#             event.preventDefault();
#             ws.send(input.value);
#             input.value = '';
#         });
#     </script>
# </body>
# </html>
# """
@app.get("/")
async def get():
    return HTMLResponse(html)

app.mount("/static", StaticFiles(directory="static",html=False), name="static")