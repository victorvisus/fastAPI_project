from fastapi import Body, FastAPI

app = FastAPI()
movies = [
    {
        "id": 87,
        "title": "As It Is in Life",
        "year": 1910,
        "cast": ["George Nichols", "Gladys Egan", "Mary Pickford"],
        "genres": ["Romance", "Drama", "Short", "Silent"],
        "category": "Drama",
        "href": "As_It_Is_in_Life",
        "extract": "As It Is In Life is a 1910 silent short film directed by D. W. Griffith and produced and distributed by the Biograph Company. Mary Pickford appears in the film.",
    },
    {
        "id": 55,
        "title": "A Christmas Carol",
        "year": 1910,
        "cast": ["Marc McDermott", "Charles Stanton Ogle"],
        "genres": ["Drama", "Silent"],
        "category": "Silent",
        "href": "A_Christmas_Carol_(1910_film)",
        "extract": "A Christmas Carol is a 1910 silent drama film directed by J. Searle Dawley and produced at Edison Studios in The Bronx in New York City. After the 1901 British release Scrooge, or, Marley's Ghost, this American version of Charles Dickens' 1843 novella is the second oldest surviving screen adaptation of the famous literary work. It features Marc McDermott as Ebenezer Scrooge and Charles S. Ogle as Bob Cratchit.",
    },
    {
        "id": 100,
        "title": "The Courtship of Miles Standish",
        "year": 1910,
        "cast": ["Robert Z. Leonard"],
        "genres": ["Drama"],
        "href": "The_Courtship_of_Miles_Standish",
        "extract": "The Courtship of Miles Standish is an 1858 narrative poem by American poet Henry Wadsworth Longfellow about the early days of Plymouth Colony, the colonial settlement established in America by the Mayflower Pilgrims.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/en/thumb/d/da/Courtship_of_Miles_Standish_a_Plymouth_Pilgrim.jpg/320px-Courtship_of_Miles_Standish_a_Plymouth_Pilgrim.jpg",
        "thumbnail_width": 320,
        "thumbnail_height": 461,
    },
    {
        "id": 101,
        "title": "The Englishman and the Girl",
        "year": 1910,
        "cast": ["Charles Craig", "Mary Pickford"],
        "genres": ["Comedy", "Short"],
        "href": "The_Englishman_and_the_Girl",
        "extract": "The Englishman and the Girl was a 1910 short comedy film directed by D. W. Griffith. Being restored by Film Preservation Society.",
    },
    {
        "id": 102,
        "title": "Frankenstein",
        "year": 1910,
        "cast": ["Augustus Phillips", "Charles Stanton Ogle", "Mary Fuller"],
        "genres": ["Horror", "Short", "Silent"],
        "href": "Frankenstein_(1910_film)",
        "extract": "Frankenstein is a 1910 American short silent horror film produced by Edison Studios. It was directed by J. Searle Dawley, who also wrote the one-reeler's screenplay, broadly basing his \"scenario\" on Mary Shelley's 1818 novel Frankenstein; or, The Modern Prometheus. This short motion picture is generally recognized by film historians as the first screen adaptation of Shelley's work. The small cast, who are not credited in the surviving 1910 print of the film, includes Augustus Phillips as Dr. Frankenstein, Charles Ogle as Frankenstein's monster, and Mary Fuller as the doctor's fiancée.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Frankenstein_%281910%29_poster.jpg/320px-Frankenstein_%281910%29_poster.jpg",
        "thumbnail_width": 320,
        "thumbnail_height": 413,
    },
    {
        "id": 103,
        "title": "Gentleman Joe",
        "year": 1910,
        "cast": ["Harry Carey"],
        "genres": [],
        "href": "Gentleman_Joe_(film)",
        "extract": "Gentleman Joe is a 1910 American film. It stars Harry Carey in his second onscreen role.",
    },
    {
        "id": 110,
        "title": "Hemlock Hoax, the Detective",
        "year": 1910,
        "cast": [],
        "genres": ["Comedy", "Short"],
        "href": "Hemlock_Hoax,_the_Detective",
        "extract": "Hemlock Hoax, the Detective is an American short comedy film produced and distributed in 1910 by the Lubin Manufacturing Company. The silent film features a detective named Hemlock Hoax who tries to solve a murder, which unbeknownst to him is a practical joke being played on him by two young boys. It was one of many shorts designed to derive its humor from a sleuth whose name was similar to Sherlock Holmes.",
    },
    {
        "id": 104,
        "title": "The House with Closed Shutters",
        "year": 1910,
        "cast": ["Henry B. Walthall"],
        "genres": ["Drama", "Silent"],
        "href": "The_House_with_Closed_Shutters",
        "extract": "The House with Closed Shutters is a 1910 American silent drama film directed by D. W. Griffith and released by the Biograph Company. Prints of The House with Closed Shutters exist in the film archives of the Museum of Modern Art, George Eastman House, and the Library of Congress.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/The_House_with_Closed_Shutters.jpg/320px-The_House_with_Closed_Shutters.jpg",
        "thumbnail_width": 320,
        "thumbnail_height": 216,
    },
    {
        "id": 105,
        "title": "In Old California",
        "year": 1910,
        "cast": [
            "Frank Powell",
            "Arthur V. Johnson",
            "Marion Leonard",
            "Henry B. Walthall",
        ],
        "genres": ["Drama", "Silent", "Western"],
        "href": "In_Old_California_(1910_film)",
        "extract": "In Old California is a 1910 American silent Western film. It was the first film shot in Hollywood, California. It was directed by D. W. Griffith of the American Mutoscope and Biograph Company. The film is a melodrama about the Mexican era of California.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/In_old_California.jpg/320px-In_old_California.jpg",
        "thumbnail_width": 320,
        "thumbnail_height": 265,
    },
    {
        "id": 106,
        "title": "In the Border States",
        "year": 1910,
        "cast": ["Charles West"],
        "genres": ["Drama"],
        "href": "In_the_Border_States",
        "extract": "In the Border States is a 1910 American drama film directed by D. W. Griffith. Prints of the film survive in the film archives of the Museum of Modern Art and the Library of Congress.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/In_the_Border_States_29.webm/320px--In_the_Border_States_29.webm.jpg",
        "thumbnail_width": 320,
        "thumbnail_height": 240,
    },
    {
        "id": 107,
        "title": "The Lad from Old Ireland",
        "year": 1910,
        "cast": ["Sidney Olcott", "Gene Gauntier", "Thomas O'Connor"],
        "genres": ["Drama"],
        "href": "The_Lad_from_Old_Ireland",
        "extract": "The Lad from Old Ireland, also called A Lad from Old Ireland, is a one-reel 1910 American motion picture directed by and starring Sidney Olcott and written by and co-starring Gene Gauntier. It was the first film appearance of prolific actor/director J.P. McGowan.",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/2.-Lad-from-Old-Ireland-advert-.jpg/320px-2.-Lad-from-Old-Ireland-advert-.jpg",
        "thumbnail_width": 320,
        "thumbnail_height": 434,
    },
]


@app.get("/", tags=["Home"])
def home():
    return "Esta web prueba el concepto API con películas"


# Ejemplo de llamada GET con un parámetro de ruta. Es simple y no espera nada más
# de modo que por barra de navegación: .../55
@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return []


# Ejemplo de llamada a GET con parámetro Query, pasa también el nombre del parámetro y no sólo
# el valor, y además lo pasa a la función, no al decorador (ruta). Observar en la anotación
# que aparece "/" al final de la ruta para indicar que está a la espera de un parámetro y un valor
# Esto se observaría por barra de navegación, p.e., ..../?category=Drama
@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie["category"] == category:
            return movie["extract"], "Año de producción", year
    return []


@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies


# Uso de POST para agregar un nuevo elemento al array, una nueva película. Como implica creación
# no puede ser GET.
"""
@app.post('/movies', tags=['Movies' ])
def create_movie(id: int, title: str, year: int, cast: list, genres: list, category: str, href: str, extract: str):
    movies.append({'id': id,'title': title,'year': year, 'cast': cast, 'genres': genres,'category': category, 'href':href, 'extract':extract})
"""


@app.post("/movies", tags=["Movies"])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    year: int = Body(),
    category: str = Body(),
    href: str = Body(),
    extract: str = Body(),
):
    movies.append(
        {
            "id": id,
            "title": title,
            "year": year,
            "category": category,
            "href": href,
            "extract": extract,
        }
    )
    return movies


# Ejemplo de modificación de un elemnto existente en la lista de películas.
# Lo cual se hace con PUT (dentro del paradigma CRUD, sería U (update)). Se pasa el id
# de lo que queremos modificar como parámetro por linea de anotación, y también en la linea de parámetros de la función. Los parámetros funcionales
# se ponen a Body() para que se integren en un cuerpo de petición, y no dispersos


@app.put("/movies/{id}", tags=["Movies"])
def modificar_movie(
    id: int,
    title: str = Body(),
    year: int = Body(),
    category: str = Body(),
    href: str = Body(),
    extract: str = Body(),
):
    for movie in movies:
        print(movie["title"], "*******", movie["id"])
        if movie["id"] == id:
            movie["title"] = title
            movie["year"] = year
            movie["category"] = category
            movie["href"] = href
            movie["extract"] = extract
            return movies
    return movies


# Ejemplo API de eliminación de un elemento del array, con el id pasado en la ruta de la anotación, también en la linea de parámetros de la función. La lógica de búsqueda es la misma que en PUT
@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return movies
    return movies


"""
*****************
***sobre FASTAPI EN ENTORNO DE EJECUCION:
****************

En vez de usar como parte del código en una app.py (o main.py) el lanzamiento del servidor, tal y como hicimos en Flask: 
***if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)***
    
En ASGI de FAstApI, se extrae de la lógica de programación y se lleva a comando:

 uvicorn main:app --host 0.0.0.0 --port 5000 --reloaD
"""
