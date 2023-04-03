from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import aiomysql
from controlsystem.private import seceret

class ControlSystemConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # MySQL 데이터베이스 연결 설정
        db = await aiomysql.connect(host=seceret.DBDATA['host'],
                                    port=3306,
                                    user=seceret.DBDATA['user'],
                                    password=seceret.DBDATA['password'],
                                    db=seceret.DBDATA['db'],
                                    charset='utf8mb4',
                                    autocommit=True)
        cursor = await db.cursor()

        # MySQL 데이터베이스 변경 사항 구독
        while True:
            await cursor.execute("SELECT * FROM moduleprocessing_dangermessages;")
            rows = await cursor.fetchall()
            for row in rows:
                # 변경된 데이터를 WebSocket을 통해 클라이언트에 전달
                await self.send(text_data=str(row))
            await asyncio.sleep(1)
