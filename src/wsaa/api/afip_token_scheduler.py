import os
from datetime import datetime, timezone

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.shared.utils.logger import logger
from src.wsaa.controllers.request_access_token_controller import \
    generate_afip_access_token
from src.wsaa.time.time_management import \
    generate_ntp_timestamp as time_provider
from src.wsaa.xml_management.xml_builder import is_expired, xml_exists

scheduler = AsyncIOScheduler()
FLAG_PATH = "src/wsaa/cache/initialized.flag"

async def run_job():

    pid = os.getpid()
    logger.info(f" [{pid}] Starting job: verifying token expiration")

    # Delete flag if token is expired to generate a new one
    if xml_exists("loginTicketResponse.xml"):
        if is_expired("loginTicketResponse.xml", time_provider):
            os.remove("src/wsaa/cache/initialized.flag")

    try:
        with open(FLAG_PATH, 'x') as f:
            f.write('1')

        if not xml_exists("loginTicketRequest.xml"):
            token_generation_status = await generate_afip_access_token()
        
        if xml_exists("loginTicketResponse.xml"):
            if is_expired("loginTicketResponse.xml", time_provider):
                token_generation_status = await generate_afip_access_token()
            logger.info("Token not expired.")
            token_generation_status = {"status" : "success"}
            
        if not xml_exists("loginTicketResponse.xml"):
            token_generation_status = await generate_afip_access_token()
    
        if token_generation_status["status"] == "success":
            logger.info("Token is still valid. Job finished.")
        else:
            logger.info("Couldn't generate token by scheduler.")

        return

    except FileExistsError:
        logger.info(f" [{pid}] Flag file already created.")
        return


def start_scheduler():
    logger.info("Scheduler starting: job configured to run every 11 hours")

    scheduler.add_job(
        run_job,
        trigger="interval",
        hours=11,
        id="afip_token_watchdog",
        replace_existing=True,
        max_instances=1,
        coalesce=True,
        next_run_time=datetime.now(timezone.utc)
    )
    scheduler.start()   

def stop_scheduler():
    scheduler.shutdown(wait=False)