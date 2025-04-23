import asyncio
from datetime import datetime
from collections import defaultdict
import aiohttp

from app.loader import bot
from app.config import ADMINS, SERVICES, TIMEOUT, RETRY_LIM, LOG_FILE
from loguru import logger 

logger.add(LOG_FILE, rotation="10 MB", retention="10 days", level="INFO")

error_count = defaultdict(int)

async def notify_admins(message: str):
    for admin_id in ADMINS:
        try:
            await bot.send_message(chat_id=admin_id, text=message)
        except Exception as e:
            logger.error(f'Ошибка при отправке сообщения ({admin_id}): {e}')

async def check_service(session, url):
    start_time = datetime.now()
    try:
        async with session.post(url) as response:
            response_time = (datetime.now() - start_time).total_seconds()
            status = response.status
            logger.info(f'{url} | {status} | {response_time:.2f}s')

            repetition_key = f'{url}_{status}'
            should_alert = False

            if not (200 <= status < 300):
                error_count[repetition_key] += 1

                if error_count[repetition_key] > RETRY_LIM:
                    should_alert = True
            else:
                error_count[repetition_key] = 0

            if response_time > TIMEOUT:
                should_alert = True

            if should_alert:
                msg = (
                    f'Сбой при проверке сервиса:\n'
                    f'URL: {url}\n'
                    f'Код ответа: {status}\n'
                    f'Время отклика: {response_time:.2f}s'
                )
                await notify_admins(msg)

    except Exception as e:
        logger.error(f'{url} | ERROR: {repr(e)}')

async def monitor_loop():
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [check_service(session, url) for url in SERVICES]
            await asyncio.gather(*tasks)
            await asyncio.sleep(300)

if __name__ == '__main__':
    try:
        asyncio.run(monitor_loop())
    except KeyboardInterrupt:
        logger.warning('Мониторинг остановлен вручную')
