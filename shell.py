# from transformers import pipeline
#
# # بارگذاری مدل تحلیل احساسات (برای مثال)
# sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
# result = sentiment_analyzer("I love using Hugging Face locally!")
# print(result)


# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
#
# html = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <title>Chat</title>
#     </head>
#     <body>
#         <h1>WebSocket Chat</h1>
#         <h2>Your ID: <span id="ws-id"></span></h2>
#         <form action="" onsubmit="sendMessage(event)">
#             <input type="text" id="messageText" autocomplete="off"/>
#             <button>Send</button>
#         </form>
#         <ul id='messages'>
#         </ul>
#         <script>
#             var client_id = Date.now()
#             document.querySelector("#ws-id").textContent = client_id;
#             var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
#             ws.onmessage = function(event) {
#                 var messages = document.getElementById('messages')
#                 var message = document.createElement('li')
#                 var content = document.createTextNode(event.data)
#                 message.appendChild(content)
#                 messages.appendChild(message)
#             };
#             function sendMessage(event) {
#                 var input = document.getElementById("messageText")
#                 ws.send(input.value)
#                 input.value = ''
#                 event.preventDefault()
#             }
#         </script>
#     </body>
# </html>
# """
#
#
# class ConnectionManager:
#     def __init__(self):
#         self.active_connections: list[WebSocket] = []
#
#     async def connect(self, websocket: WebSocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)
#
#     def disconnect(self, websocket: WebSocket):
#         self.active_connections.remove(websocket)
#
#     async def send_personal_message(self, message: str, websocket: WebSocket):
#         await websocket.send_text(message)
#
#     async def broadcast(self, message: str):
#         for connection in self.active_connections:
#             await connection.send_text(message)
#
#
# manager = ConnectionManager()
#
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
#
# @app.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: int):
#     await manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await manager.send_personal_message(f"You wrote: {data}", websocket)
#             await manager.broadcast(f"Client #{client_id} says: {data}")
#     except WebSocketDisconnect:
#         manager.disconnect(websocket)
#         await manager.broadcast(f"Client #{client_id} left the chat")
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
import openai
import requests

# url = "https://api.avalai.ir/v1/models"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer aa-**"
# }
# response = requests.get(url, headers=headers)
# print(response.json())

# =================================api open ai chat===========================
# from langchain_openai import ChatOpenAI
# from datetime import datetime
#
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content":"چگونه میشه با ادم های بیشعور برخورد کرد"},
# ]
# # استفاده از مدل gpt-4o-mini
# model_name = "gpt-4o-mini"
#
#
# llm = ChatOpenAI(
#     model=model_name, base_url="https://api.avalai.ir/v1", api_key="aa-c0dvbvKWKbbF2G5KLldcykBYQOUzNmylJBM6TCDatljY3MFQ"
# )
# start = datetime.now()
# llm.invoke(messages).pretty_print()
#
# end = datetime.now()
# print(f"time: {end - start}")
# openai._AzureModuleClient

# ================================= api open ai chat ===========================
# +++++++++++++++++++++++++++++++++++++ test ++++++++++++++++++++++++++++++

# استفاده از مدل‌ Claude 3.5 Sonnet
# model_name="anthropic.claude-3-5-sonnet-20240620-v1:0"

# llm = ChatOpenAI(
#     model=model_name, base_url="https://api.avalai.ir/v1", api_key="aa-c0dvbvKWKbbF2G5KLldcykBYQOUzNmylJBM6TCDatljY3MFQ"
# )
#
# massage2=llm.invoke(messages).text()
# print(massage2)


#
# from langchain_openai import ChatOpenAI # pip install -U langchain_openai
# import base64
# import os
#
# base_url = "https://api.avalai.ir/v1"
# api_key = "aa-90fxrFCDT7IOXM1HAh0ufu1lVpiMVVc5suQnLqmhYbBNfSkO"
#
# model_name = "gpt-4o-mini"
#
# # استفاده از مدل gemini-2.0-flash-exp
# # model_name = "gemini-2.0-flash-exp"
#
#
# # استفاده از مدل anthropic.claude-3-5-sonnet-20240620-v1:0
# # model_name = "anthropic.claude-3-5-sonnet-20240620-v1:0"
#
# llm = ChatOpenAI(
#     base_url=base_url,
#     model=model_name,
#     api_key=api_key,
# )
#
# IMAGE_PATH = "/home/hamid/Programmer/LLM1/static/media/1dd0341816ee431a.jpg"
#
# # Open the image file and encode it as a base64 string
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")
#
# base64_image = encode_image(IMAGE_PATH)
# image_ext = os.path.splitext(IMAGE_PATH)[1][1:]
#
# messages = [
#     {
#         "role": "system",
#         "content": "You are a helpful assistant.",
#     },
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": "این تصویر رو برام تفسیر کن.",
#             },
#             {
#                 "type": "image_url",
#                 "image_url": {
#                     "url": f"data:https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_b5o-PI7pYd7nkn9OS9QCRsJpzKSbBOHfsA&s;base64,{base64_image}",
#                     "detail": "auto",
#                 },
#             },
#         ],
#     },
# ]
#
# ai_message = llm.invoke(messages)
# print(ai_message.content)
# +++++++++++++++++++++++++++++++++++++ test ++++++++++++++++++++++++++++++

# server.py
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# import asyncio
# import wave
#
# app = FastAPI()
#
# # مسیر ذخیره‌سازی فایل‌های صوتی
# AUDIO_DIR = "audio_files"
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">🎤 شروع ضبط</button>
#     <button id="stopBtn" disabled>⏹️ توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 // درخواست اجازه استفاده از میکروفون
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 mediaRecorder = new MediaRecorder(stream);
#                 websocket = new WebSocket("ws://localhost:8000/ws/audio");
#
#                 websocket.onopen = () => {
#                     document.getElementById("status").innerText = "🟢 در حال ضبط...";
#                     // mediaRecorder.start(250); // ارسال هر 250 میلی‌ثانیه یک بخش از صدا
#                     mediaRecorder.start(100); // ارسال هر 100 میلی‌ثانیه
#
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     document.getElementById("status").innerText = "✅ ضبط متوقف شد!";
#                     websocket.close();
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (error) {
#                 console.error("خطا در ضبط صدا:", error);
#                 alert("اجازه دسترسی به میکروفون را بررسی کنید.");
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
#
# """
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
# import os
# @app.websocket("/ws/audio")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("✅ ارتباط وب‌سوکت برقرار شد...")
#     AUDIO_DIR = "static"
#     os.makedirs(AUDIO_DIR, exist_ok=True)
#     # نام فایل خروجی برای ذخیره صدا
#     filename = f"static/audio_record4.wav"
#
#     # Open a WAV file for writing
#     wf = wave.open(filename, "wb")
#     wf.setnchannels(3)  # Mono channel
#     wf.setsampwidth(2)  # 16-bit PCM
#     wf.setframerate(16000)  # 16kHz sample rate
#
#     try:
#         while True:
#             data = await websocket.receive_bytes()
#             if len(data) > 0:
#                 wf.writeframesraw(data)  # Write raw PCM data correctly
#                 print(f"📡 Received {len(data)} bytes of audio...")
#
#     except WebSocketDisconnect:
#         print("❌ WebSocket disconnected.")
#     finally:
#         wf.close()

#############################################################################################################3
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# import asyncio
# import wave
# import os
#
# app = FastAPI()
#
# # مسیر ذخیره‌سازی فایل‌های صوتی
# AUDIO_DIR = "audio_files"
#
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">🎤 شروع ضبط</button>
#     <button id="stopBtn" disabled>⏹️ توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 // درخواست اجازه استفاده از میکروفون
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 const options = { mimeType: 'audio/webm;codecs=opus' };
#                 mediaRecorder = new MediaRecorder(stream, options);
#                 websocket = new WebSocket("ws://localhost:8000/ws/audio");
#
#                 websocket.onopen = () => {
#                     document.getElementById("status").innerText = "🟢 در حال ضبط...";
#                     mediaRecorder.start(1); // ارسال هر 100 میلی‌ثانیه یک بخش از صدا
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     document.getElementById("status").innerText = "✅ ضبط متوقف شد!";
#                     websocket.close();
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (error) {
#                 console.error("خطا در ضبط صدا:", error);
#                 alert("اجازه دسترسی به میکروفون را بررسی کنید.");
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
# """
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
# # from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# # from fastapi.responses import HTMLResponse
# # import wave
# # import os
# # from pydub import AudioSegment
# from io import BytesIO
#
#
#
# @app.websocket("/ws/audio")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("✅ ارتباط وب‌سوکت برقرار شد...")
#
#     AUDIO_DIR = "static"
#     os.makedirs(AUDIO_DIR, exist_ok=True)
#
#     # نام فایل خروجی برای ذخیره صدا
#     filename = f"static/audio_record4.wav"
#
#     # Open a WAV file for writing
#     wf = wave.open(filename, "wb")
#     wf.setnchannels(1)  # Mono channel
#     wf.setsampwidth(2)  # 16-bit PCM
#     wf.setframerate(16000)  # 16kHz sample rate
#
#     try:
#         audio_data = BytesIO()
#         while True:
#             data = await websocket.receive_bytes()
#             audio_data.write(data)
#
#         audio_data.seek(0)
#         audio_segment = AudioSegment.from_file(audio_data, format="webm")
#         pcm_audio = audio_segment.set_frame_rate(16000).set_channels(1).set_sample_width(2)
#         pcm_audio.export(filename, format="wav")
#
#     except WebSocketDisconnect:
#         print("❌ WebSocket disconnected.")
#     finally:
#         wf.close()
############################################################3
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# from pydub import AudioSegment
# from io import BytesIO
# import wave
# import os
#
# app = FastAPI()
#
# # مسیر ذخیره‌سازی فایل‌های صوتی
# AUDIO_DIR = "audio_files"
#
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">🎤 شروع ضبط</button>
#     <button id="stopBtn" disabled>⏹️ توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 // درخواست اجازه استفاده از میکروفون
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 const options = { mimeType: 'audio/webm;codecs=opus' };
#                 mediaRecorder = new MediaRecorder(stream, options);
#                 websocket = new WebSocket("ws://localhost:8000/ws/audio");
#
#                 websocket.onopen = () => {
#                     document.getElementById("status").innerText = "🟢 در حال ضبط...";
#                     mediaRecorder.start(100); // ارسال هر 100 میلی‌ثانیه یک بخش از صدا
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     document.getElementById("status").innerText = "✅ ضبط متوقف شد!";
#                     websocket.close();
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (error) {
#                 console.error("خطا در ضبط صدا:", error);
#                 alert("اجازه دسترسی به میکروفون را بررسی کنید.");
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
# """
#
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
#
# @app.websocket("/ws/audio")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("✅ ارتباط وب‌سوکت برقرار شد...")
#
#     AUDIO_DIR = "static"
#     os.makedirs(AUDIO_DIR, exist_ok=True)
#
#     filename = f"static/audio_record4.wav"
#
#     try:
#         audio_data = BytesIO()
#         while True:
#             data = await websocket.receive_bytes()
#             audio_data.write(data)
#
#     except WebSocketDisconnect:
#         print("❌ WebSocket disconnected.")
#
#         audio_data.seek(0)
#         audio_segment = AudioSegment.from_file(audio_data, format="webm")
#         pcm_audio = audio_segment.set_frame_rate(16000).set_channels(1).set_sample_width(2)
#         pcm_audio.export(filename, format="wav")
#
#         print(f"✅ فایل صوتی ذخیره شد: {filename}")
#########################################################################
#
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# import wave
# import os
# from moviepy.audio.io import AudioFileClip
#
# app = FastAPI()
#
# # مسیر ذخیره‌سازی فایل‌های صوتی
# AUDIO_DIR = "audio_files"
#
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">🎤 شروع ضبط</button>
#     <button id="stopBtn" disabled>⏹️ توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 // درخواست اجازه استفاده از میکروفون
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 const options = { mimeType: 'audio/webm;codecs=opus' };
#                 mediaRecorder = new MediaRecorder(stream, options);
#                 websocket = new WebSocket("ws://localhost:8000/ws/audio");
#
#                 websocket.onopen = () => {
#                     document.getElementById("status").innerText = "🟢 در حال ضبط...";
#                     mediaRecorder.start(100); // ارسال هر 100 میلی‌ثانیه یک بخش از صدا
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     document.getElementById("status").innerText = "✅ ضبط متوقف شد!";
#                     websocket.close();
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (error) {
#                 console.error("خطا در ضبط صدا:", error);
#                 alert("اجازه دسترسی به میکروفون را بررسی کنید.");
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
# """
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
# @app.websocket("/ws/audio")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("✅ ارتباط وب‌سوکت برقرار شد...")
#
#     AUDIO_DIR = "static"
#     os.makedirs(AUDIO_DIR, exist_ok=True)
#
#     wav_filename = f"{AUDIO_DIR}/audio_record.wav"
#     mp4_filename = f"{AUDIO_DIR}/audio_record.mp4"
#
#     try:
#         # فایل WAV را باز کنید
#         with wave.open(wav_filename, 'wb') as wf:
#             wf.setnchannels(1)  # Mono
#             wf.setsampwidth(2)  # 16-bit PCM
#             wf.setframerate(16000)  # 16kHz sample rate
#
#             while True:
#                 try:
#                     data = await websocket.receive_bytes()
#                     wf.writeframes(data)
#                 except WebSocketDisconnect:
#                     print("❌ WebSocket disconnected.")
#                     break
#
#         # تبدیل WAV به MP4
#         audio_clip = AudioFileClip(wav_filename)
#         audio_clip.write_audiofile(mp4_filename, codec="libmp3lame")
#         audio_clip.close()
#
#         print(f"✅ فایل صوتی MP4 ذخیره شد: {mp4_filename}")
#
#     except Exception as e:
#         print(f"خطا: {e}")
############################################################################
# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# import wave
# import os
# import tempfile
# from moviepy.audio.io import AudioFileClip
#
# app = FastAPI()
#
# # مسیر ذخیره‌سازی فایل‌های صوتی
# AUDIO_DIR = "audio_files"
#
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">🎤 شروع ضبط</button>
#     <button id="stopBtn" disabled>⏹️ توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 // درخواست اجازه استفاده از میکروفون
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 const options = { mimeType: 'audio/webm;codecs=opus' };
#                 mediaRecorder = new MediaRecorder(stream, options);
#                 websocket = new WebSocket("ws://localhost:8000/ws/audio");
#
#                 websocket.onopen = () => {
#                     document.getElementById("status").innerText = "🟢 در حال ضبط...";
#                     mediaRecorder.start(100); // ارسال هر 100 میلی‌ثانیه یک بخش از صدا
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     document.getElementById("status").innerText = "✅ ضبط متوقف شد!";
#                     websocket.close();
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (error) {
#                 console.error("خطا در ضبط صدا:", error);
#                 alert("اجازه دسترسی به میکروفون را بررسی کنید.");
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
# """
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
# @app.websocket("/ws/audio")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     print("✅ ارتباط وب‌سوکت برقرار شد...")
#
#     AUDIO_DIR = "static"
#     os.makedirs(AUDIO_DIR, exist_ok=True)
#
#     wav_filename = f"{AUDIO_DIR}/audio_record.wav"
#     mp4_filename = f"{AUDIO_DIR}/audio_record.mp4"
#
#     try:
#         # فایل موقت برای ذخیره داده‌های دریافتی
#         temp_fd, temp_path = tempfile.mkstemp()
#         temp_file = os.fdopen(temp_fd, 'wb')
#
#         try:
#             while True:
#                 try:
#                     data = await websocket.receive_bytes()
#                     temp_file.write(data)
#                 except WebSocketDisconnect:
#                     print("❌ WebSocket disconnected.")
#                     break
#         finally:
#             temp_file.close()
#
#         # فایل WAV را باز کنید
#         with wave.open(wav_filename, 'wb') as wf:
#             wf.setnchannels(1)  # Mono
#             wf.setsampwidth(2)  # 16-bit PCM
#             wf.setframerate(16000)  # 16kHz sample rate
#
#             # خواندن داده‌ها از فایل موقت و نوشتن در فایل نهایی
#             with open(temp_path, 'rb') as temp_file:
#                 while True:
#                     data = temp_file.read(1024)
#                     if not data:
#                         break
#                     wf.writeframes(data)
#
#         # حذف فایل موقت
#         os.remove(temp_path)
#
#         # تبدیل WAV به MP4
#         audio_clip = AudioFileClip(wav_filename)
#         audio_clip.write_audiofile(mp4_filename, codec="libmp3lame")
#         audio_clip.close()
#
#         print(f"✅ فایل صوتی MP4 ذخیره شد: {mp4_filename}")
#
#     except Exception as e:
#         print(f"خطا: {e}")
####################################################################3
# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
# import uvicorn
# import os
# import time
#
# app = FastAPI()
#
# audio_dir = "audio"
# os.makedirs(audio_dir, exist_ok=True)
#
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">🎤 شروع ضبط</button>
#     <button id="stopBtn" disabled>⏹️ توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 // درخواست اجازه استفاده از میکروفون
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 const options = { mimeType: 'audio/webm;codecs=opus' };
#                 mediaRecorder = new MediaRecorder(stream, options);
#
#                 if (!websocket || websocket.readyState !== WebSocket.OPEN) {
#                     websocket = new WebSocket("ws://localhost:8000/ws");
#                 }
#
#                 websocket.onopen = () => {
#                     document.getElementById("status").innerText = "🟢 در حال ضبط...";
#                     mediaRecorder.start(100); // ارسال هر 100 میلی‌ثانیه یک بخش از صدا
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     document.getElementById("status").innerText = "✅ ضبط متوقف شد!";
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.stop()
#
#
#                     }
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (error) {
#                 console.error("خطا در ضبط صدا:", error);
#                 alert("اجازه دسترسی به میکروفون را بررسی کنید.");
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
#
# """
#
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     timestamp = int(time.time())
#     file_path = os.path.join(audio_dir, f"{timestamp}.webm")
#     data2 = "start"
#     if data2 == "start":
#         with (open(file_path, "wb") as f):
#             while True:
#                 try:
#                     # sockets=websocket.receive()
#                     # print(s)
#                     data = await websocket.receive_bytes()
#                     f.write(data)
#                     # if websocket.receive():
#                     #     print(data2)
#                     #     f.close()
#                     #     break
#                 except websocket_endpoint as e:
#                     f.close()
#                     break
#     print(f"Saved audio to {file_path}")
# 3333333333333333333333333333333333333

# # app.py
# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse
# import uvicorn
# import os
# import time
#
# app = FastAPI()
#
# audio_dir = "audio"
# os.makedirs(audio_dir, exist_ok=True)
#
# html = """
# <!DOCTYPE html>
# <html lang="fa">
# <head>
#     <meta charset="UTF-8">
#     <title>وب‌سوکت ضبط صدا</title>
# </head>
# <body>
#     <h2>🎙️ ضبط و ارسال صدا به سرور</h2>
#     <button id="startBtn">شروع ضبط</button>
#     <button id="stopBtn" disabled>توقف ضبط</button>
#     <p id="status">⏳ آماده ضبط...</p>
#
#     <script>
#         let mediaRecorder;
#         let websocket;
#
#         document.getElementById("startBtn").onclick = async () => {
#             try {
#                 const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
#                 const options = { mimeType: 'audio/webm;codecs=opus' };
#                 mediaRecorder = new MediaRecorder(stream, options);
#
#                 websocket = new WebSocket("ws://localhost:8000/ws");
#
#                 websocket.onopen = () => {
#                     websocket.send("start"); // پایان ارسال
#                     document.getElementById("status").innerText = "🔴 در حال ضبط...";
#                     mediaRecorder.start(200);
#                 };
#
#                 mediaRecorder.ondataavailable = (event) => {
#                     if (websocket.readyState === WebSocket.OPEN) {
#                         websocket.send(event.data);
#                     }
#                 };
#
#                 mediaRecorder.onstop = () => {
#                     websocket.send("end"); // پایان ارسال
#                 };
#
#                 websocket.onmessage = (event) => {
#                     document.getElementById("status").innerText = "✅ نتیجه سرور: " + event.data;
#                 };
#
#                 document.getElementById("startBtn").disabled = true;
#                 document.getElementById("stopBtn").disabled = false;
#             } catch (err) {
#                 alert("اجازه دسترسی به میکروفون را بدهید!");
#                 console.error(err);
#             }
#         };
#
#         document.getElementById("stopBtn").onclick = () => {
#             mediaRecorder.stop();
#             document.getElementById("startBtn").disabled = false;
#             document.getElementById("stopBtn").disabled = true;
#         };
#     </script>
# </body>
# </html>
# """
#
# @app.get("/")
# async def get():
#     return HTMLResponse(html)
#
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#
#     await websocket.accept()
#     hamid = websocket.client
#     print(hamid)
#     timestamp = int(time.time())
#     file_path = os.path.join(audio_dir, f"{timestamp}.webm")
#     message = await websocket.receive()
#     if "text" in message and message["text"] == "start":
#         with open(file_path, "wb") as file:
#             while True:
#                 try:
#                     message = await websocket.receive()
#                     if "bytes" in message:
#                         file.write(message["bytes"])
#                     elif "text" in message and message["text"] == "end":
#                         file.close()
#                         break
#                 except Exception as e:
#                     print("❌ خطا:", e)
#                     break
#
#         print(f"✅ فایل ذخیره شد: {file_path}")
#         result = f"فایل صوتی ذخیره شد: {file_path}"
#         await websocket.send_text(result)
###############################ّّّّّّّّّّّّّببببببببببببببببببببببببب#############################
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import os
import time

app = FastAPI()
audio_dir = "audio"
os.makedirs(audio_dir, exist_ok=True)

html = """
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <title>وب‌سوکت ضبط صدا</title>
</head>
<body>
    <h2>🎙️ ضبط و ارسال صدا به سرور</h2>
    <button id="startBtn">شروع ضبط</button>
    <button id="stopBtn" disabled>توقف ضبط</button>
    <p id="status">⏳ آماده ضبط...</p>

    <script>
        let websocket = new WebSocket("ws://localhost:8000/ws");
        let mediaRecorder;

        websocket.onopen = () => {
            document.getElementById("status").innerText = "🟢 اتصال برقرار شد!";
        };

        websocket.onmessage = (event) => {
            document.getElementById("status").innerText = "✅ نتیجه سرور: " + event.data;
        };

        document.getElementById("startBtn").onclick = async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                const options = { mimeType: 'audio/webm;codecs=opus' };
                mediaRecorder = new MediaRecorder(stream, options);

                websocket.send("start"); // شروع ارسال داده
                mediaRecorder.start(200);

                mediaRecorder.ondataavailable = (event) => {
                    if (websocket.readyState === WebSocket.OPEN) {
                        websocket.send(event.data);
                    }
                };

                mediaRecorder.onstop = () => {
                    websocket.send("end"); // پایان ارسال فایل فعلی
                };

                document.getElementById("startBtn").disabled = true;
                document.getElementById("stopBtn").disabled = false;
            } catch (err) {
                alert("اجازه دسترسی به میکروفون را بدهید!");
                console.error(err);
            }
        };

        document.getElementById("stopBtn").onclick = () => {
            mediaRecorder.stop();
            document.getElementById("startBtn").disabled = false;
            document.getElementById("stopBtn").disabled = true;
        };
    </script>
</body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    file_path = None
    file = None

    while True:
        try:
            message = await websocket.receive()

            if "text" in message:
                if message["text"] == "start":
                    timestamp = int(time.time())
                    file_path = os.path.join(audio_dir, f"{timestamp}.webm")
                    file = open(file_path, "wb")
                elif message["text"] == "end" and file:
                    file.close()
                    await websocket.send_text(f"✅ فایل ذخیره شد: {file_path}")
                    file = None
            elif "bytes" in message and file:
                file.write(message["bytes"])
        except Exception as e:
            print(f"❌ خطا: {e}")
            break
