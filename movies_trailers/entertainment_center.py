import fresh_tomatoes
import media

star  = media.Movie("The Last Jedi Trailer", 
		    "The Last Jedi and see it in theaters December 15.",
		    "https://lumiere-a.akamaihd.net/v1/images/the-last-jedi-theatrical-poster-film-page_bca06283.jpeg", "https://www.youtube.com/watch?v=Q0CbN8sfihY")

star_tres = media.Movie("Episodio III - La venganza de los Sith","Annos despues del inicio de las Guerra de los Clones, los nobles Caballeros Jedi lideran un gran ejercito clon en un combate de toda la galaxia contra los separatistas","https://lumiere-a.akamaihd.net/v1/images/EP3_IA_95268_A_57e9ad4e.jpeg","https://www.youtube.com/watch?v=5UnjrG_N8hU")

toy_story = media.Movie("Toy Story",
			"A story of a boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=vwyZH85NQC4")

#print(toy_story.storyline)

ragnarok = media.Movie("Thor: Ragnarok Noe",
			"Thor: Ragnarok la batalla por Asgard",
			"https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
			"https://www.youtube.com/watch?v=ue80QwXMRHg")


dragonball = media.Movie("Dragon Ball Super",
			"Dragon Ball Super la nueva aventura",
			"http://cde.laprensa.com.pe//ima/0/0/1/5/5/155253.jpg",
			"https://www.youtube.com/watch?v=wr7DMRkAnFY")

#	dragonball.show_trailer()

spider = media.Movie("Spider-Man: De regreso a casa","Peter trata de volver a su rutina diaria, aunque siempre distraido en sus pensamientos, intentando demostrar que es alguien mas que el amigable vecino Spider-Man.", "https://pbs.twimg.com/media/DAk_zUkXYAI2SGc.jpg", "https://www.youtube.com/watch?v=n9DwoQ7HWvI" )


movies = [star,toy_story,ragnarok,star_tres,dragonball,spider]
fresh_tomatoes.open_movies_page(movies)

