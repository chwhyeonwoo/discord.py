import discord #묘듈 불러오기
token = "OTAyODEwNjM1OTU0NDI5OTYz.YXj17Q.-EA6bOZ2s0AnbGmD2zkMxQb76Co" #봇 토큰 설정하기
client = discord.Client() #client 설정하기

@client.event
async def on_ready(): # 봇이 준비되었을때
    print("봇 준비 완료!")
    print(client.user)
    print("==============================")

@client.event
async def on_message(message): #사용자가 메세지를 입력했을때
    if message.content == "월요일 복장": #만일 사용자가 "월요일 복장" 라고 입력했을때
        await message.channel.send("체육복")
    if message.content == "화요일 복장": #만일 사용자가 "화요일 복장" 라고 입력했을때
        await message.channel.send("체육복")
    if message.content == "수요일 복장": #만일 사용자가 "수요일 복장" 라고 입력했을때
        await message.channel.send("체육복")
    if message.content == "목요일 복장": #만일 사용자가 "목요일 복장" 라고 입력했을때
        await message.channel.send("교복")
    if message.content == "금요일 복장": #만일 사용자가 "금요일 복장" 라고 입력했을때
        await message.channel.send("교복")


    
client.run(token)
