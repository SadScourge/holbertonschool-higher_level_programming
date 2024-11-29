const listMovies = document.getElementById('list_movies')

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then((response) => response.json())
.then((data) => {
    const movies = data.results;
    movies.forEach(element => {
        const ul = document.createElement('li');
        ul.textContent = element.title;
        listMovies.appendChild(ul);
    });
})