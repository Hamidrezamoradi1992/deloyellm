import requests
from fastapi import APIRouter, HTTPException, WebSocket, Depends
from app.schema.jwt import JWTPayload
from app.utils.JWT import JWTHandler
import asyncio
import json
import json
from fastapi import WebSocket
from datetime import datetime
# ############################################333
from langchain_openai import ChatOpenAI

# ################################################

router = APIRouter()

from concurrent.futures import ProcessPoolExecutor
import asyncio


#
#
# async def process_chunk_in_worker(chunk):
#     # این تابع برای اجرا در فرآیند جداگانه طراحی شده است
#     return chunk.text()
#
#
# import asyncio
#
# @router.websocket('/12/')
# async def signaling(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         try:
#             # دریافت پیام از کلاینت
#             message = await websocket.receive_text()
#             data = json.loads(message)
#
#             if data.get("type") == "ping":  # پیام پینگ دریافت شده
#                 print(f"Ping received: {data['content']}")
#
#                 # پردازش پیام توسط مدل AI
#                 model_name = "gpt-4o-mini"
#                 messages = [{"role": "user", "content": data['content']}]
#
#                 llm = ChatOpenAI(
#                     model=model_name,
#                     base_url="https://api.avalai.ir/v1",
#                     api_key="aa-c0dvbvKWKbbF2G5KLldcykBYQOUzNmylJBM6TCDatljY3MFQ"
#                 )
#
#                 start = datetime.now()
#                 response = []
#
#                 # تعریف تابع هندل استریم
#                 async def handle_stream(chunk):
#                     response.append(chunk.text())
#
#                 # اجرای استریم به صورت تسک‌های جداگانه
#                 tasks = [
#                     handle_stream(chunk)
#                     async for chunk in llm.astream(messages)  # استریم چانک‌ها
#                 ]
#
#                 # انتظار برای اتمام تمام تسک‌ها
#                 await asyncio.gather(*tasks)
#
#                 end = datetime.now()
#                 print(f"AI processing time: {end - start}")
#
#                 pong_message = {"type": "pong", "response": "".join(response)}
#
#                 # ارسال پاسخ به کلاینت
#                 await websocket.send_text(json.dumps(pong_message))
#
#         except Exception as e:
#             print(f"Error: {e}")
#             await websocket.close()
#             break

# @router.websocket('/12/')
# async def signaling(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         try:
#             # دریافت پیام از کلاینت
#             message = await websocket.receive_text()
#             data = json.loads(message)
#
#             if data.get("type") == "ping":  # پیام پینگ دریافت شده
#                 print(f"Ping received: {data['content']}")
#
#                 # پردازش پیام توسط مدل AI
#                 model_name = "gpt-4o-mini"
#                 messages = [{"role": "user", "content": data['content']}]
#
#                 llm = ChatOpenAI(
#                     model=model_name,
#                     base_url="https://api.avalai.ir/v1",
#                     api_key="aa-c0dvbvKWKbbF2G5KLldcykBYQOUzNmylJBM6TCDatljY3MFQ"
#                 )
#
#                 start = datetime.now()
#                 response = []
#
#                 # تنظیم Multiprocessing برای پردازش هر chunk
#                 with ProcessPoolExecutor() as executor:
#                     loop = asyncio.get_event_loop()
#                     tasks = []
#
#                     # استریم پیام‌ها و ایجاد تسک برای هر چانک
#                     async for chunk in llm.astream(messages):  # فرض پشتیبانی از استریم
#                         tasks.append(loop.run_in_executor(executor, process_chunk_in_worker, chunk))
#
#                     # منتظر ماندن برای تکمیل تمام تسک‌ها
#                     results = await asyncio.gather(*tasks)
#                     response.extend(results)
#
#                 end = datetime.now()
#                 print(f"AI processing time: {end - start}")
#
#                 pong_message = {"type": "pong", "response": "".join(response)}
#
#                 # ارسال پاسخ به کلاینت
#                 await websocket.send_text(json.dumps(pong_message))
#
#         except Exception as e:
#             print(f"Error: {e}")
#             await websocket.close()
#             break


# $$$$$$$$$$$$$$$$$$$$$4444444444444444444$$$$$$$$$$$$$$$$$$44444444$$$$$$$$$$$$$$444$$$$$$444$$$$$44$$$$$$
#


@router.websocket("/12/")
async def signaling(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            message = await websocket.receive_text()
            data = json.loads(message)

            if data.get("type") == "ping":
                start = datetime.now()
                url = "http://87.236.166.163:8000/ask"
                headers = {"Content-Type": "application/json"}
                data = {"question": data['content']}
                response = requests.post(url, headers=headers, json=data)
                end = datetime.now()
                print(f"AI processing time: {end - start}")
                print(response.text)
                await websocket.send_text(response.json()['response'])

        except Exception as e:
            print(f"Error: {e}")
            await websocket.close()
            break

###########################31121212########################3

# from fastapi import WebSocket, APIRouter
# import httpx
# import json
# from datetime import datetime
#
# router = APIRouter()
#
# from fastapi import WebSocket, APIRouter
# import httpx
# import json
# from datetime import datetime
#
# router = APIRouter()


# @router.websocket("/12/")
# async def signaling(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         try:
#             # دریافت پیام از کلاینت
#             message = await websocket.receive_text()
#             data = json.loads(message)
#
#             if data.get("type") == "ping":  # پیام پینگ دریافت شده
#                 start = datetime.now()
#                 url = "http://87.236.166.163:8000/ask"
#                 headers = {"Content-Type": "application/json"}
#                 payload = {"question": data['content']}
#
#                 # استفاده از httpx برای درخواست غیرهمزمان
#                 async with httpx.AsyncClient() as client:
#                     response = await client.post(url, headers=headers, json=payload)
#
#                 end = datetime.now()
#                 print(f"AI processing time: {end - start}")
#
#                 # ارسال پاسخ از سرور به کلاینت
#                 await websocket.send_text(response.json().get('response', 'No response'))
#
#         except Exception as e:
#             print(f"Error: {e}")
#             await websocket.close()
#             break


from app.servise.api_llm import ApiLLm


# @router.post()
# async def llm1_1(massage: str):
#     res = ApiLLm(massage=massage)
#     response = await res.send()
#     return response


from fastapi import WebSocket

# import json
# from datetime import datetime

# @router.websocket('/12/')
# async def websocket_test_text(websockets: WebSocket):
#     await websockets.accept()
#     while True:
#
#             # دریافت پیام signaling از کلاینت
#             data = await websockets.receive_text()
#             signaling_message = json.loads(data)
#             print(f"Signaling message received: {signaling_message}")
#
#             # پردازش پیام‌های signaling
#             if signaling_message["type"] == "offer":
#                 # ارسال پاسخ (answer) به کلاینت
#                 response = {
#                     "type": "answer",
#                     "sdp": "answer_sdp_example_here"  # ایجاد SDP واقعی با WebRTC API
#                 }
#                 await websockets.send_text(json.dumps(response))
#             elif signaling_message["type"] == "candidate":
#                 # پردازش ICE Candidate
#                 print(f"Received ICE Candidate: {signaling_message['candidate']}")
#                 # این پیام را به دیگر کلاینت‌ها ارسال کنید یا ذخیره کنید

# except Exception as e:
#     print(f"Error: {e}")
#     await websockets.close()
#     break

# @router.websocket('/12/')
# async def websocket_test_text(websockets: WebSocket):
#     await websockets.accept()
#     while True:
#         data = await websockets.receive_text()
#         # send massage ai
#         model_name = "gpt-4o-mini"
#         messages = [
#             {"role": "user", "content": f"{data}"},
#         ]
#         llm = ChatOpenAI(
#             model=model_name, base_url="https://api.avalai.ir/v1",
#             api_key="aa-c0dvbvKWKbbF2G5KLldcykBYQOUzNmylJBM6TCDatljY3MFQ"
#         )
#         start = datetime.now()
#         async for chunk in llm.astream(messages):  # Assuming `astream` is an async generator
#             await websockets.send_text(chunk.text())
#         end = datetime.now()
#         print(f"time: {end - start}")
