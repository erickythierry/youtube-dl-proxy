import youtube_dl
from fp.fp import FreeProxy

def baixar(song_url, song_title):

	sucess = False
	while not sucess:
		
		proxy = FreeProxy(rand=True).get()
		print('usando proxy', proxy)
		try:
			outtmpl = song_title + '.%(ext)s'
			ydl_opts = {
				'proxy': proxy,
				'noplaylist' : True,
				'format': 'bestaudio[ext=m4a]',
				'outtmpl': outtmpl
				
			}

			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				info_dict = ydl.extract_info(song_url, download=True)

				print('download bem sucedido')
				sucess = True

		except Exception as e:
			erro = str(e)
			print(erro)
			if 'erro' in erro.lower():
				print('erro ao baixar. tentando novamente')
		


## Modifique aqui o link e o nome do arquivo baixado. por padrão o script está baixando audio m4a
baixar('https://www.youtube.com/watch?v=CAyWN9ba9J8', 'musica')
