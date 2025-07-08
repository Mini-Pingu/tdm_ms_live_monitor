import logging

logging.basicConfig(
    filename="tdm_ms_live_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

logger = logging.getLogger(__name__)
