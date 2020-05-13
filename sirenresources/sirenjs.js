
//Drop-down search suggestions
$(function () {
  var getData = function (request, response) {
    var url = 'https://api.genius.com/search?access_token=84WMdKzbMh7QnirAdTu5nj8iw0zkQ9vKVcAJHJdZ_miCxwgaplV_oogM-rlKRpXN&q=' + request.term;
      $.getJSON(url,function (data) {
          var data = [`${data.response.hits[0].result.full_title} | ${data.response.hits[0].result.url}`,
                      `${data.response.hits[1].result.full_title} | ${data.response.hits[1].result.url}`,
                      `${data.response.hits[2].result.full_title} | ${data.response.hits[2].result.url}`,
                      `${data.response.hits[3].result.full_title} | ${data.response.hits[3].result.url}`,
                      `${data.response.hits[4].result.full_title} | ${data.response.hits[4].result.url}`]
          response(data);
      });
  };

  var selectItem = function (event, ui) {
      $("#genlink").val(ui.item.value);
      return false;
  }

  $("#genlink").autocomplete({
      source: getData,
      select: selectItem,
      minLength: 4,
      change: function() {
          $("#genlink").val("").css("display", 2);
      }
  });
});

//Search function
function search(ele){
  if(event.key == 'Enter') {

    var selected = ele.value;
    var songLinkSplit = selected.split('|').pop();
    var songTitle = selected.split('|').shift();
    var songLink = songLinkSplit.substring(1);
    var queryLinkOriginal = 'http://104.198.233.107:5000/sirencall/original?song=' + songLink;
    var queryLinkImproved = 'http://104.198.233.107:5000/sirencall/improved?song=' + songLink;

    document.getElementById('songTitle').innerHTML = songTitle;

    fetch(queryLinkOriginal)
    .then((res) => res.json())
    .then((data) => {
      let output = '';
      data.forEach(function(post){
        output += `${post.lyrics}`;
      });
      document.getElementById('outputOriginal').innerHTML = output;
    })

    fetch(queryLinkImproved)
    .then((res) => res.json())
    .then((data) => {
      let output = '';
      data.forEach(function(post){
        output += `${post.lyrics}`;
      });
      document.getElementById('outputImproved').innerHTML = output;
    })

  }
}
