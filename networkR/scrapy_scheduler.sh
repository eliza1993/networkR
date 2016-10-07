#!/bin/bash/                                                                                                                                  

#cron 表达式 每5分钟执行 一次
# */1 * * * *  sh /home/yuzhe/git/networkR/scrapy_scheduler.sh
export PATH=$PATH:/usr/local/bin

cd /home/yuzhe/git/networkR

nohup scrapy crawl networkr >> networkr.log 2>&1 &