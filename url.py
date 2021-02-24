import json, requests
headers = {
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/portal/search.html',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

print("欢迎使用QQ音乐VIP下载音乐地址解析工具。")
print()
print("GitHub：https://github.com/mstouk57g/QQmusicDownload")
print()
print("得到以“dl.stream.qqmusic.qq.com”开头的链接后，将链接粘贴到浏览器即可下载，部分浏览器（如safari）会自动启动在线播放界面。")
print()
print("操作时会遇到搜索QQ音乐，所以请提前准备好QQ音乐APP客户端（网页端显示不全）")
print()
print(50 * "*")
print()
print()
song_name = input("请输入要解析的歌曲（搜索时输入的歌曲名）：")
song_index = input("请输入搜索时的要解析第几条数：")

def get_songmid(name, page):
    music_info_list = []
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=' + page + '&n=1&w=' + name
    response = requests.get(url).text  # 获取到的是字符串
    # 将response切分成json格式 类似字典 但是现在还是字符串
    music_json = response[9:-1]
    # json转字典
    music_data = json.loads(music_json)  # 转换成 字典
    music_list = music_data['data']['song']['list']
    for music in music_list:
        music_name = music['songname']  # 歌曲的名字
        singer_name = music['singer'][0]['name']  # 歌手的名字
        songmid = music['songmid']
        media_mid = music['media_mid']
        music_info_list.append((songmid))
    return(music_info_list)

def get_vkey(music):
    songmid = str(music[0])
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % songmid
    response = requests.get(url).json()  # 如果你获取的数据 是 {}  .json() 他会直接帮我们转换成字典
    purl = response['req_0']['data']['midurlinfo'][0]['purl']
    media_url = 'http://dl.stream.qqmusic.qq.com/' + purl
    return media_url

url = get_vkey(get_songmid(song_name, song_index))
print()
print(50 * "*")
print()
print("链接：")
print()
print(url)
