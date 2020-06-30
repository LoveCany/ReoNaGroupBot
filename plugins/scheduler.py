from datetime import datetime
import sys
import nonebot
import config

sys.path.append('..')


@nonebot.scheduler.scheduled_job(
    'date', run_date=datetime(2020, 6, 30, 23, 0)
)
async def _():
    await nonebot.get_bot().send_group_msg(group_id=config.GROUP_ID,
                                           message="提醒：\n"
                                                   "ReoNa新曲「Untitled World」完整版已上线！\n"
                                                   "Link：https://reona.lnk.to/Untitledworld")