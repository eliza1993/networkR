#!/bin/bash/                                                                                                                                  

#cron 表达式 每5分钟执行 一次
# */5 * * * *  sh /home/yuzhe/git/networkR/scrapy_scheduler.sh
export PATH=$PATH:/usr/local/bin

cd /home/yuzhe/git/networkR

nohup scrapy crawl networkr >> /home/yuzhe/git/networkR/networkr.log 2>&1 &