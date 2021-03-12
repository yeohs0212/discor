import discord
import asyncio
import datetime
import time
from datetime import datetime, timedelta
 
client = discord.Client()

@client.event

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name="민간인 부러워"))

 
@client.event
async def on_message(message):
    if message.content.startswith('준섭') or message.content.startswith('신준섭') :
        await message.channel.send('안녕...!')
        
    elif message.content.startswith('마크') :
        await message.channel.send('땅 파는중')
   
        
    elif message.content.startswith('몇시'):
        now = time.localtime()
        await message.channel.send("현재 시각 %02d:%02d:%02d 입니다! " % (now.tm_hour, now.tm_min, now.tm_sec))

        
    elif message.content.startswith('날짜'):
        now = time.localtime()
        await message.channel.send("현재 날짜 %04d/%02d/%02d 입니다! " % (now.tm_year, now.tm_mon, now.tm_mday))


    elif message.content.startswith('언제') or message.content.startswith('저녁') or message.content.startswith('전역'):
        finishday=datetime(2022,2,17,14,0,0)
        nowday=datetime.now()
        dday=finishday-nowday
        await message.channel.send("일병 신준섭 전역까지 %d 일 남았습니다!!" % (dday.days))
        
    elif message.content.startswith('어몽'):
        await message.channel.send('나도 하고 싶다...')
        time.sleep(5)
        await message.channel.send('황진웅 나가!')
        
    elif message.content.startswith('라이어'):
        await message.channel.send('이준모 광고 보고 오셈 ㅋㅋ')
    elif message.content.startswith('화생방'):
        await message.channel.send('미필은 조용히 해~')
        time.sleep(5)
        await message.channel.send('으겍!!!!')
    elif message.content.startswith('ㅋㅋㅋ'):
        await message.channel.send('ㅎㅎㅎ 같이 웃자~ ')
    elif message.content.startswith('하스'): 
        await message.channel.send('아니 거기서 동전을 왜 먼저 내ㅋㅋ 서순 ㅋㅋ ')
    elif message.content == "!명령어":
        embed = discord.Embed(title="준섭 봇 명령어 모음집", description="명령해주세요!!", color=0xAAFFFF)

        embed.add_field(name="'저녁' or '전역' or '언제'", value="준섭이가 전역까지 남은 날짜를 알려드립니다", inline=False)
        embed.add_field(name="'몇시'", value="준섭이가 현재 시각을 알려드립니다", inline=False)
        embed.add_field(name="'날짜'", value="준섭이가 오늘 날짜를 알려드립니다", inline=False)
        embed.add_field(name="'준섭' or '신준섭'", value="준섭이가 인사해줍니다", inline=False)
        embed.add_field(name="게임 목록 : '어몽' , '라이어' , '하스'", value="준섭이가 반응해줍니다", inline=False)
        embed.add_field(name="'ㅋㅋㅋ'", value="준섭이가 같이 웃어줍니다", inline=False)
        embed.add_field(name="'화생방'", value="준섭이가 화생방 훈련을 합니다", inline=False)
        await message.channel.send(embed=embed)

 
client.run('NzQ1MTk2ODE5NzAwNTE0ODQ2.XzuQng.8hMcb4to0CwYQJNobmVR8kFVlYM')
