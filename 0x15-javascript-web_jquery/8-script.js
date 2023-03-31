const $ = window.$;
$.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
  const res = data.results;
  for (let x = 0; x < res.length; x++) {
    $('UL#list_movies').append('<li>' + res[i].title + '</li>');
  }
});
